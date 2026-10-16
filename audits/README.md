# 审计材料索引

- `references/apa7/`：原 APA7 审计目录。
- `references/audit_work/`：通用文献审计台账、字段记录和编译检查。
- `references/stage2_sources/`：第二阶段核查保存的来源证据。
- `references/baselines/`：原临时目录中的文献核查基线。
- `figures/figure1/`：图 1 检查；`baseline/` 保留历史对比文件。
- `figures/figure2/`、`figure4/`、`figure5/`：对应图的编辑工程与验收材料。
- `revisions/`：导师基线恢复、表 2 修订、原稿备份与前后对比。
- `organization/20261016/`：目录整理路径、原文件 SHA-256 和本次验收。

历史文件保留原始字节，不改写路径、日期或验收结论；这些结论只适用于当时状态。
本次整理的验收见 `organization/20261016/acceptance.json`。
旧路径对应的当前文件见 `organization/20261016/path_mapping.json`，
也可用 `tools/project_paths.py` 中的 `project_path()` 解析。
历史 ZIP 内部目录保持原样。
