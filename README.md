# Multi-agent collaborative QA — ESWA manuscript

论文入口为 `manuscript.tex`，采用 CAS 双栏模板与 APA/Biber 参考文献配置。

## 目录

| 位置 | 用途 |
| --- | --- |
| 根目录 | 主稿、原始文献库、模板、引用配置及编译入口 |
| `figures/figure1/`～`figure5/` | 正文当前使用的五张图及可编辑版本 |
| `data/` | 文献分类、检索记录、图 1 数据和 APA 字段适配源数据 |
| `submission/` | Highlights 等论文配套材料 |
| `build/manuscript.pdf` | 完整构建后发布的论文 PDF |
| `build/latex/` | 当前构建的 BBL、日志、辅助文件及 SyncTeX |
| `build/history/`、`build/baseline_20261016/` | 整理前保留的构建产物 |
| `tools/`、`tests/` | 项目工具与验证用例 |
| `audits/references/` | 文献字段、来源、APA 输出审计和历史台账 |
| `audits/figures/` | 图表来源、编辑过程、检查结果和历史基线 |
| `audits/revisions/` | 导师稿对照、修订方案、稿件备份及对比预览 |
| `audits/organization/20261016/` | 本次整理的路径映射、逐文件哈希、修改前备份和验收记录 |
| `archive/` | 当前不使用的旧章节、旧图、旧模板和历史统计数据 |
| `.cache/` | 临时 Python 依赖、下载缓存和临时预览 |
| `.vscode/` | 本项目 LaTeX Workshop 的编译与 PDF 输出配置 |

根目录的 `references.bib` 是原始文献库。APA 字段适配的源数据位于
`data/apa_reference_adaptations.json`，生成的映射仍为根目录
`eswa-apa-sourcemap.tex`。数据文件与历史证据没有因目录整理而改写。

## 编译

在项目根目录运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ./build.ps1
```

该参数只作用于本次 PowerShell 进程，不修改系统执行策略。构建依次执行
pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX，从 PATH 查找引擎。
辅助文件写入 `build/latex/`，四阶段成功后将 PDF 发布为
`build/manuscript.pdf`，不会把生成文件复制回根目录。

也可运行 `latexmk -pdf manuscript.tex`，项目 `.latexmkrc` 将其输出放入
`build/latex/`；这种方式直接查看 `build/latex/manuscript.pdf`。
LaTeX Workshop 使用项目中的四阶段构建配方，查看和 SyncTeX 路径同为
`build/latex/`。若编辑器已有正在运行的旧配方，等待其结束后再使用新配方。

环境需要兼容的 pdfLaTeX、Biber、biblatex 与 biblatex-apa；此前使用
TeX Live 2026、Biber 2.22、biblatex 3.22a、biblatex-apa 9.20。
本地构建成功不代表投稿服务器环境已验证。

## 检查与再生成

```powershell
python -B -m unittest discover -s tools -p test_active_tex.py
python -B -m unittest discover -s tests -p test_active_tex_bibpatch.py
python -B tools/run_apa_tests.py
python -B tools/verify_project_organization.py
```

APA 测试和 PDF 对比需要 PyMuPDF。原有本地依赖保存在
`.cache/python/apa7_vendor/`；需要时可在当前终端临时设置：

```powershell
$env:PYTHONPATH = (Join-Path $PWD '.cache/python/apa7_vendor')
```

图 1 再生成入口仍为 `python tools/generate_reference_figures.py --figure1`，
读取当前主稿、原始文献库及 `data/literature_audit.csv`，输出到
`figures/figure1/` 和 `data/figure1_source_data.csv`。
绘图环境版本记录在 `audits/figures/figure1/requirements.txt`。

## 历史材料与路径映射

旧报告中的日期、哈希、ZIP 内部成员名及历史路径原样保留，代表当时状态。
查找移动后的文件，请使用
`audits/organization/20261016/path_mapping.json`。
`tools/project_paths.py` 为当前工具解析旧路径，并将当前构建输出定位到
`build/`，避免把历史快照当作当前编译结果。

`complete_*`、`finalize_*`、`prepare_*` 及一次性整理脚本含有写入操作，
用于对应历史阶段，不是日常编译步骤。
旧阶段验收仍须遵守原始基线和范围条件。本次整理的验收单独记录在
`audits/organization/20261016/acceptance.json`。

本次整理不删除原文件，不合并分支，不自动提交或推送。
