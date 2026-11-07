"""从各章课后练习中抽题，组成两套在线模拟卷，写入 docs/mock-exam.md。

用法：python tools/make_mock_exam.py   （可重复运行）

题型和分值：单选 24 题 × 2 分，判断 16 题 × 1 分，简答 3 题 × 12 分，共 100 分（各章课后练习只有单选、判断、简答三种题型）。
两套卷子的题目互不重复。
抽题规则写在 PAPERS 里：(章号, 题型, 本章第几题)。
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TYPES = {"一": "single", "二": "judge", "三": "short", "四": "other", "五": "other"}
NAMES = {"single": ("一、单项选择题", 2), "judge": ("二、判断题", 1), "short": ("三、简答题", 12)}


def chapter_dirs():
    return {int(p.name[:2]): p.name for p in sorted((DOCS / "chapters").iterdir()) if p.is_dir()}


def parse(num, d):
    """返回 {题型: [题目块文本, ...]}，题目块包括题干和“答案与解析”"""
    text = (DOCS / "chapters" / d / "summary.md").read_text(encoding="utf-8")
    text = text.split("## 课后练习", 1)[1].split("\n## ", 1)[0]
    out, cur = {}, None
    for part in re.split(r"\n(?=\*\*[一二三四五]、)", text):
        m = re.match(r"\*\*([一二三四五])、", part)
        if not m:
            continue
        cur = TYPES[m.group(1)]
        body = part.split("\n", 1)[1]
        start = r'<div class="quiz' if cur in ("single", "multi", "judge") else r"\*\*\d+\.\*\*"
        blocks = [b for b in re.split(rf"\n(?={start})", "\n" + body) if re.match(start, b)]
        out[cur] = [fix_links(b.rstrip() + "\n", d) for b in blocks]
    return out


def fix_links(s, d):
    """章内的相对链接改成从 docs/ 根目录出发"""
    s = re.sub(r"\]\((#[^)]+)\)", lambda m: f"](chapters/{d}/summary.md{m.group(1)})", s)
    s = s.replace("](../../", "](")
    s = re.sub(r"\]\((?!https?:|chapters/|appendix/|sims/|#)([^)]+)\)", lambda m: f"](chapters/{d}/{m.group(1)})", s)
    s = s.replace('src="../../', 'src="')
    return s


def renumber(block, n):
    return re.sub(r"\*\*\d+\.\*\*", f"**{n}.**", block, count=1)


# (章, 题型, 本章第几题)
PAPERS = {
    "模拟卷一": {
        "single": [(c, "single", k) for c in range(1, 9) for k in (1, 3, 5)],
        "judge": [(c, "judge", k) for c in range(1, 9) for k in (1, 3)],
        "short": [(1, "short", 1), (4, "short", 1), (8, "short", 1)],
    },
    "模拟卷二": {
        "single": [(c, "single", k) for c in range(1, 9) for k in (2, 4, 6)],
        "judge": [(c, "judge", k) for c in range(1, 9) for k in (2, 4)],
        "short": [(2, "short", 2), (5, "short", 2), (7, "short", 2)],
    },
}


REVIEW = """## 复习要点

| 章 | 必须掌握 | 了解即可 |
|---|---|---|
| 第 1 章 AI 导论 | AI 的四种定义、图灵测试；三次浪潮与三大流派；弱 AI 与通用 AI；大模型的三大支柱（算法、算力、数据）；幻觉 | 缩放法则、涌现的争议；算力发展史 |
| 第 2 章 机器学习的底层逻辑 | 神经网络怎样从错误中学习；快思考与慢思考；Transformer 和注意力的作用 | 反向传播、注意力的计算细节（选学） |
| 第 3 章 语言智能 | 预训练、微调、对齐三阶段；温度；CO-STAR 提示词法则；RAG 的原理和用途；幻觉的成因与应对 | 词向量；国内外大模型格局 |
| 第 4 章 视听觉醒 | CNN 怎样“看”图；扩散模型的加噪与去噪；语音识别与合成；深度伪造的识别与标识 | GAN 的原理；AIGC 工具的版本变化 |
| 第 5 章 智能体 | 智能体的四大支柱（大脑、记忆、规划、工具）；零代码搭建智能体；多智能体协作的三种模式；具身智能 | MCP 等协议的细节 |
| 第 6 章 AI+X | 工具赋能、流程重构、生态颠覆三层模型；用三层模型分析自己专业的 AI 应用 | 各行业案例的具体数据 |
| 第 7 章 AI 安全 | 深度伪造与诈骗防范；对抗样本和提示词注入；个人信息保护；红队测试和纵深防御 | 差分隐私、联邦学习、同态加密的数学细节 |
| 第 8 章 AI 伦理 | AI 生成物版权的判断思路；算法偏见的三个来源；人机协作（半人马模式）；生成式 AI 办法的核心要求 | 公平性的数学定义；各国监管条文细节 |
"""


def main():
    dirs = chapter_dirs()
    bank = {c: parse(c, d) for c, d in dirs.items()}
    lines = ["---", "title: 期末复习与模拟卷", "description: 期末复习要点和两套模拟卷，从各章课后练习中组卷，可以直接作答并查看解析", "---", "",
             "# 期末复习与模拟卷", "",
             REVIEW,
             "下面两套模拟卷从各章课后练习中抽题组成，覆盖全书 8 章，两套卷子的题目互不重复。期末采用开卷还是闭卷由任课教师决定，题型和分值仅供参考：",
             "", "| 题型 | 题数 | 每题分值 | 合计 |", "|---|---|---|---|"]
    for t, (name, score) in NAMES.items():
        k = len(PAPERS["模拟卷一"][t])
        lines.append(f"| {name[2:]} | {k} | {score} | {k * score} |")
    lines += ["", "建议限时 90 分钟，先独立做完一整套，再展开“答案与解析”核对。简答题按参考答案的要点自评。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。", ""]
    for paper, spec in PAPERS.items():
        lines += [f"## {paper}", ""]
        for t, (name, score) in NAMES.items():
            lines += [f"**{name}**（每题 {score} 分）", ""]
            for i, (c, typ, k) in enumerate(spec[t], 1):
                lines += [renumber(bank[c][typ][k - 1], i).rstrip(), ""]
    (DOCS / "mock-exam.md").write_text("\n".join(lines), encoding="utf-8")
    print("已生成 docs/mock-exam.md：", {p: sum(len(v) for v in s.values()) for p, s in PAPERS.items()})


if __name__ == "__main__":
    main()
