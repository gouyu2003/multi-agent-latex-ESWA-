# 项目目录整理完成记录（2026-10-16）

本次按已批准方案整理文件，未删除原文件，未暂存、提交或推送 Git。

## 整理结果

- 根目录保留 11 个文件：主稿、原始文献库、CAS 模板、APA 配置、编译入口、README 和 Git 配置。
- `figures/figure1`～`figure5` 保存当前正文图片及可编辑版本；数据进入 `data/`，Highlights 进入 `submission/`。
- 文献、图表、稿件修订证据分别进入 `audits/references/`、`audits/figures/`、`audits/revisions/`。
- 旧章节、旧图、旧 BST 和历史数据进入 `archive/`；Python 依赖和普通缓存进入 `.cache/`。
- 当前构建进入 `build/latex/`，四阶段成功后发布 `build/manuscript.pdf`。
- 已同步编译脚本、LaTeX Workshop 项目配置和当前工具的路径解析。

## 内容保护

整理前快照记录 7718 个文件，移动 7661 个文件。
每个原文件的字节均在新位置或修改前备份中保留，缺失文件为 0。
另将保存主稿时编辑器自动生成的 10 个文件移入 `build/editor_generated_20261016/`，逐个校验哈希一致。

主稿仅改动 6 处图片文件路径，其中 5 处有效、1 处位于禁用旧稿块。
正文其他字节保持一致；136 处引用命令、78 篇引用来源未变。
原始 `references.bib`、CAS 模板、APA 配置和字段映射的内容保持不变。
历史台账、日期、哈希和 ZIP 内部路径未改写；工具通过路径映射查找当前文件。
原有重复图片均保留。

## 验证

| 检查 | 结果 |
| --- | --- |
| 文件完整性 | 全部通过，原始字节完整保留 |
| 引用扫描测试 | 10/10 + 3/3 通过 |
| APA 核心/扩展回归 | 14/14 + 15/15 通过 |
| 文献覆盖 | 78 篇引用来源、85 条原库记录均无遗漏或额外条目 |
| 完整构建 | pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX 成功 |
| 当前交叉引用 | 无未定义、重复有效标签或需重跑提示 |
| PDF 对比 | 23/23 页文字和 72 dpi 渲染像素逐页一致 |
| 既有 Overfull 提示 | 2 → 2，未增加 |
| Git 差异空白检查 | 通过 |

Biber 在受限环境下发生 DLL 重定位错误，已通过获准的项目构建命令重跑完整构建及 APA 回归。
PowerShell 的 Bypass 参数只用于当前进程，没有修改系统执行策略或安装软件。
PDF 比较证明整理未改变既有成品，不代表重新完成学术内容、元数据或投稿服务器验收。

## 可追溯文件

- `file_manifest.json`：整理前逐文件 SHA-256、大小、新旧位置和原跟踪状态。
- `path_mapping.json`：文件移动映射；历史报告中的旧路径原样保留。
- `directory_mapping.json`：目录映射及当前构建输出规则。
- `edited_files.json`、`before_edit/`：当前修改清单与原始字节备份。
- `manuscript_path_changes.json`：主稿六处图片路径替换。
- `editor_generated_manifest.json`：额外归档的编辑器生成文件。
- `acceptance.json`：文件、主稿、构建和逐页 PDF 对比证据。
- `tests_summary.json`：测试结果与当前配置哈希。
- `git_verification.json`：Git 检查结果。

Git 尚未暂存，移动文件会以旧路径删除和新路径未跟踪的形式显示；本次没有删除这些文件。
日常使用及构建方法见项目根目录 README。
