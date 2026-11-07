"""根据 data/errata.yml 生成 docs/errata.md（网络版与纸质版对照）。

用法：python tools/make_errata.py   （可重复运行）
errata.yml 每条：page（1-1、index-3、summary-5、8-index）、where、kind（事实 / 过时 / 表述 / 编排）、old、new、why
"""
import collections
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
KINDS = ["事实", "过时", "表述", "编排"]
KIND_NOTE = {"事实": "与可核查的事实、文献或数据不符", "过时": "截至 2026 年 11 月已经变化的产品、政策、数据",
             "表述": "说法绝对化、易误解或不够准确", "编排": "前后矛盾、重复、编号和结构调整"}


def chapter_dirs():
    return {int(p.name[:2]): p.name for p in sorted((DOCS / "chapters").iterdir()) if p.is_dir()}


def locate(page, dirs):
    """返回 (章号, 链接)"""
    if page.startswith(("index-", "summary-")):
        kind, n = page.split("-")
        n = int(n)
        return n, f"chapters/{dirs[n]}/{kind}.md"
    if page.endswith("-index"):
        n = int(page.split("-")[0])
        return n, f"chapters/{dirs[n]}/index.md"
    n = int(page.split("-")[0])
    return n, f"chapters/{dirs[n]}/{page}.md"


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", "<br>")


def main():
    items = yaml.safe_load((ROOT / "data/errata.yml").read_text(encoding="utf-8"))
    dirs = chapter_dirs()
    by_ch = collections.defaultdict(list)
    for it in items:
        n, link = locate(it["page"], dirs)
        by_ch[n].append((link, it))
    cnt = collections.Counter(it["kind"] for it in items)
    out = ["---", "title: 网络版与纸质版对照", "description: 网络版对纸质教材《人工智能通识教程》所做的事实更正、时效更新、表述调整和编排调整清单", "---", "",
           "# 网络版与纸质版对照", "",
           "网络版以纸质教材《人工智能通识教程》（吴迪、龚志武主编，东南大学出版社，2026 年 5 月第 1 版）为底本，章节结构和节号与纸质版基本一致。"
           "人工智能发展很快，纸质教材付印后不少产品、政策和数据已经变化；编写网络版时，编者逐条核对了书中的事实、数据和引文，"
           "发现的问题已在网络版正文中直接改正。下表逐条列出，供教师备课和纸质教材重印时参考。", "",
           "此外，网络版的随堂小测和章末课后练习是重新编写的，与纸质版的“思考与练习”不同；第 8 章的图号按网络版的插图顺序重新编排。", "",
           f"## 改动统计（共 {len(items)} 处）", "", "| 类别 | 含义 | 处数 |", "|---|---|---|"]
    out += [f"| {k} | {KIND_NOTE[k]} | {cnt[k]} |" for k in KINDS]
    out += [""]
    for n in sorted(by_ch):
        rows = by_ch[n]
        out += [f"## 第 {n} 章（{len(rows)} 处）", "", "| 位置 | 类别 | 纸质版 | 网络版 | 说明 |", "|---|---|---|---|---|"]
        for link, it in rows:
            out.append(f"| [{cell(it['where'])}]({link}) | {it['kind']} | {cell(it['old'])} | {cell(it['new'])} | {cell(it['why'])} |")
        out.append("")
    (DOCS / "errata.md").write_text("\n".join(out), encoding="utf-8")
    print("已生成 docs/errata.md：", len(items), "处", dict(cnt))


if __name__ == "__main__":
    main()
