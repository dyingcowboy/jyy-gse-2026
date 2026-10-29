# lecture — 讲义、幻灯片与实验

《生成式软件工程 (2026 秋)》课程材料，来自 <https://jyywiki.cn/GSE/2026/>。
课时：每周二上午 10:00–12:00 ｜ [课堂直播](https://live.bilibili.com/21816941) ｜ [视频回放](https://space.bilibili.com/202224425/lists?sid=8942017)

## notes/ — 讲义正文（Markdown）

| # | 讲义 | 主题 |
| --- | --- | --- |
| 01 | [欢迎来到未来](notes/lect01-欢迎来到未来.md) | 课程立场；Agent 与 harness；先用好再理解原理 |
| 02 | [提示词与上下文工程](notes/lect02-提示词与上下文工程.md) | 上下文、token、结构化提示 |
| 03 | [版本管理 (1)](notes/lect03-版本管理-1.md) | Git 对象模型、提交、分支、协作 |
| 04 | [版本管理 (2)](notes/lect04-版本管理-2.md) | rebase/worktree/bisect；Jujutsu 与一等冲突 |
| 05 | [软件工程的来龙去脉](notes/lect05-软件工程的来龙去脉.md) | 软件危机、Royce、契约、UML、形式化 |
| 06 | [需求和架构 (1)](notes/lect06-需求和架构-1.md) | 事件溯源、CQRS、DDD |
| 07 | [需求和架构 (2)](notes/lect07-需求和架构-2.md) | 结构化编程、接口与约定、数据模型 |
| 08 | [Agent Native 开发](notes/lect08-Agent-Native-开发.md) | CI/CD、harness、one-shot agent 的工程实践 |
| 09 | [DeepSeek Harness](notes/lect09-DeepSeek-Harness.md) | harness 设计：幂等、重试、状态与流处理 |
| 10 | [软件的演化](notes/lect10-软件的演化.md) | 兼容性、演化与迁移、SWE-bench |

## slides/ — 课堂幻灯片

每讲三份等价材料，按需取用：

| 形式 | 文件 | 用途 |
| --- | --- | --- |
| 原始 HTML | `slides/slides1.html` … `slides10.html` | 官网原件，浏览器打开可交互翻页（离线可用） |
| Markdown | `slides/slides01.md` … `slides10.md` | 全文可搜索 / 可 diff；插图在 `slides/img/` |
| PDF | `slides/pdf/slides01.pdf` … `slides10.pdf` | 16:9，一页一张，共 343 页，适合打印与批注 |

`slides/embedded/` 是幻灯片里以 data URI 内嵌的整篇文档（Royce 1970 全文、
Reenskaug 的 MVC 1979 PDF、记账凭证示例、办公 Agent 需求规格书）。

重新生成（需要本机 Chrome/Edge）：

```bash
python tools/slides-to-md.py          # HTML -> Markdown + 图片/内嵌文档
python tools/slides-to-pdf.py         # HTML -> PDF（可带编号，如 1 5 9）
```

`slides/vendor/` 里是 MathJax 与 highlight.js 的本地副本，保证离线也能正确排版公式和代码。

## labs/ — 实验

- [Lab1: 个人数字助手](labs/lab01-Lab1-个人数字助手.md)
- [Lab2: Deeper Research](labs/lab02-Lab2-Deeper-Research.md)

## raw-html/ — 原始页面快照

`raw-html/lect*.html`、`raw-html/lab*.html` 是官网 `.md` 链接实际返回的 HTML 原文，
`notes/` 下的 Markdown 由它转换而来（去掉了导航、页脚与重复标题）。
保留原文是为了在转换出错时能够回溯。

## 讲义引用的论文与资料

见 [`../Resource/`](../Resource/README.md) —— 按讲义和类型整理好的论文、规范、文档与文章。

## 重新同步

```bash
python tools/fetch-lectures.py        # 重新抓取讲义与幻灯片
python tools/fetch-resources.py       # 重新抓取 Resource 中的资料
python tools/make-index.py            # 重建 Resource/README.md 索引
python tools/slides-to-md.py          # 幻灯片 -> Markdown
python tools/slides-to-pdf.py         # 幻灯片 -> PDF
```
