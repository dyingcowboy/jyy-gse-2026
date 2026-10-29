#!/usr/bin/env python3
"""根据 tools/fetch-resources.py 的清单生成 Resource/README.md 索引。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)


# 直接执行清单文件里的数据结构, 避免模块名带连字符的问题
ns = {"__file__": os.path.join(HERE, "fetch-resources.py")}
exec(open(os.path.join(HERE, "fetch-resources.py"), encoding="utf-8").read()
     .split("def fetch(")[0], ns)
MANIFEST = ns["MANIFEST"]
LINK_ONLY = ns["LINK_ONLY"]

CATS = {
    "papers": ("📄 papers/", "经典论文与学术文献"),
    "specs": ("📐 specs/", "标准与规范"),
    "docs": ("📚 docs/", "官方文档与手册"),
    "blogs": ("📝 blogs/", "工程文章与案例"),
}

LECT_NAMES = {
    "L1": "L01 欢迎来到未来",
    "L2": "L02 提示词与上下文工程",
    "L3": "L03 版本管理 (1)",
    "L4": "L04 版本管理 (2)",
    "L5": "L05 软件工程的来龙去脉",
    "L6": "L06 需求和架构 (1)",
    "L7": "L07 需求和架构 (2)",
    "L8": "L08 Agent Native 开发",
    "L9": "L09 DeepSeek Harness",
    "L10": "L10 软件的演化",
    "Lab2": "Lab2 Deeper Research",
}


def main():
    lines = []
    A = lines.append
    A("# Resource — 讲义引用的论文与资料")
    A("")
    A("《生成式软件工程 (2026 秋)》各讲中提到的经典论文、规范、官方文档和工程文章。")
    A("全部按**类型**分目录，下面再按**讲义**列一遍，方便对照阅读。")
    A("")
    A("> 重新下载：`python tools/fetch-resources.py`（已存在的文件会跳过，`--force` 强制覆盖）  ")
    A("> 少数被 Cloudflare / Medium 拦截的页面用 Playwright 渲染后存为 `.md`。")
    A("")
    A("## 目录")
    A("")
    for key, (path, desc) in CATS.items():
        n = len([r for r in MANIFEST if r[0] == key and
                 os.path.exists(os.path.join(ROOT, "Resource", key, r[1]))])
        A(f"- `{path}` — {desc}（{n} 个文件）")
    A("")

    # ---- 按类型 ----
    A("## 按类型")
    A("")
    for key, (path, desc) in CATS.items():
        items = [r for r in MANIFEST if r[0] == key]
        if not items:
            continue
        A(f"### {desc} `{path}`")
        A("")
        A("| 文件 | 标题 | 讲义 | 备注 |")
        A("| --- | --- | --- | --- |")
        for subdir, fn, url, title, lects, note in items:
            exists = os.path.exists(os.path.join(ROOT, "Resource", subdir, fn))
            name = f"[`{fn}`]({subdir}/{fn})" if exists else f"`{fn}` ❌"
            A(f"| {name} | [{title}]({url}) | {lects} | {note} |")
        A("")

    # ---- 按讲义 ----
    A("## 按讲义")
    A("")
    order = [f"L{i}" for i in range(1, 11)] + ["Lab2"]
    for lect in order:
        rows = [r for r in MANIFEST if lect in [x.strip() for x in r[4].split(",")]]
        extra = [r for r in LINK_ONLY if lect in [x.strip() for x in r[2].split(",")]]
        if not rows and not extra:
            continue
        A(f"### {LECT_NAMES[lect]}")
        A("")
        for subdir, fn, url, title, lects, note in rows:
            exists = os.path.exists(os.path.join(ROOT, "Resource", subdir, fn))
            mark = "" if exists else " ❌"
            A(f"- [{title}]({url}) → `{subdir}/{fn}`{mark}")
        for title, url, lects, note in extra:
            tag = f" ({note})" if note else ""
            A(f"- [{title}]({url}) — 仅链接{tag}")
        A("")

    # ---- 仅链接 ----
    A("## 仅保留链接的资料")
    A("")
    A("付费墙、视频、需要登录或纯交互式的页面没有下载，只记录地址。")
    A("")
    A("| 资料 | 讲义 | 说明 |")
    A("| --- | --- | --- |")
    for title, url, lects, note in LINK_ONLY:
        A(f"| [{title}]({url}) | {lects} | {note} |")
    A("")

    A("## 说明")
    A("")
    A("- 论文优先存**作者主页 / 会议官网 / arXiv** 的公开副本；讲义里指向 ACM DL、IEEE Xplore 的条目")
    A("  因付费墙无法直接下载，已换成可公开访问的同一篇文献。")
    A("- 网页类资料保存的是抓取时的 HTML 快照，排版与线上版本可能有差异。")
    A("- 所有内容版权归原作者所有，仅供个人学习使用。")
    A("")

    out = os.path.join(ROOT, "Resource", "README.md")
    open(out, "w", encoding="utf-8").write("\n".join(lines))
    print("written", out)


if __name__ == "__main__":
    main()
