# 图 1 修改与验收记录

日期：2026-10-13。基线：`f67f29499dd54822305576d2230ce5154f8dedb3`。

图 1 由历史 84 条快照改为一个连通的当前文献构成图：85 条文献池分为 78 篇实际引用来源和 7 条未引用记录；78 篇按 I/S/B/T 分为 13/15/42/8。未引用记录不等同于不真实或被排除的来源。原有历史检索数字继续保留在正文和历史资料中，本图不重建 PRISMA 检索流程，也不宣称所有出版字段均已核实。

统计从 `references.bib`、有效正文引用扫描和 `literature_audit.csv` 自动计算；逐记录数据见 `../figure1_source_data.csv`，输入哈希及完整角色统计见 `source_summary.json`。未修改原文献库、角色台账、APA 配置或其他图片。

## 图形与文件

- Python / Matplotlib 确定性绘图；AI 辅助绘图代码和布局的用途已同步到图注及现有声明。
- 正式文件为嵌入 Arial 常规体与粗体的矢量 PDF，尺寸 140 × 50 mm，无嵌入位图；SVG 保留文本，400 dpi PNG 仅用于预览。
- 论文保留原图号、引用标签及跨栏环境。实际入稿文字约 7.052 pt，数字约 7.747 pt。
- 对照材料保存在本机 `tmp/figure1_revision/figure1_before_after.png`，最终页面预览为同目录 `figure1_manuscript_page.png`。

## 已执行验收

- 独立 PDF 字号检查：14 个文字段，最低 7.1 pt，无低于检查阈值的文字。
- 严格 PDF 碰撞检查：0 FAIL、0 WARN；14 个文字段完全位于填色框内，属于正常标签。
- 单一连通示意图只有一个绘图区，多面板对齐检查记录为 NOT APPLICABLE。
- `pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX` 成功，正式 PDF 仍为 22 页，图 1 位于第 3 页。首次受限环境启动 Biber 的 Windows DLL 重定位错误，经正常执行环境重试解决。
- 136 处引用命令及其顺序/引用键保持一致，展开引用为 180 个；新编译 BBL 与基线字节一致。无未定义引用或交叉引用，既有 Overfull 警告保持一致。
- 已查看独立图、等宽前后对照和正式论文第 3 页；图 1、图注、相邻图 2 与正文未见新增裁切或重叠。其余图片尚不属于本次字体修改范围。

源代码预检无 FAIL。其三项 WARN 为：未输出 TIFF（正式图为矢量 PDF）、静态工具未识别字典中的 400 dpi、静态工具未求值 `140 / 25.4` 的单位换算。实际 PDF 尺寸、字体和内容已单独核实，不能将这三项 WARN 当作已自动通过。

机器验收以 `acceptance.json` 为准；本轮没有重新执行 APA 14/15 样例或重新阅读全文献，旧的 APA 验收文件保持其原阶段记录，不代表本次图形修改后的全文 PDF 哈希。

## 再生成

安装 `requirements.txt` 中记录的 Python 依赖后，在仓库根目录执行：

```powershell
python tools/generate_reference_figures.py --figure1
```

只更新图 1、其源数据及摘要；原脚本其他输出不在此入口中运行。需要 nature-figure 对齐记录时，可通过 `--qa-scripts` 指定该技能的 scripts 目录。

编译可在 VS Code 中执行现有的四阶段流程，也可以运行 `./build.ps1`。本次基线保存在本机 `tmp/figure1_revision/`，保留该目录后可运行 `python tools/verify_figure1_revision.py` 再次进行差异和产物检查；它不会重新编译或自动标记视觉审阅完成。
