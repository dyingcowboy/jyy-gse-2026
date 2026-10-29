# Resource — 讲义引用的论文与资料

《生成式软件工程 (2026 秋)》各讲中提到的经典论文、规范、官方文档和工程文章。
全部按**类型**分目录，下面再按**讲义**列一遍，方便对照阅读。

> 重新下载：`python tools/fetch-resources.py`（已存在的文件会跳过，`--force` 强制覆盖）  
> 少数被 Cloudflare / Medium 拦截的页面用 Playwright 渲染后存为 `.md`。

## 目录

- `📄 papers/` — 经典论文与学术文献（18 个文件）
- `📐 specs/` — 标准与规范（8 个文件）
- `📚 docs/` — 官方文档与手册（47 个文件）
- `📝 blogs/` — 工程文章与案例（17 个文件）

## 按类型

### 经典论文与学术文献 `📄 papers/`

| 文件 | 标题 | 讲义 | 备注 |
| --- | --- | --- | --- |
| [`sutton-2019-the-bitter-lesson.pdf`](papers/sutton-2019-the-bitter-lesson.pdf) | [The Bitter Lesson (Rich Sutton, 2019)](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf) | L5 |  |
| [`dijkstra-1968-go-to-statement-considered-harmful.pdf`](papers/dijkstra-1968-go-to-statement-considered-harmful.pdf) | [Go To Statement Considered Harmful (Dijkstra, 1968)](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf) | L5 |  |
| [`nato-1968-software-engineering-report.pdf`](papers/nato-1968-software-engineering-report.pdf) | [Software Engineering: Report on a Conference (NATO, 1968)](https://www.scrummanager.com/files/nato1968e.pdf) | L5 |  |
| [`royce-1970-managing-the-development-of-large-software-systems.pdf`](papers/royce-1970-managing-the-development-of-large-software-systems.pdf) | [Managing the Development of Large Software Systems (Royce, 1970)](https://raw.githubusercontent.com/tpn/pdfs/master/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%201970%20(waterfall).pdf) | L5 | 原链接 dl.acm.org 付费墙, 此处为公开副本 |
| [`hughes-2000-quickcheck.pdf`](papers/hughes-2000-quickcheck.pdf) | [QuickCheck: A Lightweight Tool for Random Testing (Hughes, 2000)](https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf) | L5 |  |
| [`dahl-hoare-1966-hierarchical-program-structures.pdf`](papers/dahl-hoare-1966-hierarchical-program-structures.pdf) | [Hierarchical Program Structures (Dahl & Hoare, 1966)](https://www.informatik.uni-bremen.de/agbkb/lehre/programmiersprachen/artikel/dahl-hoare-hierarchical.pdf) | L7 |  |
| [`codd-1970-a-relational-model-of-data.pdf`](papers/codd-1970-a-relational-model-of-data.pdf) | [A Relational Model of Data for Large Shared Data Banks (Codd, 1970)](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf) | L7 | 原链接为 IBM 出版物页, 此处为可下载副本 |
| [`meyer-1992-applying-design-by-contract.pdf`](papers/meyer-1992-applying-design-by-contract.pdf) | [Applying Design by Contract (Meyer, 1992)](https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf) | L5 | 原链接为 IEEE Xplore, 此处为作者主页副本 |
| [`evans-2015-ddd-reference.pdf`](papers/evans-2015-ddd-reference.pdf) | [Domain-Driven Design Reference (Eric Evans, 2015)](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) | L6 |  |
| [`dean-ghemawat-2004-mapreduce.pdf`](papers/dean-ghemawat-2004-mapreduce.pdf) | [MapReduce: Simplified Data Processing on Large Clusters (OSDI 2004)](https://static.usenix.org/event/osdi04/tech/full_papers/dean/dean.pdf) | L9 |  |
| [`steele-1998-growing-a-language.pdf`](papers/steele-1998-growing-a-language.pdf) | [Growing a Language (Guy Steele, 1998)](https://langev.com/pdf/steele99growing.pdf) | L7 |  |
| [`jimenez-2023-swe-bench.pdf`](papers/jimenez-2023-swe-bench.pdf) | [SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023)](https://arxiv.org/pdf/2310.06770) | L3, L10 |  |
| [`silver-2017-alphazero.pdf`](papers/silver-2017-alphazero.pdf) | [Mastering Chess and Shogi by Self-Play (AlphaZero, 2017)](https://arxiv.org/pdf/1712.01815) | Lab2 |  |
| [`humanize-2026-judgement-engineering-for-agentic-coding.pdf`](papers/humanize-2026-judgement-engineering-for-agentic-coding.pdf) | [Humanize: Judgement Engineering for Agentic Coding (2026)](https://arxiv.org/pdf/2610.08900) | Lab2 |  |
| [`dijkstra-ewd249-notes-on-structured-programming.html`](papers/dijkstra-ewd249-notes-on-structured-programming.html) | [Notes on Structured Programming (Dijkstra, EWD249, 1970)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html) | L7 |  |
| [`dijkstra-ewd340-the-humble-programmer.html`](papers/dijkstra-ewd340-the-humble-programmer.html) | [The Humble Programmer (Dijkstra, EWD340, 1972)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html) | L5 |  |
| [`sutton-2019-the-bitter-lesson.html`](papers/sutton-2019-the-bitter-lesson.html) | [The Bitter Lesson (作者主页 HTML 版)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) | L5 |  |
| [`cleland-huang-2014-software-traceability-trends-and-future-directions.pdf`](papers/cleland-huang-2014-software-traceability-trends-and-future-directions.pdf) | [Software Traceability: Trends and Future Directions (2014)](https://selab.netlab.uky.edu/homepage/publications/2014-ICSE-FOSE.pdf) | L4 | 原链接 dl.acm.org 付费墙, 此处为作者主页副本 |

### 标准与规范 `📐 specs/`

| 文件 | 标题 | 讲义 | 备注 |
| --- | --- | --- | --- |
| [`uml-2.5.1-specification.pdf`](specs/uml-2.5.1-specification.pdf) | [OMG UML 2.5.1 规范 (2017)](https://www.omg.org/spec/UML/2.5.1/PDF) | L5 | 9.6 MB |
| [`rfc1958-architectural-principles-of-the-internet.html`](specs/rfc1958-architectural-principles-of-the-internet.html) | [RFC 1958: Architectural Principles of the Internet (1996)](https://www.rfc-editor.org/rfc/rfc1958.html) | L7 |  |
| [`r7rs-scheme-report.html`](specs/r7rs-scheme-report.html) | [R7RS: Revised^7 Report on the Algorithmic Language Scheme](https://standards.scheme.org/r7rs-html5/index.html) | L7 |  |
| [`posix-chap12-utility-conventions.html`](specs/posix-chap12-utility-conventions.html) | [POSIX: Utility Conventions (命令行约定)](https://pubs.opengroup.org/onlinepubs/9699919799.orig/basedefs/V1_chap12.html) | L7 |  |
| [`posix-shell-command-language.html`](specs/posix-shell-command-language.html) | [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) | L7 |  |
| [`conventional-commits-1.0.0.html`](specs/conventional-commits-1.0.0.html) | [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) | L3 |  |
| [`java-language-specification-se7.html`](specs/java-language-specification-se7.html) | [The Java Language Specification (SE 7)](https://docs.oracle.com/javase/specs/jls/se7/html/) | L7 |  |
| [`common-lisp-the-language-2nd-ed.html`](specs/common-lisp-the-language-2nd-ed.html) | [Common Lisp: The Language, 2nd Edition (Steele)](https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html) | L7 |  |

### 官方文档与手册 `📚 docs/`

| 文件 | 标题 | 讲义 | 备注 |
| --- | --- | --- | --- |
| [`git-internals-git-objects.html`](docs/git-internals-git-objects.html) | [Pro Git: Git Internals — Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) | L3, L4 |  |
| [`git-short-history.html`](docs/git-short-history.html) | [Pro Git: A Short History of Git](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git) | L3 |  |
| [`git-branching-and-merging.html`](docs/git-branching-and-merging.html) | [Pro Git: Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) | L3 |  |
| [`git-rebasing.html`](docs/git-rebasing.html) | [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) | L3 |  |
| [`git-rebase.html`](docs/git-rebase.html) | [git-rebase 手册](https://git-scm.com/docs/git-rebase) | L4 |  |
| [`git-worktree.html`](docs/git-worktree.html) | [git-worktree 手册](https://git-scm.com/docs/git-worktree) | L4 |  |
| [`git-bisect.html`](docs/git-bisect.html) | [git-bisect 手册](https://git-scm.com/docs/git-bisect) | L4 |  |
| [`git-blame.html`](docs/git-blame.html) | [git-blame 手册](https://git-scm.com/docs/git-blame) | L4 |  |
| [`git-notes.html`](docs/git-notes.html) | [git-notes 手册](https://git-scm.com/docs/git-notes) | L4 |  |
| [`git-add.html`](docs/git-add.html) | [git-add 手册](https://git-scm.com/docs/git-add) | L3 |  |
| [`gitignore.html`](docs/gitignore.html) | [gitignore 手册](https://git-scm.com/docs/gitignore) | L3 |  |
| [`jj-tutorial.html`](docs/jj-tutorial.html) | [Jujutsu 教程](https://docs.jj-vcs.dev/latest/tutorial/) | L3 |  |
| [`jj-conflicts.html`](docs/jj-conflicts.html) | [Jujutsu: First-class Conflicts](https://docs.jj-vcs.dev/latest/conflicts/) | L3, L4 |  |
| [`jj-operation-log.html`](docs/jj-operation-log.html) | [Jujutsu: Operation Log](https://docs.jj-vcs.dev/latest/operation-log/) | L3 |  |
| [`jj-glossary.md`](docs/jj-glossary.md) | [Jujutsu 术语表](https://raw.githubusercontent.com/jj-vcs/jj/main/docs/glossary.md) | L4 |  |
| [`jj-working-copy.md`](docs/jj-working-copy.md) | [Jujutsu: Working Copy](https://raw.githubusercontent.com/jj-vcs/jj/main/docs/working-copy.md) | L4 |  |
| [`kubernetes-controller.html`](docs/kubernetes-controller.html) | [Kubernetes: Controllers (控制器模式)](https://kubernetes.io/docs/concepts/architecture/controller/) | L10 |  |
| [`kubernetes-dockershim-faq.html`](docs/kubernetes-dockershim-faq.html) | [Kubernetes: dockershim 移除说明](https://kubernetes.io/blog/2022/02/17/dockershim-faq/) | L10 |  |
| [`python-3.0-whatsnew.html`](docs/python-3.0-whatsnew.html) | [What's New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) | L10 |  |
| [`python2-sunset.html`](docs/python2-sunset.html) | [Sunsetting Python 2 (PEP 373)](https://www.python.org/doc/sunset-python-2/) | L10 |  |
| [`postgres-transaction-isolation.html`](docs/postgres-transaction-isolation.html) | [PostgreSQL: 事务隔离](https://www.postgresql.org/docs/current/transaction-iso.html) | L3 |  |
| [`postgres-materialized-views.html`](docs/postgres-materialized-views.html) | [PostgreSQL: 物化视图](https://www.postgresql.org/docs/current/rules-materializedviews.html) | L7 |  |
| [`flink-time.html`](docs/flink-time.html) | [Flink: 时间与水印](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) | L9 |  |
| [`flink-stateful-stream-processing.html`](docs/flink-stateful-stream-processing.html) | [Flink: 有状态流处理](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/) | L9 |  |
| [`spark-rdd-guide.html`](docs/spark-rdd-guide.html) | [Spark RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html) | L9 |  |
| [`aws-idempotent-apis.html`](docs/aws-idempotent-apis.html) | [AWS: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) | L9 |  |
| [`jvm-gc-tuning-ergonomics.html`](docs/jvm-gc-tuning-ergonomics.html) | [HotSpot JVM: GC Tuning — Ergonomics](https://docs.oracle.com/en/java/javase/25/gctuning/ergonomics.html) | L9 |  |
| [`php-fpm-configuration.html`](docs/php-fpm-configuration.html) | [PHP-FPM 进程管理配置](https://www.php.net/manual/en/install.fpm.configuration.php) | L9 |  |
| [`linux-cfs-scheduler.html`](docs/linux-cfs-scheduler.html) | [Linux CFS 调度器文档](https://docs.kernel.org/scheduler/sched-design-CFS.html) | L10 |  |
| [`azure-event-sourcing.html`](docs/azure-event-sourcing.html) | [Azure 架构中心: Event Sourcing 模式](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) | L6 |  |
| [`azure-cqrs.html`](docs/azure-cqrs.html) | [Azure 架构中心: CQRS 模式](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) | L6 |  |
| [`excel-calculation-performance.html`](docs/excel-calculation-performance.html) | [Excel: 提升计算性能](https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance) | L6 |  |
| [`vue-computed.html`](docs/vue-computed.html) | [Vue: 计算属性](https://vuejs.org/guide/essentials/computed.html) | L7 |  |
| [`vue-forms.html`](docs/vue-forms.html) | [Vue: 表单输入绑定](https://vuejs.org/guide/essentials/forms.html) | L7 |  |
| [`react-thinking-in-react.html`](docs/react-thinking-in-react.html) | [React: Thinking in React](https://react.dev/learn/thinking-in-react) | L7 |  |
| [`react-state-as-a-snapshot.html`](docs/react-state-as-a-snapshot.html) | [React: State as a Snapshot](https://react.dev/learn/state-as-a-snapshot) | L7 |  |
| [`nasa-requirements-management.html`](docs/nasa-requirements-management.html) | [NASA SEH: 6.2 Requirements Management](https://www.nasa.gov/reference/6-2-requirements-management/) | L5 |  |
| [`nasa-apollo11-program-alarms.html`](docs/nasa-apollo11-program-alarms.html) | [Apollo 11: Program Alarms (1201/1202)](https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-pa.html) | L5 |  |
| [`nasa-margaret-hamilton.html`](docs/nasa-margaret-hamilton.html) | [NASA: Margaret Hamilton](https://science.nasa.gov/people/margaret-hamilton/) | L5 |  |
| [`eiffel-design-by-contract.html`](docs/eiffel-design-by-contract.html) | [Eiffel: Design by Contract 介绍](https://www.eiffel.com/values/design-by-contract/introduction/) | L5 |  |
| [`swebench-harness-api.html`](docs/swebench-harness-api.html) | [SWE-bench Harness API](https://www.swebench.com/SWE-bench/api/harness/) | L3 |  |
| [`jq-manual.html`](docs/jq-manual.html) | [jq 手册](https://jqlang.org/manual/) | L7 |  |
| [`gh-cli-manual.html`](docs/gh-cli-manual.html) | [GitHub CLI 手册](https://cli.github.com/manual/) | L3 |  |
| [`glab-cli.html`](docs/glab-cli.html) | [GitLab CLI 文档](https://docs.gitlab.com/cli/) | L3 |  |
| [`github-protected-branches.html`](docs/github-protected-branches.html) | [GitHub: 保护分支](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | L8 |  |
| [`solar-lezama-synthesis-lecture10.html`](docs/solar-lezama-synthesis-lecture10.html) | [Program Synthesis 课程讲义 (Solar-Lezama)](https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm) | L10 |  |
| [`openstax-accounting-cycle.html`](docs/openstax-accounting-cycle.html) | [会计循环: 复式记账 (OpenStax)](https://openstax.org/books/principles-financial-accounting/pages/3-3-define-and-describe-the-initial-steps-in-the-accounting-cycle) | L7 |  |

### 工程文章与案例 `📝 blogs/`

| 文件 | 标题 | 讲义 | 备注 |
| --- | --- | --- | --- |
| [`fowler-event-sourcing.html`](blogs/fowler-event-sourcing.html) | [Martin Fowler: Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) | L6, L7, L9 |  |
| [`fowler-technical-debt-quadrant.html`](blogs/fowler-technical-debt-quadrant.html) | [Martin Fowler: Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) | L4 |  |
| [`fowler-original-continuous-integration.html`](blogs/fowler-original-continuous-integration.html) | [Martin Fowler: 最初的 CI (2000)](https://martinfowler.com/articles/originalContinuousIntegration.html) | L8 |  |
| [`startuplessonslearned-mvp.html`](blogs/startuplessonslearned-mvp.html) | [Good Enough Never Is (MVP 的解读)](https://www.startuplessonslearned.com/2010/09/good-enough-never-is-or-is-it.html) | L4 |  |
| [`ghuntley-ralph.html`](blogs/ghuntley-ralph.html) | [Geoffrey Huntley: Ralph](https://ghuntley.com/ralph/) | L8 |  |
| [`continuous-delivery-vs-deployment.html`](blogs/continuous-delivery-vs-deployment.html) | [Continuous Delivery vs Continuous Deployment](https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/) | L8 |  |
| [`stripe-minions-part2.html`](blogs/stripe-minions-part2.html) | [Stripe Minions: one-shot end-to-end coding agents (part 2)](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2) | L8 |  |
| [`anthropic-building-c-compiler.html`](blogs/anthropic-building-c-compiler.html) | [Anthropic: Building a C compiler with an agent](https://www.anthropic.com/engineering/building-c-compiler) | L8 |  |
| [`strongdm-factory.html`](blogs/strongdm-factory.html) | [StrongDM Software Factory](https://factory.strongdm.ai/) | L8 |  |
| [`strongdm-digital-twin-universe.html`](blogs/strongdm-digital-twin-universe.html) | [StrongDM: Digital Twin Universe](https://factory.strongdm.ai/techniques/dtu) | L8 |  |
| [`openai-harness-engineering.md`](blogs/openai-harness-engineering.md) | [OpenAI: Harness Engineering (2026-02-11)](https://openai.com/index/harness-engineering/) | L8 | 需浏览器渲染 |
| [`openai-scientific-understanding.md`](blogs/openai-scientific-understanding.md) | [OpenAI: Building scientific understanding with academic communities (2026-10-26)](https://openai.com/index/building-scientific-understanding-with-academic-communities/) | L10 | 需浏览器渲染 |
| [`typesafe-system-one-models-and-jev.html`](blogs/typesafe-system-one-models-and-jev.html) | [TypeSafe: System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | L5 |  |
| [`unorthodox-approach-to-database-design.html`](blogs/unorthodox-approach-to-database-design.html) | [An unorthodox approach to database design (2006)](http://mysqldba.blogspot.com/2006/11/unorthodox-approach-to-database-design.html?m=1) | L8 |  |
| [`quibi-open-letter.md`](blogs/quibi-open-letter.md) | [Quibi: An Open Letter (2020)](https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f) | L8 | 需浏览器渲染 |
| [`sec-loudcloud-s1-2000.txt`](blogs/sec-loudcloud-s1-2000.txt) | [Loudcloud S-1 招股书 (2000)](https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt) | L8 | SEC 要求带联系方式的 UA |
| [`sethrobertson-git-best-practices.html`](blogs/sethrobertson-git-best-practices.html) | [Git Best Practices](https://sethrobertson.github.io/GitBestPractices/) | L3 |  |

## 按讲义

### L03 版本管理 (1)

- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023)](https://arxiv.org/pdf/2310.06770) → `papers/jimenez-2023-swe-bench.pdf`
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) → `specs/conventional-commits-1.0.0.html`
- [Pro Git: Git Internals — Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) → `docs/git-internals-git-objects.html`
- [Pro Git: A Short History of Git](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git) → `docs/git-short-history.html`
- [Pro Git: Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) → `docs/git-branching-and-merging.html`
- [Pro Git: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) → `docs/git-rebasing.html`
- [git-add 手册](https://git-scm.com/docs/git-add) → `docs/git-add.html`
- [gitignore 手册](https://git-scm.com/docs/gitignore) → `docs/gitignore.html`
- [Jujutsu 教程](https://docs.jj-vcs.dev/latest/tutorial/) → `docs/jj-tutorial.html`
- [Jujutsu: First-class Conflicts](https://docs.jj-vcs.dev/latest/conflicts/) → `docs/jj-conflicts.html`
- [Jujutsu: Operation Log](https://docs.jj-vcs.dev/latest/operation-log/) → `docs/jj-operation-log.html`
- [PostgreSQL: 事务隔离](https://www.postgresql.org/docs/current/transaction-iso.html) → `docs/postgres-transaction-isolation.html`
- [SWE-bench Harness API](https://www.swebench.com/SWE-bench/api/harness/) → `docs/swebench-harness-api.html`
- [GitHub CLI 手册](https://cli.github.com/manual/) → `docs/gh-cli-manual.html`
- [GitLab CLI 文档](https://docs.gitlab.com/cli/) → `docs/glab-cli.html`
- [Git Best Practices](https://sethrobertson.github.io/GitBestPractices/) → `blogs/sethrobertson-git-best-practices.html`
- [Learn Git Branching](https://learngitbranching.js.org/) — 仅链接 (交互式练习)
- [61A Code](https://code.cs61a.org/) — 仅链接 (在线编辑器)
- [Astropy Issue #12906](https://github.com/astropy/astropy/issues/12906) — 仅链接 (GitHub)
- [Astropy PR #12907](https://github.com/astropy/astropy/pull/12907) — 仅链接 (GitHub)
- [Astropy PR #12907 (diff)](https://github.com/astropy/astropy/pull/12907/files) — 仅链接 (GitHub)
- [SWE-bench 官网](https://www.swebench.com/) — 仅链接

### L04 版本管理 (2)

- [Software Traceability: Trends and Future Directions (2014)](https://selab.netlab.uky.edu/homepage/publications/2014-ICSE-FOSE.pdf) → `papers/cleland-huang-2014-software-traceability-trends-and-future-directions.pdf`
- [Pro Git: Git Internals — Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) → `docs/git-internals-git-objects.html`
- [git-rebase 手册](https://git-scm.com/docs/git-rebase) → `docs/git-rebase.html`
- [git-worktree 手册](https://git-scm.com/docs/git-worktree) → `docs/git-worktree.html`
- [git-bisect 手册](https://git-scm.com/docs/git-bisect) → `docs/git-bisect.html`
- [git-blame 手册](https://git-scm.com/docs/git-blame) → `docs/git-blame.html`
- [git-notes 手册](https://git-scm.com/docs/git-notes) → `docs/git-notes.html`
- [Jujutsu: First-class Conflicts](https://docs.jj-vcs.dev/latest/conflicts/) → `docs/jj-conflicts.html`
- [Jujutsu 术语表](https://raw.githubusercontent.com/jj-vcs/jj/main/docs/glossary.md) → `docs/jj-glossary.md`
- [Jujutsu: Working Copy](https://raw.githubusercontent.com/jj-vcs/jj/main/docs/working-copy.md) → `docs/jj-working-copy.md`
- [Martin Fowler: Technical Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) → `blogs/fowler-technical-debt-quadrant.html`
- [Good Enough Never Is (MVP 的解读)](https://www.startuplessonslearned.com/2010/09/good-enough-never-is-or-is-it.html) → `blogs/startuplessonslearned-mvp.html`
- [Jujutsu 主页](https://www.jj-vcs.dev/latest/) — 仅链接

### L05 软件工程的来龙去脉

- [The Bitter Lesson (Rich Sutton, 2019)](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf) → `papers/sutton-2019-the-bitter-lesson.pdf`
- [Go To Statement Considered Harmful (Dijkstra, 1968)](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf) → `papers/dijkstra-1968-go-to-statement-considered-harmful.pdf`
- [Software Engineering: Report on a Conference (NATO, 1968)](https://www.scrummanager.com/files/nato1968e.pdf) → `papers/nato-1968-software-engineering-report.pdf`
- [Managing the Development of Large Software Systems (Royce, 1970)](https://raw.githubusercontent.com/tpn/pdfs/master/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%201970%20(waterfall).pdf) → `papers/royce-1970-managing-the-development-of-large-software-systems.pdf`
- [QuickCheck: A Lightweight Tool for Random Testing (Hughes, 2000)](https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf) → `papers/hughes-2000-quickcheck.pdf`
- [Applying Design by Contract (Meyer, 1992)](https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf) → `papers/meyer-1992-applying-design-by-contract.pdf`
- [The Humble Programmer (Dijkstra, EWD340, 1972)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html) → `papers/dijkstra-ewd340-the-humble-programmer.html`
- [The Bitter Lesson (作者主页 HTML 版)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) → `papers/sutton-2019-the-bitter-lesson.html`
- [OMG UML 2.5.1 规范 (2017)](https://www.omg.org/spec/UML/2.5.1/PDF) → `specs/uml-2.5.1-specification.pdf`
- [NASA SEH: 6.2 Requirements Management](https://www.nasa.gov/reference/6-2-requirements-management/) → `docs/nasa-requirements-management.html`
- [Apollo 11: Program Alarms (1201/1202)](https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-pa.html) → `docs/nasa-apollo11-program-alarms.html`
- [NASA: Margaret Hamilton](https://science.nasa.gov/people/margaret-hamilton/) → `docs/nasa-margaret-hamilton.html`
- [Eiffel: Design by Contract 介绍](https://www.eiffel.com/values/design-by-contract/introduction/) → `docs/eiffel-design-by-contract.html`
- [TypeSafe: System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) → `blogs/typesafe-system-one-models-and-jev.html`
- [Jev 演示 (Bilibili)](https://www.bilibili.com/video/BV1x1ex6TEFu/) — 仅链接 (视频)
- [1968 年 9 月《Boys' Life》](https://books.google.com/books?id=gmA305LImsYC&pg=PA24) — 仅链接 (Google Books)
- [OMG UML 2.5.1 规范页](https://www.omg.org/spec/UML/2.5.1) — 仅链接
- [Dafny](https://dafny.org/) — 仅链接 (工具)
- [Verus](https://github.com/verus-lang/verus) — 仅链接 (工具)

### L06 需求和架构 (1)

- [Domain-Driven Design Reference (Eric Evans, 2015)](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) → `papers/evans-2015-ddd-reference.pdf`
- [Azure 架构中心: Event Sourcing 模式](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) → `docs/azure-event-sourcing.html`
- [Azure 架构中心: CQRS 模式](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) → `docs/azure-cqrs.html`
- [Excel: 提升计算性能](https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance) → `docs/excel-calculation-performance.html`
- [Martin Fowler: Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) → `blogs/fowler-event-sourcing.html`
- [不工整的用户系统 (微信公众号)](https://mp.weixin.qq.com/s/ibm6hFMc_JaMOWlqg7RF7A) — 仅链接 (需登录)

### L07 需求和架构 (2)

- [Hierarchical Program Structures (Dahl & Hoare, 1966)](https://www.informatik.uni-bremen.de/agbkb/lehre/programmiersprachen/artikel/dahl-hoare-hierarchical.pdf) → `papers/dahl-hoare-1966-hierarchical-program-structures.pdf`
- [A Relational Model of Data for Large Shared Data Banks (Codd, 1970)](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf) → `papers/codd-1970-a-relational-model-of-data.pdf`
- [Growing a Language (Guy Steele, 1998)](https://langev.com/pdf/steele99growing.pdf) → `papers/steele-1998-growing-a-language.pdf`
- [Notes on Structured Programming (Dijkstra, EWD249, 1970)](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html) → `papers/dijkstra-ewd249-notes-on-structured-programming.html`
- [RFC 1958: Architectural Principles of the Internet (1996)](https://www.rfc-editor.org/rfc/rfc1958.html) → `specs/rfc1958-architectural-principles-of-the-internet.html`
- [R7RS: Revised^7 Report on the Algorithmic Language Scheme](https://standards.scheme.org/r7rs-html5/index.html) → `specs/r7rs-scheme-report.html`
- [POSIX: Utility Conventions (命令行约定)](https://pubs.opengroup.org/onlinepubs/9699919799.orig/basedefs/V1_chap12.html) → `specs/posix-chap12-utility-conventions.html`
- [POSIX: Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) → `specs/posix-shell-command-language.html`
- [The Java Language Specification (SE 7)](https://docs.oracle.com/javase/specs/jls/se7/html/) → `specs/java-language-specification-se7.html`
- [Common Lisp: The Language, 2nd Edition (Steele)](https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html) → `specs/common-lisp-the-language-2nd-ed.html`
- [PostgreSQL: 物化视图](https://www.postgresql.org/docs/current/rules-materializedviews.html) → `docs/postgres-materialized-views.html`
- [Vue: 计算属性](https://vuejs.org/guide/essentials/computed.html) → `docs/vue-computed.html`
- [Vue: 表单输入绑定](https://vuejs.org/guide/essentials/forms.html) → `docs/vue-forms.html`
- [React: Thinking in React](https://react.dev/learn/thinking-in-react) → `docs/react-thinking-in-react.html`
- [React: State as a Snapshot](https://react.dev/learn/state-as-a-snapshot) → `docs/react-state-as-a-snapshot.html`
- [jq 手册](https://jqlang.org/manual/) → `docs/jq-manual.html`
- [会计循环: 复式记账 (OpenStax)](https://openstax.org/books/principles-financial-accounting/pages/3-3-define-and-describe-the-initial-steps-in-the-accounting-cycle) → `docs/openstax-accounting-cycle.html`
- [Martin Fowler: Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) → `blogs/fowler-event-sourcing.html`
- [fzf](https://github.com/junegunn/fzf) — 仅链接 (工具)
- [xdotool](https://github.com/jordansissel/xdotool) — 仅链接 (工具)
- [Oracle JSP 说明](https://docs.oracle.com/cd/B32110_01/web.1013/b28961/genlovw.htm) — 仅链接

### L08 Agent Native 开发

- [GitHub: 保护分支](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) → `docs/github-protected-branches.html`
- [Martin Fowler: 最初的 CI (2000)](https://martinfowler.com/articles/originalContinuousIntegration.html) → `blogs/fowler-original-continuous-integration.html`
- [Geoffrey Huntley: Ralph](https://ghuntley.com/ralph/) → `blogs/ghuntley-ralph.html`
- [Continuous Delivery vs Continuous Deployment](https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/) → `blogs/continuous-delivery-vs-deployment.html`
- [Stripe Minions: one-shot end-to-end coding agents (part 2)](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2) → `blogs/stripe-minions-part2.html`
- [Anthropic: Building a C compiler with an agent](https://www.anthropic.com/engineering/building-c-compiler) → `blogs/anthropic-building-c-compiler.html`
- [StrongDM Software Factory](https://factory.strongdm.ai/) → `blogs/strongdm-factory.html`
- [StrongDM: Digital Twin Universe](https://factory.strongdm.ai/techniques/dtu) → `blogs/strongdm-digital-twin-universe.html`
- [OpenAI: Harness Engineering (2026-02-11)](https://openai.com/index/harness-engineering/) → `blogs/openai-harness-engineering.md`
- [An unorthodox approach to database design (2006)](http://mysqldba.blogspot.com/2006/11/unorthodox-approach-to-database-design.html?m=1) → `blogs/unorthodox-approach-to-database-design.html`
- [Quibi: An Open Letter (2020)](https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f) → `blogs/quibi-open-letter.md`
- [Loudcloud S-1 招股书 (2000)](https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt) → `blogs/sec-loudcloud-s1-2000.txt`

### L09 DeepSeek Harness

- [MapReduce: Simplified Data Processing on Large Clusters (OSDI 2004)](https://static.usenix.org/event/osdi04/tech/full_papers/dean/dean.pdf) → `papers/dean-ghemawat-2004-mapreduce.pdf`
- [Flink: 时间与水印](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) → `docs/flink-time.html`
- [Flink: 有状态流处理](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/) → `docs/flink-stateful-stream-processing.html`
- [Spark RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html) → `docs/spark-rdd-guide.html`
- [AWS: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) → `docs/aws-idempotent-apis.html`
- [HotSpot JVM: GC Tuning — Ergonomics](https://docs.oracle.com/en/java/javase/25/gctuning/ergonomics.html) → `docs/jvm-gc-tuning-ergonomics.html`
- [PHP-FPM 进程管理配置](https://www.php.net/manual/en/install.fpm.configuration.php) → `docs/php-fpm-configuration.html`
- [Martin Fowler: Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) → `blogs/fowler-event-sourcing.html`
- [dsh-bot](https://github.com/Nothing1024/dsh-bot) — 仅链接 (工具)

### L10 软件的演化

- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023)](https://arxiv.org/pdf/2310.06770) → `papers/jimenez-2023-swe-bench.pdf`
- [Kubernetes: Controllers (控制器模式)](https://kubernetes.io/docs/concepts/architecture/controller/) → `docs/kubernetes-controller.html`
- [Kubernetes: dockershim 移除说明](https://kubernetes.io/blog/2022/02/17/dockershim-faq/) → `docs/kubernetes-dockershim-faq.html`
- [What's New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) → `docs/python-3.0-whatsnew.html`
- [Sunsetting Python 2 (PEP 373)](https://www.python.org/doc/sunset-python-2/) → `docs/python2-sunset.html`
- [Linux CFS 调度器文档](https://docs.kernel.org/scheduler/sched-design-CFS.html) → `docs/linux-cfs-scheduler.html`
- [Program Synthesis 课程讲义 (Solar-Lezama)](https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm) → `docs/solar-lezama-synthesis-lecture10.html`
- [OpenAI: Building scientific understanding with academic communities (2026-10-26)](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → `blogs/openai-scientific-understanding.md`
- [SWE-bench 官网](https://www.swebench.com/) — 仅链接

### Lab2 Deeper Research

- [Mastering Chess and Shogi by Self-Play (AlphaZero, 2017)](https://arxiv.org/pdf/1712.01815) → `papers/silver-2017-alphazero.pdf`
- [Humanize: Judgement Engineering for Agentic Coding (2026)](https://arxiv.org/pdf/2610.08900) → `papers/humanize-2026-judgement-engineering-for-agentic-coding.pdf`

## 仅保留链接的资料

付费墙、视频、需要登录或纯交互式的页面没有下载，只记录地址。

| 资料 | 讲义 | 说明 |
| --- | --- | --- |
| [Jev 演示 (Bilibili)](https://www.bilibili.com/video/BV1x1ex6TEFu/) | L5 | 视频 |
| [1968 年 9 月《Boys' Life》](https://books.google.com/books?id=gmA305LImsYC&pg=PA24) | L5 | Google Books |
| [不工整的用户系统 (微信公众号)](https://mp.weixin.qq.com/s/ibm6hFMc_JaMOWlqg7RF7A) | L6 | 需登录 |
| [Learn Git Branching](https://learngitbranching.js.org/) | L3 | 交互式练习 |
| [61A Code](https://code.cs61a.org/) | L3 | 在线编辑器 |
| [Astropy Issue #12906](https://github.com/astropy/astropy/issues/12906) | L3 | GitHub |
| [Astropy PR #12907](https://github.com/astropy/astropy/pull/12907) | L3 | GitHub |
| [Astropy PR #12907 (diff)](https://github.com/astropy/astropy/pull/12907/files) | L3 | GitHub |
| [Jujutsu 主页](https://www.jj-vcs.dev/latest/) | L4 |  |
| [OMG UML 2.5.1 规范页](https://www.omg.org/spec/UML/2.5.1) | L5 |  |
| [SWE-bench 官网](https://www.swebench.com/) | L3, L10 |  |
| [fzf](https://github.com/junegunn/fzf) | L7 | 工具 |
| [xdotool](https://github.com/jordansissel/xdotool) | L7 | 工具 |
| [Dafny](https://dafny.org/) | L5 | 工具 |
| [Verus](https://github.com/verus-lang/verus) | L5 | 工具 |
| [dsh-bot](https://github.com/Nothing1024/dsh-bot) | L9 | 工具 |
| [Oracle JSP 说明](https://docs.oracle.com/cd/B32110_01/web.1013/b28961/genlovw.htm) | L7 |  |

## 说明

- 论文优先存**作者主页 / 会议官网 / arXiv** 的公开副本；讲义里指向 ACM DL、IEEE Xplore 的条目
  因付费墙无法直接下载，已换成可公开访问的同一篇文献。
- 网页类资料保存的是抓取时的 HTML 快照，排版与线上版本可能有差异。
- 所有内容版权归原作者所有，仅供个人学习使用。
