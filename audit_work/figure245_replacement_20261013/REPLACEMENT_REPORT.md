# 图2、图4、图5 PDF替换记录

2026-10-13。按用户指定三个PDF只替换有效正文的三个includegraphics路径。正文、图注、宽度设置、隐藏历史章、书目与其他图稿保持不变。旧图文件保留，三个输入PDF未编辑。

| 图号 | 新PDF | 编译页 |
|---|---|---|
| 2 | output/figure2_editable/20261013-153831-codex-clipboard-1eb7c158-b30c-49e1-bfa6-5ae40fd6f410/final/Figure2_Evolution_of_QA_Paradigms.pdf | 3 |
| 4 | output/figure4_editable/20261013-161131-Figure4_architecture_selection/final/Figure4_architecture_selection_edited.pdf | 9 |
| 5 | output/figure5_editable/20261013-163435-Figure5_resource_map/final/Figure5_resource_map_edited.pdf | 13 |

重新运行两轮pdfLaTeX，使用阶段二已经核验且字节不变的78项Biber BBL；未修改bibliography，未触发Biber重跑要求。最终23页PDF已同步根目录manuscript.pdf，三个指定PDF均在编译输入记录中。

已查看三个输入PDF及嵌入后的第3、9、13页，未见新增裁切或重叠；未定义引用和交叉引用为0。既有maketitle及长期团队学习段的两处hbox提示仍在。

图4新PDF仍含此前三个语义问题：Medical/Legal直接导向Hybrid+HITL、难度波动/跨域直接导向Hybrid、Role play/Group chat直接导向Flat；本轮只替换用户指定版本，不更改图内内容或用图注掩盖，语义同步继续待处理。

执行前正文和PDF等备份以before_前缀保存；精确三行补丁见replacement.patch，来源哈希见sources.json，编译和检查记录见compiled_review.json。阶段二恢复报告及其交付PDF保留为历史快照，不覆盖。未提交、推送或合并。

最终PDF SHA256：d66455301e6db47badd9ca1c237570a5e2a51d12916be1887e9f780e452262c4