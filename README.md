# jyy-gse-2026

《生成式软件工程》（2026 秋，江宇 / jyy）课程材料的本地镜像与整理。
原站：<https://jyywiki.cn/GSE/2026/> ｜ 课时：每周二 10:00–12:00

> 一门讨论「当实现软件的成本骤降，什么能力还值得训练」的实验课。
> 讲义本身也是文本 → 渲染 → 讨论 → 再整理的工作流产物。

## 目录结构

```
jyy-gse-2026/
├── lecture/                 课程材料
│   ├── README.md            讲义索引（10 讲 + 2 个 Lab）
│   ├── notes/               讲义正文，Markdown（推荐从这里读）
│   ├── slides/              课堂幻灯片：HTML 原件 + Markdown + PDF
│   │   ├── slides1.html…    官网原件（可交互翻页）
│   │   ├── slides01.md…     全文可搜索版，插图在 img/
│   │   ├── pdf/             16:9 打印版，343 页
│   │   ├── embedded/        幻灯片内嵌的整篇文档（Royce、MVC 1979…）
│   │   └── vendor/          MathJax / highlight.js 本地副本（离线排版）
│   ├── labs/                实验说明
│   ├── raw-html/            官网原始 HTML 快照（可回溯）
│   └── index.html           课程主页快照
├── Resource/                讲义里引用的论文与资料
│   ├── README.md            资源索引（按类型 + 按讲义两种查法）
│   ├── papers/              经典论文：Dijkstra、Royce、Codd、Sutton、MapReduce…
│   ├── specs/               UML 2.5.1、RFC 1958、R7RS、POSIX、JLS…
│   ├── docs/                Git / Jujutsu / Kubernetes / Flink / React 等官方文档
│   └── blogs/               Fowler、Stripe、Anthropic、OpenAI 等工程文章
└── tools/                   抓取与索引脚本
    ├── fetch-lectures.py    抓讲义 + 幻灯片 + Lab
    ├── fetch-resources.py   抓 Resource 清单里的资料
    └── make-index.py        重建 Resource/README.md
```

## 从哪里开始

| 想做什么 | 去哪里 |
| --- | --- |
| 通读课程 | [`lecture/README.md`](lecture/README.md) → `lecture/notes/` |
| 看某一讲的幻灯片 | `lecture/slides/pdf/slides<N>.pdf`（打印/批注）或 `slides/slides<N>.html`（交互） |
| 搜幻灯片里的原话 | `lecture/slides/slides<NN>.md`（grep 或编辑器全局搜索） |
| 找某讲提到的论文 | [`Resource/README.md`](Resource/README.md) 的「按讲义」一节 |
| 系统读经典论文 | `Resource/papers/`（18 篇，PDF 为主） |

## 十讲一览

| # | 讲义 | 关键资源 |
| --- | --- | --- |
| 01 | 欢迎来到未来 | — |
| 02 | 提示词与上下文工程 | — |
| 03 | 版本管理 (1) | SWE-bench、Pro Git、Jujutsu |
| 04 | 版本管理 (2) | Software Traceability、Jujutsu 冲突模型 |
| 05 | 软件工程的来龙去脉 | NATO 1968、Royce 1970、Dijkstra、QuickCheck、UML |
| 06 | 需求和架构 (1) | Event Sourcing、CQRS、DDD Reference |
| 07 | 需求和架构 (2) | EWD249、Codd 1970、RFC 1958、Growing a Language |
| 08 | Agent Native 开发 | CI/CD 起源、Harness Engineering、Stripe Minions |
| 09 | DeepSeek Harness | MapReduce、幂等重试、Flink 时间与状态 |
| 10 | 软件的演化 | Python 2 退役、dockershim、SWE-bench |

## 维护

```bash
python tools/fetch-lectures.py      # 同步讲义与幻灯片
python tools/fetch-resources.py     # 下载 Resource 中缺失的资料（--force 覆盖）
python tools/make-index.py          # 重新生成 Resource/README.md
python tools/slides-to-md.py        # 幻灯片 -> Markdown（含图片/内嵌文档）
python tools/slides-to-pdf.py       # 幻灯片 -> PDF（需本机 Chrome 或 Edge）
```

依赖：`curl`、`python` + `beautifulsoup4`、`html2text`、`pypdf`。

```bash
pip install beautifulsoup4 html2text pypdf
```

少数页面（OpenAI、Medium）用 `curl` 会被 Cloudflare 拦截，是通过 Playwright
渲染后另存为 Markdown 的，重新抓取时需要浏览器。

## 版权

课程讲义、幻灯片版权归课程作者所有，采用
[CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/) 许可。
`Resource/` 中的论文与文档版权归各自原作者所有，此处仅作个人学习用途的本地副本。
