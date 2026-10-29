#!/usr/bin/env python3
"""把 slides*.html 渲染成 16:9 的 PDF（每页一张幻灯片）。

原理: 幻灯片是 JS 渲染的，正文在 #slides-data 里。这里生成一个"打印版"页面，
沿用原 deck 的 CSS，把每张幻灯片放进固定 1280x720 的盒子，再跑一次与原
deck 相同的等比缩放（fit），最后用 headless Chrome 打印成 PDF。

用法:  python tools/slides-to-pdf.py [编号...]     # 缺省处理 1..10
依赖:  本机 Chrome / Edge；需要联网（MathJax、highlight.js 走 CDN）
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES = os.path.join(ROOT, "lecture", "slides")
PDFDIR = os.path.join(SLIDES, "pdf")

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

PRINT_CSS = """
@page { size: 1280px 720px; margin: 0; }
html, body { height: auto; overflow: visible; background: #fff; }
body { margin: 0; }
.slide {
  position: relative !important;
  inset: auto !important;
  display: block !important;
  width: 1280px; height: 720px;
  overflow: hidden;
  break-after: page;
  page-break-after: always;
  animation: none !important;
}
.slide:last-child { break-after: auto; page-break-after: auto; }
.slide .inner { transform-origin: top left; }
.slide .titlebar { margin: -3vh -4vw .8em; }
"""

BUILD_JS = """
const data = JSON.parse(document.getElementById('slides-data').textContent);
const W = 1280, H = 720;
function makeSlide(html, i) {
  const section = document.createElement('section');
  section.className = 'slide';
  const m = html.match(/^\\s*<h1[^>]*>[\\s\\S]*?<\\/h1\\s*>/i);
  const title = m ? '<div class="titlebar">' + m[0].trim() + '</div>' : '';
  const body = m ? html.slice(m[0].length) : html;
  section.innerHTML = title + '<div class="inner">' + body + '</div>';
  return section;
}
const host = document.getElementById('deck');
data.forEach((html, i) => host.appendChild(makeSlide(html, i)));

function fit() {
  document.querySelectorAll('.slide').forEach(s => {
    const inner = s.querySelector('.inner');
    const title = s.querySelector('.titlebar');
    const cs = getComputedStyle(s);
    const width = W - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    const bottom = H - parseFloat(cs.paddingBottom);
    if (title) {
      const base = parseFloat(cs.fontSize);
      let lo = 0, hi = base;
      for (let n = 0; n < 16; n++) {
        const size = (lo + hi) / 2;
        title.style.fontSize = size + 'px';
        if (title.offsetHeight <= H * 0.3 && title.scrollWidth <= title.clientWidth) lo = size;
        else hi = size;
      }
      title.style.fontSize = lo + 'px';
    }
    inner.style.transform = 'none';
    const height = Math.max(1, bottom - inner.offsetTop);
    const imgs = inner.querySelectorAll('img');
    inner.style.setProperty('--image-height', (height / Math.max(1, imgs.length)) + 'px');
    const scale = Math.min(1,
      Math.max(1, width - 1) / Math.max(1, inner.scrollWidth),
      Math.max(1, height - 1) / Math.max(1, inner.scrollHeight, inner.offsetHeight));
    inner.style.transform = 'scale(' + scale + ')';
  });
  if (window.hljs) document.querySelectorAll('pre code').forEach(el => hljs.highlightElement(el));
}

// 等 MathJax 完成排版后再统一缩放，避免公式把版面撑破
fit();
(function waitMathJax(tries) {
  if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
    MathJax.startup.promise.then(fit, fit);
  } else if (tries > 0) {
    setTimeout(() => waitMathJax(tries - 1), 50);
  }
})(200);
window.__ready = true;
"""


TEX_MARKS = (r"\frac", r"\mathrm", r"\Pr", r"\sum", r"\int", r"\mid",
             r"\mathbf", r"\text", r"\le", r"\cdot", r"\times")


def check_tex(pdf):
    """检查是否有未渲染的 TeX 残留（MathJax 没跑完的信号）。"""
    try:
        import pypdf
    except ImportError:
        return ""
    try:
        r = pypdf.PdfReader(pdf)
    except Exception:
        return ""
    bad = [i for i, p in enumerate(r.pages, 1)
           if any(k in (p.extract_text() or "").replace(" ", "") for k in TEX_MARKS)]
    return f"   pages={len(r.pages)}" + (f"  WARN raw-TeX pages: {bad}" if bad else "  math-ok")


def find_chrome():
    for p in CHROME_CANDIDATES:
        if os.path.exists(p):
            return p
    return shutil.which("chrome") or shutil.which("msedge")


def build_print_page(src, dst):
    s = open(src, encoding="utf-8").read()
    styles = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S))
    payload = re.search(r'<script id="slides-data" type="application/json">(.*?)</script>',
                        s, re.S).group(1)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    # 原 deck 里有 MathJax 配置（关键：inlineMath 用 $...$），必须原样带上，
    # 否则行内公式不会被排版。
    cfg = re.search(r"<script>\s*(MathJax\s*=\s*\{.*?\})\s*;?\s*</script>", s, re.S)
    mj_cfg = f"<script>{cfg.group(1)};</script>" if cfg else ""
    page = f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><title>{title}</title>
<style>{styles}</style>
<style>{PRINT_CSS}</style>
{mj_cfg}
<script src="../vendor/tex-svg.js"></script>
<script src="../vendor/highlight.min.js"></script>
</head><body>
<script id="slides-data" type="application/json">{payload}</script>
<div id="deck"></div>
<script>{BUILD_JS}</script>
</body></html>"""
    open(dst, "w", encoding="utf-8").write(page)


def main():
    nums = [int(a) for a in sys.argv[1:]] or list(range(1, 11))
    chrome = find_chrome()
    if not chrome:
        sys.exit("找不到 Chrome/Edge，无法打印 PDF")
    os.makedirs(PDFDIR, exist_ok=True)
    tmp = os.path.join(SLIDES, ".print")
    os.makedirs(tmp, exist_ok=True)

    for n in nums:
        src = os.path.join(SLIDES, f"slides{n}.html")
        if not os.path.exists(src):
            print(f"skip slides{n}")
            continue
        html = os.path.join(tmp, f"slides{n}.print.html")
        build_print_page(src, html)
        pdf = os.path.join(PDFDIR, f"slides{n:02d}.pdf")
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               "--virtual-time-budget=30000", f"--print-to-pdf={pdf}",
               "file:///" + html.replace("\\", "/")]
        r = subprocess.run(cmd, capture_output=True, text=True)
        size = os.path.getsize(pdf) / 1024 if os.path.exists(pdf) else 0
        print(f"slides{n:02d}.pdf  {size:8.0f} KB  {'ok' if size > 10 else 'FAILED'}{check_tex(pdf)}")
        if size <= 10 and r.stderr:
            print("   ", r.stderr.strip().splitlines()[-1][:200])

    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
