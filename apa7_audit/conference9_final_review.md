# ESWA 九篇会议文献最终核查与 APA 7 验收报告

核查日期：2026-10-12。目标分支：`codex/eswa-apa7-migration`；基线提交：`6679e5ab3008799af3df0e397bb78329c16545b6`。开始时工作区干净，没有需暂存或覆盖的本地改动。核查阶段未创建 Git 提交或推送；完成后用户另行授权将本轮改动提交并推送当前分支，不合并 main。

**格式和范围回归已通过；编辑者缺证的会议文献由 9 篇降为 8 篇，不能宣称全部出版元数据严格验收已闭环。** Generative Agents 的编辑者和 Article 2 已有证据，AutoGen 正式署名已修正，其他缺字段仍按证据保留 PENDING。

## 1. 证据与判断边界

用户本消息实际提供 8 篇不同论文的官方文章级 BibTeX：MMLU 重复一次，Decomposed Prompting 未出现。清理 Markdown 链接、HTML 空白实体、复制产生的反斜线后，仅保存相关字段，见 `conference9_sources/user_supplied_bibtex_fields.json`；没有覆盖原库。Decomposed Prompting 另查作者官方 [DecomP-ODQA 仓库的 Citation](https://github.com/HarshTrivedi/DecomP-ODQA)，核对题名、7 人顺序、2023 和正式会名。

DOI 三篇逐条请求出版商登记的 Crossref，确认题名、作者顺序、年份、会议和页码；另外获取 UIST/ICAIF 整卷 DOI 登记、UIST 30 页前置材料、ICLR 2021/2023 出版目录和 COLM 官方录用名单。原始响应、访问失败、SHA-256 见 `conference9_sources/retrieval_manifest.json`。ACM 直连 403、OpenReview API 403／BibTeX 端点 404 均明确保留；没有把这些失败当无编辑者证据。

UIST 编辑者使用同卷 ACM 官方网页可检索的 Published In 栏，它明确使用 Editors 标签，卷 DOI `10.1145/3586183`、ISBN `9798400701320` 与该文一致。前置材料中的 General/Program/Proceedings Chairs 仅作核对，不直接转换成 editor。网页缓存观察单独记录于 `uist_acm_editor_observation.json`，区别于本机下载成功的完整响应。

按 [APA 官方会议录规则](https://apastyle.apa.org/style-grammar-guidelines/references/examples/conference-proceeding-references)，保留会议录章节形态，不改成演讲、网页或预印本。按 [APA 出版社规则](https://apastyle.apa.org/blog/publisher-locations-in-book-references)，ACM 两篇使用出版记录给出的 Association for Computing Machinery；不添加 New York 或会议举办地。出版社全称是该出版记录与 APA source 规则共同支持的选择，不声称所有简称一律禁止。

文章级 BibTeX、整卷登记或目录不含 editor，均不能证明整卷没有编辑者。本轮没有找到足以确证另外 8 篇无编辑者的资料，因此全部保留空值及 PENDING。六篇 OpenReview 会议文献也没有取得可信的会议录连续页码，不能由论文长度补填。ICLR 的晚出 POD/USB 目录没有作为新版本或新页码来源，保持原正式 OpenReview 版本。

补充访问边界：本机下载的两份 APA 页面虽然 HTTP 200，正文实际为 Incapsula 验证页，已在 retrieval_manifest 标记不可作为出版证据。格式指导另经网页检索读取，不能把这两个缓存文件当作完整 APA 指南。

## 2. 九篇逐项结果

|引用键|已确认／修正|最终 editor / publisher / locator|仍待核实|主要证据|
|---|---|---|---|---|
|fatemi2024financialqa|2 人署名、2024、题名、会名、530–537、DOI 一致；ACM → 全称|editor空 / Association for Computing Machinery / 530--537|editor|[正式记录](https://doi.org/10.1145/3677052.3698686)|
|hendrycks2021mmlu|7 人、2021、题名、URL 一致；会名和原适配保持|editor空 / International Conference on Learning Representations / 空；PENDING|editor；pages|[正式记录](https://openreview.net/forum?id=d7KBjmI3GmQ)|
|khot2023decomposed_prompting|作者官方仓库补证；7 人、2023、题名、URL 一致；正式 ICLR 2023 会名|editor空 / International Conference on Learning Representations / 空；PENDING|editor；pages|[正式记录](https://github.com/HarshTrivedi/DecomP-ODQA)|
|park2023generative_agents|6 人、2023、题名、DOI 一致；补 4 位编辑者、Article 2、总页数22；ACM → 全称|已补4人 / Association for Computing Machinery / Article 2（pagetotal=22，内部1–22不打印）|无本轮新增元数据缺项|[正式记录](https://doi.org/10.1145/3586183.3606763)|
|wang2023self_consistency|8 人顺序不变；Le, Q. → Q. V.；Chi, E. → E. H.；正式会名|editor空 / International Conference on Learning Representations / 空；PENDING|editor；pages|[正式记录](https://openreview.net/forum?id=1PL1NIMMrw)|
|wu2024autogen|正式 COLM 2024 的14人及顺序确认；Awadallah, A. → A. H.|editor空 / publisher空；PENDING / 空；PENDING|editor；publisher；pages|[正式记录](https://colmweb.org/2024/AcceptedPapers.html)|
|tang2025llmmedqa|9 人及顺序、2025、题名、IJCNN、IEEE、1–8、DOI 一致；保留既有正确适配|editor空 / IEEE / 1--8|editor|[正式记录](https://ieeexplore.ieee.org/document/11228647)|
|yao2023react|7 人顺序不变；Narasimhan, K. → K. R.；正式会名|editor空 / International Conference on Learning Representations / 空；PENDING|editor；pages|[正式记录](https://openreview.net/forum?id=WE_vluYUL-X)|
|zhou2023least_to_most|11 人顺序不变；Schärli 转正常姓名编码；Le, Q. V.、Chi, E. H.；正式会名|editor空 / International Conference on Learning Representations / 空；PENDING|editor；pages|[正式记录](https://openreview.net/forum?id=WZH7099tgfM)|

所有已有 DOI/URL 保持一致；无 DOI 的 OpenReview 文献保持无 DOI。出版社不得根据平台、赞助商或主办人猜填。Financial QA 的 530–537 和 LLM-MedQA 的 1–8 是官方登记／用户正式 BibTeX 提供的范围，非按实际 PDF 页数构造。

## 3. Generative Agents 的文章编号、编辑者和实现

[ACM 正式文章页](https://doi.org/10.1145/3586183.3606763) 同时显示 Article No. 2 与 Pages 1–22；用户导出为 articleno=2、numpages=22。Crossref 仅登记 page=1–22 而未带 Article 编号，故不能只依其 pages 字段作为最终定位方式。APA 官方在[有文章编号的期刊条目](https://apastyle.apa.org/style-grammar-guidelines/references/elements-list-entry)中以 Article 取代页码；将这个定位原则应用于 ACM 文章编号会议录是本项目有明确记录的适配判断，APA 的会议录示例页没有直接给出同款 ACM 示例。

实现：独立 overlay 设置 `eid=2`、`pages=null`、`pagetotal=22`；原始 `pages=1--22` 不动，并在九篇台账保留 internal_pages=1--22 和官方 articleno/numpages。使用 eid 是 biblatex 标准字段，articleno 是 ACM 导出字段，numpages 是篇幅字段；二者都不能混成起始页。

当前 biblatex-apa 9.20 的 inbook driver 不打印 eid，所以项目配置仅修补 booktitle 后的定位宏：有 eid 输出 Article 2，否则保持原有 pp. 页码逻辑。安装的 APA 样式和 CAS 文件均未修改；宏补丁失配会报错，不静默丢失编号。最终 PDF 明确显示 `(Article 2)`，不显示 pp. 1–22。

4 位 editor 依同卷 [ACM 明确的编辑者标签](https://doi.org/10.1145/3586183.3606810)补入 Sean Follmer、Jeff Han、Jürgen Steimle、Nathalie Henry Riche。复核出版商姓名拆分时，Crossref 对 Nathalie Henry Riche 有 Riche / Henry Riche 两种历史形式（证据另存 `henry_riche_name_crossref.json`）；本次采用 Riche, Nathalie Henry，输出 N. H. Riche，完整署名未少词。该拆分选择透明保留，不以程序委员会身份推断编辑者。

## 4. AutoGen 及 ICLR 的处理

用户正式 OpenReview BibTeX 与 [COLM 2024 官方录用名单](https://colmweb.org/2024/AcceptedPapers.html)均列 Ahmed Hassan Awadallah。overlay 使用 `Awadallah, Ahmed Hassan`，最终 PDF 为 `Awadallah, A. H.`；仍为正式 2024 版全部 14 位作者，不混用 2023 预印本名单。COLM 官网组织信息只能确认会议，不足以确定出版社或 editor，相关字段保持 PENDING。

仅四篇 ICLR 2023（Decomposed Prompting、Self-Consistency、ReAct、Least-to-Most）补正式会名 `The Eleventh International Conference on Learning Representations`。保留会议专名，APA sentence case 生成 `The eleventh International Conference on Learning Representations`；2021 MMLU 和其他年份/文献未修改。同 [ICLR 2023 出版目录](https://www.proceedings.com/80586.html)相符；该目录明确区分原出版者 ICLR 与晚出的 POD 版本，未把 Curran 机械当成原文出版社。

## 5. 官方 BibTeX 与原值差异

|引用键|字段|本轮前有效值|最终有效值|依据|
|---|---|---|---|---|
|fatemi2024financialqa|publisher|ACM|Association for Computing Machinery|[证据](https://apastyle.apa.org/blog/publisher-locations-in-book-references)|
|park2023generative_agents|publisher|ACM|Association for Computing Machinery|[证据](https://apastyle.apa.org/blog/publisher-locations-in-book-references)|
|park2023generative_agents|editor|None|Follmer, Sean and Han, Jeff and Steimle, Jürgen and Riche, Nathalie Henry|[证据](https://doi.org/10.1145/3586183.3606810)|
|park2023generative_agents|eid|None|2|[证据](https://doi.org/10.1145/3586183.3606763)|
|park2023generative_agents|pages|1--22|None|[证据](https://doi.org/10.1145/3586183.3606763)|
|park2023generative_agents|pagetotal|None|22|[证据](https://doi.org/10.1145/3586183.3606763)|
|wang2023self_consistency|author|Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny|Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc V and Chi, Ed H. and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny|[证据](https://openreview.net/forum?id=1PL1NIMMrw)|
|yao2023react|author|Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan|Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik R and Cao, Yuan|[证据](https://openreview.net/forum?id=WE_vluYUL-X)|
|zhou2023least_to_most|author|Zhou, Denny and Sch{\"a}rli, Nathanael and Hou, Le and Wei, Jason and Scales, Nathan and Wang, Xuezhi and Schuurmans, Dale and Cui, Claire and Bousquet, Olivier and Le, Quoc and Chi, Ed|Zhou, Denny and Schärli, Nathanael and Hou, Le and Wei, Jason and Scales, Nathan and Wang, Xuezhi and Schuurmans, Dale and Cui, Claire and Bousquet, Olivier and Le, Quoc V and Chi, Ed H.|[证据](https://openreview.net/forum?id=WZH7099tgfM)|
|wu2024autogen|author|Wu, Qingyun and Bansal, Gagan and Zhang, Jieyu and Wu, Yiran and Li, Beibin and Zhu, Erkang and Jiang, Li and Zhang, Xiaoyun and Zhang, Shaokun and Liu, Jiale and Awadallah, Ahmed and White, Ryen W. and Burger, Doug and Wang, Chi|Wu, Qingyun and Bansal, Gagan and Zhang, Jieyu and Wu, Yiran and Li, Beibin and Zhu, Erkang and Jiang, Li and Zhang, Xiaoyun and Zhang, Shaokun and Liu, Jiale and Awadallah, Ahmed Hassan and White, Ryen W. and Burger, Doug and Wang, Chi|[证据](https://openreview.net/forum?id=BAakY1hNKS)|
|wang2023self_consistency|booktitle|{International Conference on Learning Representations}|The Eleventh {International Conference on Learning Representations}|[证据](https://openreview.net/forum?id=1PL1NIMMrw)|
|yao2023react|booktitle|{International Conference on Learning Representations}|The Eleventh {International Conference on Learning Representations}|[证据](https://openreview.net/forum?id=WE_vluYUL-X)|
|zhou2023least_to_most|booktitle|{International Conference on Learning Representations}|The Eleventh {International Conference on Learning Representations}|[证据](https://openreview.net/forum?id=WZH7099tgfM)|
|khot2023decomposed_prompting|booktitle|{International Conference on Learning Representations}|The Eleventh {International Conference on Learning Representations}|[证据](https://github.com/HarshTrivedi/DecomP-ODQA)|

共14项字段适配，所有字段修正仅在项目 overlay 与自动生成的 sourcemap。`references.bib` SHA-256 始终为 `ef7c289c90c183c5f72f5484ee31b64d675a0f7a8dbfc325803d1bdc1d7b9a59`。所有现有引用键、原字段、旧 pending 和被替代的差异记录保留于 verification_history、metadata_changes.history 及 history/conference9_baseline_20261012。

## 6. 修改前后实际 APA 7 输出

“前”来自本机独立重建的改动前 APA 分支 PDF，而非旧根目录生成物或预测字符串；“后”来自本次正式 PDF。文本抽取保留链接断行空白，实际可点击 URI 和字形另由78条输出检查与原尺寸页面验证。题名内排版断字可能导致抽取连接差异，应以 PDF 字形和原题名对照。

### fatemi2024financialqa

**修改前：** Fatemi, S., & Hu, Y. (2024). Enhancing financial question answering with a multi-agent reflection framework. In Proceedings of the 5th ACM international conference on AI in finance (pp. 530–537). ACM. https://doi.org/10.1145/3677052.3698686

**修改后：** Fatemi, S., & Hu, Y. (2024). Enhancing financial question answering with a multi-agent reflection framework. In Proceedings of the 5th ACM international conference on AI in finance (pp. 530–537). Association for Computing Machinery. https://doi.org/10.1145/ 3677052.3698686

格式输出：PASS；元数据：PENDING；正式 PDF 第 19 页。

### hendrycks2021mmlu

**修改前：** Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J. (2021). Measuring massive multitask language understanding. In International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/forum?id=d7KBjmI3GmQ

**修改后：** Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J. (2021). Measuring massive multitask language understanding. In International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/forum?id=d7KBjmI3GmQ

格式输出：PASS；元数据：PENDING；正式 PDF 第 19 页。

### khot2023decomposed_prompting

**修改前：** Khot, T., Trivedi, H., Finlayson, M., Fu, Y., Richardson, K., Clark, P., & Sabharwal, A. (2023). Decomposed prompting: A modular approach for solving complex tasks. In International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/forum?id= _nGgzQjzaRy

**修改后：** Khot, T., Trivedi, H., Finlayson, M., Fu, Y., Richardson, K., Clark, P., & Sabharwal, A. (2023). Decomposed prompting: A modular approach for solving complex tasks. In The eleventh International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/ forum?id=_nGgzQjzaRy

格式输出：PASS；元数据：PENDING；正式 PDF 第 20 页。

### park2023generative_agents

**修改前：** Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th annual ACM symposium on user interface software and technology (pp. 1–22). ACM. https://doi.org/10.1145/3586183.3606763

**修改后：** Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In S. Follmer, J. Han, J. Steimle, & N. H. Riche (Eds.), Proceedings of the 36th annual ACM symposium on user interface software and technology (Article 2). Association for Computing Machinery. https : / / doi . org / 10 . 1145 / 3586183 . 3606763

格式输出：PASS；元数据：CHECKED_WITH_RECORDED_LIMITS；正式 PDF 第 21 页。

### wang2023self_consistency

**修改前：** Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., & Zhou, D. (2023). Self-consistency improves chain of thought reasoning in language models. In International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/forum?id= 1PL1NIMMrw

**修改后：** Wang, X., Wei, J., Schuurmans, D., Le, Q. V., Chi, E. H., Narang, S., Chowdhery, A., & Zhou, D. (2023). Self-consistency improves chain of thought reasoning in language models. In The eleventh International Conference on Learning Representations. International Conference on Learning Representations. https : / / openreview.net/forum?id=1PL1NIMMrw

格式输出：PASS；元数据：PENDING；正式 PDF 第 21 页。

### wu2024autogen

**修改前：** Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A., White, R. W., Burger, D., & Wang, C. (2024). AutoGen: Enabling next-gen LLM applications via multi-agent conversations. In First conference on language modeling. https://openreview.net/forum?id=BAakY1hNKS

**修改后：** Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2024). AutoGen: Enabling next-gen LLM applications via multi-agent conversations. In First conference on language modeling. https://openreview.net/forum?id=BAakY1hNKS

格式输出：PASS；元数据：PENDING；正式 PDF 第 21 页。

### tang2025llmmedqa

**修改前：** Yang, H., Chen, H., Guo, H., Chen, Y., Lin, C.-S., Hu, S., Hu, J., Wu, X., & Wang, X. (2025). LLM-MedQA: Enhancing medical question answering through case studies in large language models. In 2025 international joint conference on neural networks (IJCNN) (pp. 1–8). IEEE. https://doi.org/10.1109/IJCNN64981.2025. 11228647

**修改后：** Yang, H., Chen, H., Guo, H., Chen, Y., Lin, C.-S., Hu, S., Hu, J., Wu, X., & Wang, X. (2025). LLM-MedQA: Enhancing medical question answering through case studies in large language models. In 2025 international joint conference on neural networks (IJCNN) (pp. 1–8). IEEE. https://doi.org/10.1109/IJCNN64981.2025. 11228647

格式输出：PASS；元数据：PENDING；正式 PDF 第 22 页。

### yao2023react

**修改前：** Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. In International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/forum?id=WE_vluYUL-X

**修改后：** Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. R., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. In The eleventh International Conference on Learning Representations. International Conference on Learning Representations. https : / / openreview. net / forum ? id = WE _ vluYUL-X

格式输出：PASS；元数据：PENDING；正式 PDF 第 22 页。

### zhou2023least_to_most

**修改前：** Zhou, D., Schärli, N., Hou, L., Wei, J., Scales, N., Wang, X., Schuurmans, D., Cui, C., Bousquet, O., Le, Q., & Chi, E. (2023). Least-to-most prompting enables complex reasoning in large language models. In International Conference on Learning Representations. International Conference on Learning Representations. https: //openreview.net/forum?id=WZH7099tgfM

**修改后：** Zhou, D., Schärli, N., Hou, L., Wei, J., Scales, N., Wang, X., Schuurmans, D., Cui, C., Bousquet, O., Le, Q. V., & Chi, E. H. (2023). Least-tomost prompting enables complex reasoning in large language models. In The eleventh International Conference on Learning Representations. International Conference on Learning Representations. https://openreview.net/forum?id=WZH7099tgfM

格式输出：PASS；元数据：PENDING；正式 PDF 第 22 页。

## 7. 回归、完整性、编译和版面

|验收|本轮实际结果|
|---|---|
|APA 核心|14/14 PASS|
|APA 扩展|15/15 PASS|
|引用扫描器补丁回归|3/3 PASS；保留真实正文引用，拒绝补丁内隐藏引用或输入|
|九篇专项 PDF 检查|9/9 PASS；只代表列明的输出，不把缺证升级为已核实|
|正式78条逐项输出|78/78 PASS|
|85条独立预览|85/85 PASS|
|文献池／正文来源／命令|85／78／136；集合、键、全部命令逐项一致|
|原研究内容、图表、CAS|字节／哈希保护全部通过；其余76条 overlay 逐记录一致|
|完整构建|pdfLaTeX → Biber → pdfLaTeX → pdfLaTeX，全部成功|
|双栏和页数|22→22；第1–18页文本与72dpi像素逐页完全一致；全部图像与位置完全一致|
|视觉检查|22页联系表检查，参考文献19–22页另看完整分辨率，未引入裁切、重叠、缩进或跨栏问题|
|冻结BBL重建|本机三次pdfLaTeX、不跑Biber；22页文本与像素全部一致；不代表投稿服务器兼容|
|Overfull|3→3；三条既有值完全一致|
|Underfull|69→69；未增加|
|最终编译／Biber 警告和错误|0／0；无未定义引用或需重跑提示|

已有 Overfull 为123.62721pt（CAS前置宏内部）、0.76843pt、0.5575pt；它们与改动前完全一致，页面无越界，不为了清警告改研究内容或布局。细节见 warning_comparison.json、conference9_pdf_comparison.json、scope_validation.json、final_checks.json、conference9_acceptance.json。

当前正式 PDF SHA-256：`4c57b1d85fd178fa9a5b7c72a1c565be21baf45590e6a657f9da9ea8b136847d`；BBL SHA-256：`c0b086e805ea79b007c3ee9fd71ad756456e9c5ed63389a8e07aaff46a16c8e4`。构建产物与日志在根目录和 tmp/apa7_build；前版在 tmp/conference9_before_build。

本机复现时，将 PyMuPDF 放入 Python 环境后，执行 `python -B tools/generate_apa_sourcemap.py`、`powershell -File build.ps1`、`python -B tools/run_apa_tests.py`、`python -B tools/audit_apa_output.py --skip-scope`、`python -B tools/audit_apa_output.py --pool85`。本轮运行环境用仓库 tmp/apa7_vendor 的 PyMuPDF，不修改全局 Python。修正了原测试/冻结脚本写死的 D 盘 TeX 路径，并修正 PowerShell 的 Biber 日志重定向；默认从 PATH 找本机引擎。引用扫描器仅增加对5参数 bibmacro补丁的跳过，仍拒绝隐藏引用/输入。

## 8. PENDING 的关闭与保留

关闭：Generative Agents 的 editor 缺项（同卷出版社明确标注四位编辑者）；其出版定位采用 Article 2，有证据的出版社全称、作者中间名与四篇正式会名修正完成。

保留：Financial QA、MMLU、Decomposed Prompting、Self-Consistency、AutoGen、LLM-MedQA、ReAct、Least-to-Most 的 editor（8篇）；MMLU／四篇ICLR2023／AutoGen 的会议录分页（6篇）；AutoGen 出版社（1篇）。8篇不能因用户官方文章级 BibTeX 没有这些字段而强行关闭。后续需要原整卷出版署名页或明确编辑／无编辑声明；如有分页需有同版本正式记录。

既有 Attention 页码、未引用 GenMentor/XAgent 等限制仍留在原台账；不扩本轮范围。原研究声明、图中的历史快照、内容与引用支持关系未作新核查，不能把本轮格式/出版字段检查理解为全部研究论证再次验证。导师的真实性和格式验收可使用这份当前证据进入审核，但“全部元数据无待核实项”仍不满足。
