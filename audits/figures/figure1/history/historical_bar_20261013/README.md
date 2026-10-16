# 图 1：历史构建过程与当前引用的横向分类色条

更新日期：2026-10-13。图 1 现为一个连通的示意图，明确区分两个统计阶段。

- 历史工作记录：108 candidates → 72 retained → 12 additions → 84 records；候选阶段另有 36 条 logged exclusions。
- 当前审计结果：85 条文献池分为 78 篇实际引用来源和 7 条未引用记录；78 篇按 I/S/B/T 分为 13/15/42/8。
- I/S/B/T 使用用户指定的横向分段色条：青绿、蓝、灰、橙四色，白色文字及细白分隔线；宽度严格按 13:15:42:8 分配，色条由 Cited sources 节点连接，完整类别名称在图注解释。

历史数字逐项读取原 `figure_source_data.csv`，保持其历史内容；当前统计从 `references.bib`、有效正文引用扫描和 `literature_audit.csv` 计算。来源哈希、历史限制及当前逐记录数据见 `source_summary.json` 与 `../figure1_source_data.csv`。

虚线的 Later source audit 表示由历史快照转向当前审计结果，不将 +12 改成 +13，不宣称已重建每条文献的检索/增删过程或完整 PRISMA 检索。7 条未引用记录不等于不存在或已排除的来源。未修改原文献库、角色台账、历史源数据、APA 配置或其他图片。

## 当前导出及检查

- Python / Matplotlib 绘制，矢量 PDF 为 140 × 88 mm；Arial 常规体与粗体均嵌入，SVG 保留文字，400 dpi PNG 为预览。
- 普通文字和色条内加粗标签 7.1 pt、节点数字 7.8 pt；保留论文原跨栏环境和 0.80 linewidth，实际入稿效果留待用户编译后检查。
- 独立图已执行字体、严格碰撞和源数据/保护检查，结果见 `font_audit.json`、`collision.json`、`acceptance.json`。单一绘图区的多面板对齐为 NOT APPLICABLE。
- 已查看新版独立预览；历史链、排除支路、虚线衔接和横向色条连接清楚，最窄 T 段标签完整，未见文字重叠或裁切。验收脚本直接读取导出 PDF 的四段矩形宽度核对比例。
- 图注和正文说明已同步历史与当前两种口径，并保留 AI 辅助绘图代码/布局的实际用途说明。
- 源码预检的三条通用提示已复核：本图以矢量 PDF 交付，无需另供 TIFF；PNG 导出实际指定 400 dpi；预检未解析 `140 / 25.4` 尺寸表达式，实际 PDF 已验证为 140 × 88 mm。

**本次没有重新编译全文，按用户要求由其在 VS Code 中完成。** 当前 `manuscript.pdf` 未由本轮更新，横向色条在全文中的分页及相邻图表效果尚待检查。本轮验收范围是独立图与源码保护，不宣称已完成新的全文 PDF 验收。

## 历史验收记录

此前“仅当前构成”版本及其 22 页四阶段编译结果已保存到 `history/current_only_20261013/`；其中的旧字体、页面、产物哈希及 PASS 只适用于该版，不能当作新版验收。它在本机的旧图备份保存在 `tmp/figure1_revision/restore_history/`。

本次替换前的竖排 I/S/B/T 版本及其正文备份保存在本机 `tmp/figure1_revision/horizontal_bar/`。

## 再生成及检查

安装 `requirements.txt` 中的依赖后，在仓库根目录执行：

```powershell
python tools/generate_reference_figures.py --figure1
python tools/verify_figure1_revision.py --figure-only
```

第二条命令依赖本机保存的 `tmp/figure1_revision/baseline.json` 和新运行的图形碰撞结果，不重新编译。完整编译后可省略 `--figure-only` 检查实际嵌入图中是否同时包含历史链与当前数据，避免误将旧 PDF 当作新版。

重新导出后应重跑 nature-figure 的 PDF 字号/碰撞检查；需要其单绘图区记录时，通过生成脚本的 `--qa-scripts` 指定该技能 scripts 目录。历史数据源及当前引用集合均继续保留。
