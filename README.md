# 人工智能通识教程（网络教材）

面向全体专科、本科学生（含非人工智能专业）的《人工智能通识教程》网络教材，与吴迪、龚志武主编的纸质教材（东南大学出版社，2026 年）配套。网页地址：https://mingzifu9.github.io/ai-literacy/

- 8 章，每节一页：学前导读、正文、交互动画、随堂小测；每章有在线体验和课后练习
- 28 个交互动画（`docs/sims/`），19 个在线体验，120 道课后练习，两套模拟卷
- 编者逐条核对了纸质版的事实和数据，281 处改动记录在 `data/errata.yml`，生成网站上的“网络版与纸质版对照”页
- 课件底稿 `slides/`、教案底稿 `lesson-plans/`，可生成 .pptx 和 .docx

## 目录结构

| 路径 | 内容 |
|---|---|
| `course.yml` | 课程配置：书名、学时、章节、附录。改完运行 `python tools/course.py sync` |
| `docs/chapters/` | 8 章正文，每章 `index.md`（章首页）、各节页面、`labs.md`（在线体验）、`summary.md`（小结与练习） |
| `docs/sims/` | 交互动画，每个动画有 `main.html` 和教学说明 `index.md` |
| `docs/appendix/` | 附录 A 法律法规、B 参考文献、C 术语表 |
| `data/errata.yml` | 网络版对纸质版的改动清单 |
| `slides/`、`lesson-plans/` | 课件和教案底稿 |
| `tools/` | 维护脚本 |
| `编写规范.md`、`系列公共术语表.md` | 系列教材共用的编写规范和术语 |

## 维护脚本

```bash
python tools/glossary_links.py anchors     # 给术语表每个术语加锚点
python tools/glossary_links.py link 03     # 第 3 章正文中的术语改成悬停可见定义的链接
python tools/glossary_links.py concepts 03 # 生成第 3 章的“本章概念清单”
python tools/graph_text.py                 # 检查学习图谱并生成文字版
python tools/book_stats.py                 # 更新首页“全书概览”统计表
python tools/course.py sync                # 按 course.yml 更新导航、首页、章节骨架等
python tools/course.py new-sim 名称 3 "标题" # 新建第 3 章的交互动画骨架
python tools/make_errata.py               # 由 data/errata.yml 生成“网络版与纸质版对照”页
python tools/make_mock_exam.py            # 从各章课后练习组两套模拟卷
python tools/export_docx.py --pdf          # 导出 Word 版和 PDF 版到 build/（需要 pandoc 和 LibreOffice）
```

## 课件、教案和 Word/PDF 版

```bash
pip install -r requirements-tools.txt      # 第一次：Python 库
npm install && npx playwright install chromium   # 第一次：渲染配图用的 Node 库和浏览器
npm run figures                            # 把 Mermaid 图和交互动画渲染成图片（课件、Word 版要用）

python tools/make_slides.py draft 3        # 从第 3 章正文生成课件底稿 slides/ch03.md，精简后再 build
python tools/make_slides.py build 3        # → build/课件/第03章 章名.pptx（all 表示全部章节）
python tools/make_lesson_plan.py draft 3   # 生成教案底稿 lesson-plans/ch03.yml，补写“【待填】”后再 build
python tools/make_lesson_plan.py build 3   # → build/教案/第03章 章名 教案.docx
python tools/export_docx.py --pdf          # → build/书名.docx 和 .pdf，动画换成截图和二维码
```

本机不想装这些工具时，在 GitHub 仓库的 **Actions → 导出课件、教案和 Word/PDF → Run workflow** 运行一次，几分钟后在运行页面底部的 Artifacts 下载全部文件。底稿（`slides/`、`lesson-plans/`）要提交到仓库，生成的文件不提交。

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve          # 浏览器打开 http://127.0.0.1:8000
mkdocs build --strict # 提交前确认没有警告
```

## 说明

- 第 3 章图 3-5、第 5 章和第 6 章的插图目前是占位图（灰底文字），收到彩色插图后放进对应章的 `images/` 目录（同名替换，或改成 .jpg 并修改正文引用）。
- 产品名称、版本和价格集中在 `docs/tool-snapshot.md`，建议每学期更新一次。
