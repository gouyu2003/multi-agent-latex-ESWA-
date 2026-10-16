# 图 1：当前文献池与引用来源分类

更新日期：2026-10-13。正式图仅展示能从当前逐条记录复算的统计：85 条文献池、78 篇实际引用来源、7 条未引用记录，以及引用来源的 I/S/B/T = 13/15/42/8。

横向色条沿用青绿、蓝、灰、橙四色、白字和细白分隔线，宽度按 13:15:42:8 绘制。分类由作者按正文标准编码；78 是全部引用来源数，核心研究为 I 类的 13 篇。7 条未引用记录不等于不存在或已排除的来源。

数据来自 references.bib、有效正文引用扫描和 literature_audit.csv；逐条记录及来源哈希见 ../figure1_source_data.csv 和 source_summary.json。

## 历史流程的移除依据

已删除历史流程、排除支路、虚线和 Later source audit，并同步图名、图注及正文引图说明。

- 最早 Git 版本 f84c78b 的文献库确有 84 条；逐条台账中 108 条原始记录包含 81 条非 X、27 条 X，另有 3 条定向新增。
- 4ff0569、98732a2 及三个 audit_work/before*.zip 备份均未提供 72 条保留、36 条排除阶段的逐条状态。
- 旧报告记录 108 − 36 + 3 = 75；历史绘图 CSV 另加 9 条资源得到 84，但未找到这 9 条完整的逐条变更证据。算术一致不能证明历史流程成立。
- 原 figure_source_data.csv、旧报告、台账均作为历史记录保留。当前图不再读取历史汇总 CSV，也不以 81/27 机械替换旧筛选节点。

## 当前导出与验收

- Python / Matplotlib；矢量 PDF 为 140 × 48 mm，Arial 字体嵌入；SVG 保留文字，PNG 为 400 dpi 预览。
- 文字与色条标签 7.1 pt，节点数量 7.8 pt；保留跨栏环境和 0.80 linewidth。缩短画布高度去掉留白，不放大字体。
- 独立图执行字体、严格碰撞、数据/保护检查。直接读取 PDF 四段矩形核对比例，并检查历史标签消失。
- 对齐检查为 NOT APPLICABLE（单绘图区）。源码预检的通用提示已复核：矢量 PDF 无需另供 TIFF；PNG 实际指定 400 dpi；尺寸表达式实际为 140 × 48 mm。
- 自动和人工视觉检查记录见 acceptance.json、font_audit.json、collision.json。

本轮不调用全文编译。用户在 VS Code 编译后仍需检查全文分页和相邻图表；本轮不宣称完成全文 PDF 验收。

## 旧版本

history/historical_bar_20261013/ 保存删除历史流程前的验收记录，旧 PASS 只代表当时的图形和计算检查，不代表筛选过程得到证实。该版图片和正文保存在本机 tmp/figure1_revision/remove_history/。

history/current_only_20261013/ 是更早竖排分类版本及其旧编译记录，不能用于当前图的全文验收。

## 再生成

安装 requirements.txt 依赖后运行：

```powershell
python tools/generate_reference_figures.py --figure1
# 重新执行 nature-figure 的 PDF 字体与碰撞检查后：
python tools/verify_figure1_revision.py --figure-only
```

验收依赖本机 tmp/figure1_revision/baseline.json 和最新碰撞报告，不重新编译。用户编译后可省略 --figure-only，检查嵌入图的当前标签存在且历史标签消失。
