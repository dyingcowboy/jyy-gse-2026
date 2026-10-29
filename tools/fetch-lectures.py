#!/usr/bin/env python3
"""抓取 jyy《生成式软件工程 (2026 秋)》讲义、幻灯片与实验。

用法:  python tools/fetch-lectures.py
产物:
  lecture/raw-html/lect*.html   官网 .md 链接实际返回的 HTML 原文
  lecture/notes/*.md            转换后的 Markdown 讲义
  lecture/labs/*.md             实验说明
  lecture/slides/slides*.html   课堂幻灯片
  lecture/index.html            课程主页快照
"""
import html2text
import os
import re
import subprocess
import sys

from bs4 import BeautifulSoup

BASE = "https://jyywiki.cn/GSE/2026/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LECT = os.path.join(ROOT, "lecture")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

TITLES = {
    "lect1": "欢迎来到未来",
    "lect2": "提示词与上下文工程",
    "lect3": "版本管理-1",
    "lect4": "版本管理-2",
    "lect5": "软件工程的来龙去脉",
    "lect6": "需求和架构-1",
    "lect7": "需求和架构-2",
    "lect8": "Agent-Native-开发",
    "lect9": "DeepSeek-Harness",
    "lect10": "软件的演化",
    "lab1": "Lab1-个人数字助手",
    "lab2": "Lab2-Deeper-Research",
}


def get(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    p = subprocess.run(["curl", "-sSL", "-A", UA, "--max-time", "120",
                        "-o", dest, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    code = (p.stdout or "").strip()
    size = os.path.getsize(dest) if os.path.exists(dest) else 0
    print(f"[{code}] {os.path.relpath(dest, ROOT)} ({size})")
    return code == "200" and size > 512


def to_markdown(src, dst, title, source_url):
    soup = BeautifulSoup(open(src, encoding="utf-8").read(), "html.parser")
    wiki = soup.find("div", class_="wiki")
    if wiki is None:
        print("  ! 找不到 .wiki 容器, 跳过", src)
        return
    for a in wiki.find_all("a", href=True):
        if "creativecommons" in a["href"] or "beian.miit" in a["href"]:
            a.decompose()
    for tag in wiki.find_all(["script", "style"]):
        tag.decompose()

    h = html2text.HTML2Text()
    h.body_width = 0
    body = h.handle(str(wiki)).strip()
    body = re.sub(r"^# " + re.escape(title) + r"\n+", "", body)
    body = re.split(r"\n(?:Creative Commons|苏 ICP)", body)[0]
    body = re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+\n", "\n", body)).rstrip()

    header = (f"# {title}\n\n> 来源: {source_url}  \n"
              f"> 生成式软件工程 (2026 秋) · 课程讲义\n\n---\n\n")
    open(dst, "w", encoding="utf-8").write(header + body + "\n")
    print(f"  -> {os.path.relpath(dst, ROOT)} ({len(body)} chars)")


def main():
    get(BASE, os.path.join(LECT, "index.html"))

    for i in range(1, 11):
        raw = os.path.join(LECT, "raw-html", f"lect{i}.html")
        if not get(f"{BASE}lect{i}.md", raw):
            continue
        to_markdown(raw, os.path.join(LECT, "notes", f"lect{i:02d}-{TITLES[f'lect{i}']}.md"),
                    TITLES[f"lect{i}"], f"{BASE}lect{i}.md")
        get(f"{BASE}slides{i}.html", os.path.join(LECT, "slides", f"slides{i}.html"))

    for i in (1, 2):
        raw = os.path.join(LECT, "raw-html", f"lab{i}.html")
        if not get(f"{BASE}lab{i}.md", raw):
            continue
        to_markdown(raw, os.path.join(LECT, "labs", f"lab{i:02d}-{TITLES[f'lab{i}']}.md"),
                    TITLES[f"lab{i}"].replace("-", ": ", 1), f"{BASE}lab{i}.md")


if __name__ == "__main__":
    main()
