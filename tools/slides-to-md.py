#!/usr/bin/env python3
"""把 slides*.html 里的 slides-data 提取成 Markdown，并把内联的图片 / data: 链接落成文件。

用法:  python tools/slides-to-md.py
产物:
  lecture/slides/slidesNN.md        每页一节，可搜索、可 diff
  lecture/slides/img/*              页面插图（从 base64 还原）
  lecture/slides/embedded/*         幻灯片里以 data: URI 内嵌的整篇文档
"""
import base64
import html2text
import json
import os
import re

from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES = os.path.join(ROOT, "lecture", "slides")
IMG = os.path.join(SLIDES, "img")
EMB = os.path.join(SLIDES, "embedded")

EXT = {
    "image/png": "png", "image/jpeg": "jpg", "image/webp": "webp",
    "image/gif": "gif", "image/svg+xml": "svg",
    "text/markdown": "md", "text/plain": "txt", "text/html": "html",
    "application/json": "json", "application/pdf": "pdf", "application/zip": "zip",
}


def parse_data_uri(uri):
    m = re.match(r"data:([^;,]+)(;base64)?,(.*)$", uri, re.S)
    if not m:
        return None, None
    mime, is_b64, payload = m.group(1), bool(m.group(2)), m.group(3)
    data = base64.b64decode(payload) if is_b64 else payload.encode()
    # 有些 data: URI 的 mime 不可靠，用文件头兜底
    if data[:4] == b"%PDF":
        mime = "application/pdf"
    elif data[:2] == b"PK":
        mime = "application/zip"
    return mime, data


def safe(name):
    return re.sub(r'[\\/:*?"<>|]+', "-", name).strip() or "file"


def main():
    os.makedirs(IMG, exist_ok=True)
    os.makedirs(EMB, exist_ok=True)
    h = html2text.HTML2Text()
    h.body_width = 0

    for i in range(1, 11):
        src = os.path.join(SLIDES, f"slides{i}.html")
        if not os.path.exists(src):
            continue
        s = open(src, encoding="utf-8").read()
        title = re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
        payload = re.search(r'<script id="slides-data" type="application/json">(.*?)</script>',
                            s, re.S).group(1)
        slides = json.loads(payload)

        out = [f"# {title}", "",
               f"> 来源: https://jyywiki.cn/GSE/2026/slides{i}.html  ",
               f"> 共 {len(slides)} 页 · 由 slides{i}.html 的 slides-data 提取", "", "---", ""]
        n_img = n_emb = 0

        for idx, frag in enumerate(slides, 1):
            soup = BeautifulSoup(frag, "html.parser")

            for img in soup.find_all("img"):
                uri = img.get("src", "")
                if not uri.startswith("data:"):
                    continue
                mime, data = parse_data_uri(uri)
                if not data:
                    continue
                n_img += 1
                fn = f"slides{i}-p{idx:02d}.{EXT.get(mime, 'bin')}"
                open(os.path.join(IMG, fn), "wb").write(data)
                img["src"] = f"img/{fn}"
                img["alt"] = img.get("alt") or f"第 {idx} 页插图"

            for a in soup.find_all("a", href=True):
                uri = a["href"]
                if not uri.startswith("data:"):
                    continue
                mime, data = parse_data_uri(uri)
                if not data:
                    continue
                n_emb += 1
                stem = safe(a.get_text(strip=True) or f"embedded-{n_emb}")
                if not os.path.splitext(stem)[1]:
                    stem += "." + EXT.get(mime, "bin")
                fn = f"slides{i}-{stem}"
                open(os.path.join(EMB, fn), "wb").write(data)
                a["href"] = f"embedded/{fn}"

            md = re.sub(r"\n{3,}", "\n\n", h.handle(str(soup)).strip())
            out += [f"## 第 {idx} 页", "", md or "*(空白页)*", ""]

        dst = os.path.join(SLIDES, f"slides{i:02d}.md")
        open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print(f"slides{i:02d}.md  {len(slides):>3} 页  {n_img:>2} 图  {n_emb:>2} 内嵌文档  {title}")


if __name__ == "__main__":
    main()
