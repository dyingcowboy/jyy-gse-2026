#!/usr/bin/env python3
"""下载 jyy《生成式软件工程 (2026 秋)》讲义中引用的论文 / 规范 / 文档 / 文章。

用法:  python tools/fetch-resources.py [--force]
输出:  Resource/{papers,specs,docs,blogs}/
清单:  每条 = (子目录, 文件名, URL, 标题, 相关讲义, 备注)
无法下载(付费墙/失效)的条目仍会记录在 Resource/README.md 的链接索引中。
"""
import os
import subprocess
import sys
import time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, "Resource")

# (dir, filename, url, title, lectures, note)
MANIFEST = [
    # ---------------- papers: 经典论文 ----------------
    ("papers", "sutton-2019-the-bitter-lesson.pdf",
     "https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf",
     "The Bitter Lesson (Rich Sutton, 2019)", "L5", ""),
    ("papers", "dijkstra-1968-go-to-statement-considered-harmful.pdf",
     "https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf",
     "Go To Statement Considered Harmful (Dijkstra, 1968)", "L5", ""),
    ("papers", "nato-1968-software-engineering-report.pdf",
     "https://www.scrummanager.com/files/nato1968e.pdf",
     "Software Engineering: Report on a Conference (NATO, 1968)", "L5", ""),
    ("papers", "royce-1970-managing-the-development-of-large-software-systems.pdf",
     "https://raw.githubusercontent.com/tpn/pdfs/master/Managing%20the%20Development%20of%20Large%20Software%20Systems%20-%201970%20(waterfall).pdf",
     "Managing the Development of Large Software Systems (Royce, 1970)", "L5",
     "原链接 dl.acm.org 付费墙, 此处为公开副本"),
    ("papers", "hughes-2000-quickcheck.pdf",
     "https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf",
     "QuickCheck: A Lightweight Tool for Random Testing (Hughes, 2000)", "L5", ""),
    ("papers", "dahl-hoare-1966-hierarchical-program-structures.pdf",
     "https://www.informatik.uni-bremen.de/agbkb/lehre/programmiersprachen/artikel/dahl-hoare-hierarchical.pdf",
     "Hierarchical Program Structures (Dahl & Hoare, 1966)", "L7", ""),
    ("papers", "codd-1970-a-relational-model-of-data.pdf",
     "https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf",
     "A Relational Model of Data for Large Shared Data Banks (Codd, 1970)", "L7",
     "原链接为 IBM 出版物页, 此处为可下载副本"),
    ("papers", "meyer-1992-applying-design-by-contract.pdf",
     "https://se.inf.ethz.ch/~meyer/publications/computer/contract.pdf",
     "Applying Design by Contract (Meyer, 1992)", "L5",
     "原链接为 IEEE Xplore, 此处为作者主页副本"),
    ("papers", "evans-2015-ddd-reference.pdf",
     "https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf",
     "Domain-Driven Design Reference (Eric Evans, 2015)", "L6", ""),
    ("papers", "dean-ghemawat-2004-mapreduce.pdf",
     "https://static.usenix.org/event/osdi04/tech/full_papers/dean/dean.pdf",
     "MapReduce: Simplified Data Processing on Large Clusters (OSDI 2004)", "L9", ""),
    ("papers", "steele-1998-growing-a-language.pdf",
     "https://langev.com/pdf/steele99growing.pdf",
     "Growing a Language (Guy Steele, 1998)", "L7", ""),
    ("papers", "jimenez-2023-swe-bench.pdf",
     "https://arxiv.org/pdf/2310.06770",
     "SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (2023)", "L3, L10", ""),
    ("papers", "silver-2017-alphazero.pdf",
     "https://arxiv.org/pdf/1712.01815",
     "Mastering Chess and Shogi by Self-Play (AlphaZero, 2017)", "Lab2", ""),
    ("papers", "humanize-2026-judgement-engineering-for-agentic-coding.pdf",
     "https://arxiv.org/pdf/2610.08900",
     "Humanize: Judgement Engineering for Agentic Coding (2026)", "Lab2", ""),
    ("papers", "dijkstra-ewd249-notes-on-structured-programming.html",
     "https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html",
     "Notes on Structured Programming (Dijkstra, EWD249, 1970)", "L7", ""),
    ("papers", "dijkstra-ewd340-the-humble-programmer.html",
     "https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html",
     "The Humble Programmer (Dijkstra, EWD340, 1972)", "L5", ""),
    ("papers", "sutton-2019-the-bitter-lesson.html",
     "http://www.incompleteideas.net/IncIdeas/BitterLesson.html",
     "The Bitter Lesson (作者主页 HTML 版)", "L5", ""),
    ("papers", "cleland-huang-2014-software-traceability-trends-and-future-directions.pdf",
     "https://selab.netlab.uky.edu/homepage/publications/2014-ICSE-FOSE.pdf",
     "Software Traceability: Trends and Future Directions (2014)", "L4",
     "原链接 dl.acm.org 付费墙, 此处为作者主页副本"),

    # ---------------- specs: 标准与规范 ----------------
    ("specs", "uml-2.5.1-specification.pdf",
     "https://www.omg.org/spec/UML/2.5.1/PDF",
     "OMG UML 2.5.1 规范 (2017)", "L5", "9.6 MB"),
    ("specs", "rfc1958-architectural-principles-of-the-internet.html",
     "https://www.rfc-editor.org/rfc/rfc1958.html",
     "RFC 1958: Architectural Principles of the Internet (1996)", "L7", ""),
    ("specs", "r7rs-scheme-report.html",
     "https://standards.scheme.org/r7rs-html5/index.html",
     "R7RS: Revised^7 Report on the Algorithmic Language Scheme", "L7", ""),
    ("specs", "posix-chap12-utility-conventions.html",
     "https://pubs.opengroup.org/onlinepubs/9699919799.orig/basedefs/V1_chap12.html",
     "POSIX: Utility Conventions (命令行约定)", "L7", ""),
    ("specs", "posix-shell-command-language.html",
     "https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html",
     "POSIX: Shell Command Language", "L7", ""),
    ("specs", "conventional-commits-1.0.0.html",
     "https://www.conventionalcommits.org/en/v1.0.0/",
     "Conventional Commits 1.0.0", "L3", ""),
    ("specs", "java-language-specification-se7.html",
     "https://docs.oracle.com/javase/specs/jls/se7/html/",
     "The Java Language Specification (SE 7)", "L7", ""),
    ("specs", "common-lisp-the-language-2nd-ed.html",
     "https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html",
     "Common Lisp: The Language, 2nd Edition (Steele)", "L7", ""),

    # ---------------- docs: 官方文档与手册 ----------------
    ("docs", "git-internals-git-objects.html",
     "https://git-scm.com/book/en/v2/Git-Internals-Git-Objects",
     "Pro Git: Git Internals — Git Objects", "L3, L4", ""),
    ("docs", "git-short-history.html",
     "https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git",
     "Pro Git: A Short History of Git", "L3", ""),
    ("docs", "git-branching-and-merging.html",
     "https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging",
     "Pro Git: Basic Branching and Merging", "L3", ""),
    ("docs", "git-rebasing.html",
     "https://git-scm.com/book/en/v2/Git-Branching-Rebasing",
     "Pro Git: Rebasing", "L3", ""),
    ("docs", "git-rebase.html", "https://git-scm.com/docs/git-rebase",
     "git-rebase 手册", "L4", ""),
    ("docs", "git-worktree.html", "https://git-scm.com/docs/git-worktree",
     "git-worktree 手册", "L4", ""),
    ("docs", "git-bisect.html", "https://git-scm.com/docs/git-bisect",
     "git-bisect 手册", "L4", ""),
    ("docs", "git-blame.html", "https://git-scm.com/docs/git-blame",
     "git-blame 手册", "L4", ""),
    ("docs", "git-notes.html", "https://git-scm.com/docs/git-notes",
     "git-notes 手册", "L4", ""),
    ("docs", "git-add.html", "https://git-scm.com/docs/git-add",
     "git-add 手册", "L3", ""),
    ("docs", "gitignore.html", "https://git-scm.com/docs/gitignore",
     "gitignore 手册", "L3", ""),
    ("docs", "jj-tutorial.html", "https://docs.jj-vcs.dev/latest/tutorial/",
     "Jujutsu 教程", "L3", ""),
    ("docs", "jj-conflicts.html", "https://docs.jj-vcs.dev/latest/conflicts/",
     "Jujutsu: First-class Conflicts", "L3, L4", ""),
    ("docs", "jj-operation-log.html", "https://docs.jj-vcs.dev/latest/operation-log/",
     "Jujutsu: Operation Log", "L3", ""),
    ("docs", "jj-glossary.md", "https://raw.githubusercontent.com/jj-vcs/jj/main/docs/glossary.md",
     "Jujutsu 术语表", "L4", ""),
    ("docs", "jj-working-copy.md", "https://raw.githubusercontent.com/jj-vcs/jj/main/docs/working-copy.md",
     "Jujutsu: Working Copy", "L4", ""),
    ("docs", "kubernetes-controller.html",
     "https://kubernetes.io/docs/concepts/architecture/controller/",
     "Kubernetes: Controllers (控制器模式)", "L10", ""),
    ("docs", "kubernetes-dockershim-faq.html",
     "https://kubernetes.io/blog/2022/02/17/dockershim-faq/",
     "Kubernetes: dockershim 移除说明", "L10", ""),
    ("docs", "python-3.0-whatsnew.html",
     "https://docs.python.org/3/whatsnew/3.0.html",
     "What's New In Python 3.0", "L10", ""),
    ("docs", "python2-sunset.html", "https://www.python.org/doc/sunset-python-2/",
     "Sunsetting Python 2 (PEP 373)", "L10", ""),
    ("docs", "postgres-transaction-isolation.html",
     "https://www.postgresql.org/docs/current/transaction-iso.html",
     "PostgreSQL: 事务隔离", "L3", ""),
    ("docs", "postgres-materialized-views.html",
     "https://www.postgresql.org/docs/current/rules-materializedviews.html",
     "PostgreSQL: 物化视图", "L7", ""),
    ("docs", "flink-time.html",
     "https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/",
     "Flink: 时间与水印", "L9", ""),
    ("docs", "flink-stateful-stream-processing.html",
     "https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/",
     "Flink: 有状态流处理", "L9", ""),
    ("docs", "spark-rdd-guide.html",
     "https://spark.apache.org/docs/latest/rdd-programming-guide.html",
     "Spark RDD Programming Guide", "L9", ""),
    ("docs", "aws-idempotent-apis.html",
     "https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/",
     "AWS: Making retries safe with idempotent APIs", "L9", ""),
    ("docs", "jvm-gc-tuning-ergonomics.html",
     "https://docs.oracle.com/en/java/javase/25/gctuning/ergonomics.html",
     "HotSpot JVM: GC Tuning — Ergonomics", "L9", ""),
    ("docs", "php-fpm-configuration.html",
     "https://www.php.net/manual/en/install.fpm.configuration.php",
     "PHP-FPM 进程管理配置", "L9", ""),
    ("docs", "linux-cfs-scheduler.html",
     "https://docs.kernel.org/scheduler/sched-design-CFS.html",
     "Linux CFS 调度器文档", "L10", ""),
    ("docs", "azure-event-sourcing.html",
     "https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing",
     "Azure 架构中心: Event Sourcing 模式", "L6", ""),
    ("docs", "azure-cqrs.html",
     "https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs",
     "Azure 架构中心: CQRS 模式", "L6", ""),
    ("docs", "excel-calculation-performance.html",
     "https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance",
     "Excel: 提升计算性能", "L6", ""),
    ("docs", "vue-computed.html", "https://vuejs.org/guide/essentials/computed.html",
     "Vue: 计算属性", "L7", ""),
    ("docs", "vue-forms.html", "https://vuejs.org/guide/essentials/forms.html",
     "Vue: 表单输入绑定", "L7", ""),
    ("docs", "react-thinking-in-react.html", "https://react.dev/learn/thinking-in-react",
     "React: Thinking in React", "L7", ""),
    ("docs", "react-state-as-a-snapshot.html", "https://react.dev/learn/state-as-a-snapshot",
     "React: State as a Snapshot", "L7", ""),
    ("docs", "nasa-requirements-management.html",
     "https://www.nasa.gov/reference/6-2-requirements-management/",
     "NASA SEH: 6.2 Requirements Management", "L5", ""),
    ("docs", "nasa-apollo11-program-alarms.html",
     "https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-pa.html",
     "Apollo 11: Program Alarms (1201/1202)", "L5", ""),
    ("docs", "nasa-margaret-hamilton.html",
     "https://science.nasa.gov/people/margaret-hamilton/",
     "NASA: Margaret Hamilton", "L5", ""),
    ("docs", "eiffel-design-by-contract.html",
     "https://www.eiffel.com/values/design-by-contract/introduction/",
     "Eiffel: Design by Contract 介绍", "L5", ""),
    ("docs", "swebench-harness-api.html", "https://www.swebench.com/SWE-bench/api/harness/",
     "SWE-bench Harness API", "L3", ""),
    ("docs", "jq-manual.html", "https://jqlang.org/manual/", "jq 手册", "L7", ""),
    ("docs", "gh-cli-manual.html", "https://cli.github.com/manual/", "GitHub CLI 手册", "L3", ""),
    ("docs", "glab-cli.html", "https://docs.gitlab.com/cli/", "GitLab CLI 文档", "L3", ""),
    ("docs", "github-protected-branches.html",
     "https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches",
     "GitHub: 保护分支", "L8", ""),
    ("docs", "solar-lezama-synthesis-lecture10.html",
     "https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm",
     "Program Synthesis 课程讲义 (Solar-Lezama)", "L10", ""),
    ("docs", "openstax-accounting-cycle.html",
     "https://openstax.org/books/principles-financial-accounting/pages/3-3-define-and-describe-the-initial-steps-in-the-accounting-cycle",
     "会计循环: 复式记账 (OpenStax)", "L7", ""),

    # ---------------- blogs: 工程文章与案例 ----------------
    ("blogs", "fowler-event-sourcing.html",
     "https://martinfowler.com/eaaDev/EventSourcing.html",
     "Martin Fowler: Event Sourcing", "L6, L7, L9", ""),
    ("blogs", "fowler-technical-debt-quadrant.html",
     "https://martinfowler.com/bliki/TechnicalDebtQuadrant.html",
     "Martin Fowler: Technical Debt Quadrant", "L4", ""),
    ("blogs", "fowler-original-continuous-integration.html",
     "https://martinfowler.com/articles/originalContinuousIntegration.html",
     "Martin Fowler: 最初的 CI (2000)", "L8", ""),
    ("blogs", "startuplessonslearned-mvp.html",
     "https://www.startuplessonslearned.com/2010/09/good-enough-never-is-or-is-it.html",
     "Good Enough Never Is (MVP 的解读)", "L4", ""),
    ("blogs", "ghuntley-ralph.html", "https://ghuntley.com/ralph/",
     "Geoffrey Huntley: Ralph", "L8", ""),
    ("blogs", "continuous-delivery-vs-deployment.html",
     "https://continuousdelivery.com/2010/08/continuous-delivery-vs-continuous-deployment/",
     "Continuous Delivery vs Continuous Deployment", "L8", ""),
    ("blogs", "stripe-minions-part2.html",
     "https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2",
     "Stripe Minions: one-shot end-to-end coding agents (part 2)", "L8", ""),
    ("blogs", "anthropic-building-c-compiler.html",
     "https://www.anthropic.com/engineering/building-c-compiler",
     "Anthropic: Building a C compiler with an agent", "L8", ""),
    ("blogs", "strongdm-factory.html", "https://factory.strongdm.ai/",
     "StrongDM Software Factory", "L8", ""),
    ("blogs", "strongdm-digital-twin-universe.html",
     "https://factory.strongdm.ai/techniques/dtu",
     "StrongDM: Digital Twin Universe", "L8", ""),
    # 下面 3 篇 curl 会被 Cloudflare/Medium 拦截, 由 tools/fetch-blocked.mjs (Playwright) 抓取
    ("blogs", "openai-harness-engineering.md",
     "https://openai.com/index/harness-engineering/",
     "OpenAI: Harness Engineering (2026-02-11)", "L8", "需浏览器渲染"),
    ("blogs", "openai-scientific-understanding.md",
     "https://openai.com/index/building-scientific-understanding-with-academic-communities/",
     "OpenAI: Building scientific understanding with academic communities (2026-10-26)", "L10", "需浏览器渲染"),
    ("blogs", "typesafe-system-one-models-and-jev.html",
     "https://typesafe.ai/blog/introducing-system-one-models-and-jev",
     "TypeSafe: System One Models and Jev", "L5", ""),
    ("blogs", "unorthodox-approach-to-database-design.html",
     "http://mysqldba.blogspot.com/2006/11/unorthodox-approach-to-database-design.html?m=1",
     "An unorthodox approach to database design (2006)", "L8", ""),
    ("blogs", "quibi-open-letter.md",
     "https://quibi-hq.medium.com/an-open-letter-from-quibi-8af6b415377f",
     "Quibi: An Open Letter (2020)", "L8", "需浏览器渲染"),
    ("blogs", "sec-loudcloud-s1-2000.txt",
     "https://www.sec.gov/Archives/edgar/data/1092657/000101287001001485/0001012870-01-001485.txt",
     "Loudcloud S-1 招股书 (2000)", "L8", "SEC 要求带联系方式的 UA"),
    ("blogs", "sethrobertson-git-best-practices.html",
     "https://sethrobertson.github.io/GitBestPractices/",
     "Git Best Practices", "L3", ""),
]

# 只在索引中保留链接(付费墙 / 视频 / 动态页面 / 需要登录)
LINK_ONLY = [
    ("Jev 演示 (Bilibili)", "https://www.bilibili.com/video/BV1x1ex6TEFu/", "L5", "视频"),
    ("1968 年 9 月《Boys' Life》", "https://books.google.com/books?id=gmA305LImsYC&pg=PA24", "L5", "Google Books"),
    ("不工整的用户系统 (微信公众号)", "https://mp.weixin.qq.com/s/ibm6hFMc_JaMOWlqg7RF7A", "L6", "需登录"),
    ("Learn Git Branching", "https://learngitbranching.js.org/", "L3", "交互式练习"),
    ("61A Code", "https://code.cs61a.org/", "L3", "在线编辑器"),
    ("Astropy Issue #12906", "https://github.com/astropy/astropy/issues/12906", "L3", "GitHub"),
    ("Astropy PR #12907", "https://github.com/astropy/astropy/pull/12907", "L3", "GitHub"),
    ("Astropy PR #12907 (diff)", "https://github.com/astropy/astropy/pull/12907/files", "L3", "GitHub"),
    ("Jujutsu 主页", "https://www.jj-vcs.dev/latest/", "L4", ""),
    ("OMG UML 2.5.1 规范页", "https://www.omg.org/spec/UML/2.5.1", "L5", ""),
    ("SWE-bench 官网", "https://www.swebench.com/", "L3, L10", ""),
    ("fzf", "https://github.com/junegunn/fzf", "L7", "工具"),
    ("xdotool", "https://github.com/jordansissel/xdotool", "L7", "工具"),
    ("Dafny", "https://dafny.org/", "L5", "工具"),
    ("Verus", "https://github.com/verus-lang/verus", "L5", "工具"),
    ("dsh-bot", "https://github.com/Nothing1024/dsh-bot", "L9", "工具"),
    ("Oracle JSP 说明", "https://docs.oracle.com/cd/B32110_01/web.1013/b28961/genlovw.htm", "L7", ""),
]


def fetch(subdir, filename, url, force=False):
    dest_dir = os.path.join(RES, subdir)
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, filename)
    if os.path.exists(dest) and os.path.getsize(dest) > 1024 and not force:
        return "skip", os.path.getsize(dest)
    tmp = dest + ".part"
    ua = "jyy-gse-mirror/1.0 (course-materials; student@example.edu)" if "sec.gov" in url else UA
    for attempt in range(3):
        p = subprocess.run(
            ["curl", "-sSL", "-A", ua, "--max-time", "120", "-o", tmp,
             "-w", "%{http_code}", url],
            capture_output=True, text=True)
        code = (p.stdout or "").strip()
        if code == "200" and os.path.exists(tmp) and os.path.getsize(tmp) > 512:
            os.replace(tmp, dest)
            return "ok", os.path.getsize(dest)
        if os.path.exists(tmp):
            os.remove(tmp)
        time.sleep(2 * (attempt + 1))
    return "fail", code


def main():
    force = "--force" in sys.argv
    results = []
    for subdir, filename, url, title, lects, note in MANIFEST:
        status, info = fetch(subdir, filename, url, force)
        results.append((status, subdir, filename, url, title, lects, note, info))
        print(f"[{status:4}] {subdir}/{filename} ({info})", flush=True)
        time.sleep(0.5)

    ok = [r for r in results if r[0] in ("ok", "skip")]
    bad = [r for r in results if r[0] == "fail"]
    print(f"\n下载成功 {len(ok)} / {len(results)}, 失败 {len(bad)}")
    for r in bad:
        print("  FAIL:", r[1], r[2], r[3])


if __name__ == "__main__":
    main()
