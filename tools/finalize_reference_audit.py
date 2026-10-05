from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from build_reference_inventory import citation_contexts, parse_fields


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "audit_work"


CORE = {
    "du2024multiagent_debate",
    "qian2024scaling_multiagent",
    "liang2024divergent_debate",
    "xiong2023inter_consistency",
    "zhao2024longagent",
    "kim2024mdagents",
    "tang2024medagents",
    "tang2025llmmedqa",
    "legalgraphrag2026",
    "hu2024triad",
    "fatemi2024financialqa",
    "chen2024reconcile",
    "zhang2024chain_agents",
    "jiang2026cocoa",
}

TECHNICAL = {
    "anthropic2024mcp", "google2025a2a", "langgraph2024", "crewai2023",
    "dify2024", "xagent2023",
}

SUPPORTING = {
    "wu2024autogen", "hong2024metagpt", "park2023generative_agents",
    "li2023camel", "qian2023chatdev", "shen2024hugginggpt",
    "duan2024langgraph_crewai", "zhuge2024gptswarm", "chen2024agentverse",
    "li2024genmentor", "yang2024swe_agent", "han2024mast",
    "huang2023agentcoder", "zhang2024eduplanner",
}

MANUAL = {
    "brown2020gpt3": ("verified", "verified", "https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html", "Manual check resolved a same-title false match."),
    "openai2023gpt4": ("verified", "corrected", "https://arxiv.org/abs/2303.08774", "Author attribution corrected to the official OpenAI group author; title and arXiv identifier verified against the official preprint."),
    "minsky1988society": ("verified", "verified", "https://www.simonandschuster.com/books/Society-Of-Mind/Marvin-Minsky/9780671657130", "The cited 1986 first-edition year is retained; the linked publisher page describes a later edition."),
    "wu2024autogen": ("verified", "corrected", "https://openreview.net/forum?id=BAakY1hNKS", "Title and full author list aligned with the COLM 2024 record."),
    "hong2024metagpt": ("verified", "corrected", "https://proceedings.iclr.cc/paper_files/paper/2024/hash/6507b115562bb0a305f1958ccc87355a-Abstract-Conference.html", "Final ICLR 2024 version retained instead of the 2023 preprint year."),
    "du2024multiagent_debate": ("verified", "corrected", "https://proceedings.mlr.press/v235/du24e.html", "Final ICML 2024 volume and pages added."),
    "vaswani2017attention": ("verified", "verified", "https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html", "Manual check resolved a same-title false match."),
    "devlin2019bert": ("verified", "corrected", "https://aclanthology.org/N19-1423/", "ACL Anthology DOI and official URL added."),
    "qian2024scaling_multiagent": ("verified", "corrected", "https://proceedings.iclr.cc/paper_files/paper/2025/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html", "Final ICLR 2025 publication retained; preprint first appeared in 2024."),
    "khattab2024dspy": ("verified", "corrected", "https://mlanthology.org/iclr/2024/khattab2024iclr-dspy/", "Title and full author list aligned with the ICLR 2024 record."),
    "chen2024agentverse": ("verified", "corrected", "https://proceedings.iclr.cc/paper_files/paper/2024/hash/578e65cdee35d00c708d4c64bce32971-Abstract-Conference.html", "Final ICLR 2024 publication retained; preprint first appeared in 2023."),
    "asai2024selfrag": ("verified", "verified", "https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html", "Manual title and author verification against ICLR 2024."),
    "li2024genmentor": ("verified", "corrected", "https://doi.org/10.1145/3701716.3715244", "Final WWW 2025 Companion Proceedings metadata and DOI verified; the citation key is retained for compatibility."),
    "brynjolfsson2023generative_ai_work": ("verified", "corrected", "https://doi.org/10.1093/qje/qjae044", "Final QJE 2025 article retained instead of the 2023 NBER working paper."),
    "jimenez2024swe_bench": ("verified", "corrected", "https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html", "Spurious title match rejected; official ICLR 2024 record used."),
    "han2024mast": ("verified", "corrected", "https://proceedings.neurips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html", "Final NeurIPS 2025 dataset-and-benchmarks paper used; citation key retained for compatibility."),
    "liu2024agentbench": ("verified", "corrected", "https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html", "Final ICLR 2024 publication verified."),
    "legalgraphrag2026": ("verified", "corrected", "https://aclanthology.org/2026.acl-long.1738/", "Final ACL 2026 proceedings metadata supersedes the preprint/working-paper record."),
    "zhang2024eduplanner": ("verified", "corrected", "https://doi.org/10.1109/TLT.2025.3561332", "Final IEEE TLT 2025 volume and pages used; the citation key is retained for compatibility."),
    "mialon2024gaia": ("verified", "duplicate", "https://arxiv.org/abs/2311.12983", "Duplicate of mialon2023gaia; removed from the active bibliography."),
    "chen2025llm_mas_survey": ("verified", "corrected", "https://arxiv.org/abs/2412.17481", "Preprint year is 2024 and first author is Shuaihang Chen."),
    "patil2023gorilla": ("verified", "corrected", "https://proceedings.neurips.cc/paper_files/paper/2024/hash/e4a5ae3e2e1212f36e32f1d5b43e1b4a-Abstract-Datasets_and_Benchmarks_Track.html", "Final NeurIPS publication year is 2024."),
    "chen2024universal_self_consistency": ("verified", "corrected", "https://arxiv.org/abs/2311.17311", "Preprint first appeared in 2023."),
    "lin2025creativity_mas": ("verified", "corrected", "https://aclanthology.org/2025.emnlp-main.1403/", "First author corrected from Junyou Lin to Yi-Cheng Lin."),
    "fan2025foundation_agents": ("verified", "corrected", "https://arxiv.org/abs/2504.01990", "Local title and author were incomplete; official preprint record identified."),
    "li2024trustworthy_medical_qa": ("not_found", "unverifiable", "", "No authoritative record matched the exact local title and author; excluded."),
    "zhuang2024atm": ("verified", "corrected", "https://aclanthology.org/2024.emnlp-main.610/", "Title and first author corrected to the EMNLP 2024 paper by Junda Zhu et al."),
    "zhu2023efficient_odqa_survey": ("verified", "corrected", "https://aclanthology.org/2023.acl-long.808/", "First author corrected from Yutao Zhu to Qin Zhang."),
    "ho2024multihop_qa_survey": ("verified", "corrected", "https://doi.org/10.1561/9781638283751", "First author corrected from Xanh Ho to Vaibhav Mavi."),
    "qin2024multiagent_survey_cn": ("not_found", "unverifiable", "", "Local Chinese title, author, and venue are corrupted by mojibake; excluded."),
    "ruanjianbao2024code_gen_survey": ("not_found", "unverifiable", "", "Local Chinese title and author are corrupted and no exact source can be established; excluded."),
    "zeng2023glm130b": ("verified", "corrected", "https://openreview.net/forum?id=-Aw0rrrPUF", "Final ICLR 2023 publication retained; preprint first appeared in 2022."),
    "zhao2023llm_survey_cn": ("not_found", "unverifiable", "", "Local Chinese title and author are corrupted by mojibake; excluded."),
    "liu2024se_agents_survey": ("verified", "corrected", "https://doi.org/10.1145/3796507", "Final ACM TOSEM record is 2026 and first author is Junwei Liu."),
    "hendrycks2021mmlu": ("verified", "corrected", "https://openreview.net/forum?id=d7KBjmI3GmQ", "Final ICLR 2021 publication year used instead of the 2020 preprint year."),
    "zhou2024webarena": ("verified", "verified", "https://proceedings.iclr.cc/paper_files/paper/2024/hash/2e64e47c57ecc2e4a7261da0f12fb8e3-Abstract-Conference.html", "Manual title and author verification against ICLR 2024."),
    "glm2024chatglm": ("verified", "corrected", "https://arxiv.org/abs/2406.12793", "Author attribution normalised to the official GLM Team group author; title and arXiv identifier verified against the official preprint."),
}

FIELD_OVERRIDES = {
    "brown2020gpt3": {"author": "Brown, Tom and Mann, Benjamin and Ryder, Nick and Subbiah, Melanie and Kaplan, Jared D. and Dhariwal, Prafulla and Neelakantan, Arvind and Shyam, Pranav and Sastry, Girish and Askell, Amanda and Agarwal, Sandhini and Herbert-Voss, Ariel and Krueger, Gretchen and Henighan, Tom and Child, Rewon and Ramesh, Aditya and Ziegler, Daniel and Wu, Jeffrey and Winter, Clemens and Hesse, Chris and Chen, Mark and Sigler, Eric and Litwin, Mateusz and Gray, Scott and Chess, Benjamin and Clark, Jack and Berner, Christopher and McCandlish, Sam and Radford, Alec and Sutskever, Ilya and Amodei, Dario", "url": MANUAL["brown2020gpt3"][2]},
    "openai2023gpt4": {"title": "{GPT-4} Technical Report", "author": "{OpenAI}", "url": "https://arxiv.org/abs/2303.08774"},
    "minsky1988society": {"url": MANUAL["minsky1988society"][2]},
    "wooldridge1995intelligent": {"doi": "10.1017/S0269888900008122", "url": "https://doi.org/10.1017/S0269888900008122"},
    "wang2024survey_autonomous_agents": {
        "author": "Wang, Lei and Ma, Chen and Feng, Xueyang and Zhang, Zeyu and Yang, Hao and Zhang, Jingsen and Chen, Zhiyuan and Tang, Jiakai and Chen, Xu and Lin, Yankai and Zhao, Wayne Xin and Wei, Zhewei and Wen, Jirong",
        "doi": "10.1007/s11704-024-40231-1",
        "url": "https://doi.org/10.1007/s11704-024-40231-1",
    },
    "wu2024autogen": {
        "title": "{AutoGen}: Enabling Next-Gen {LLM} Applications via Multi-Agent Conversations",
        "author": "Wu, Qingyun and Bansal, Gagan and Zhang, Jieyu and Wu, Yiran and Li, Beibin and Zhu, Erkang and Jiang, Li and Zhang, Xiaoyun and Zhang, Shaokun and Liu, Jiale and Awadallah, Ahmed Hassan and White, Ryen W. and Burger, Doug and Wang, Chi",
        "booktitle": "First Conference on Language Modeling",
        "url": MANUAL["wu2024autogen"][2],
    },
    "hong2024metagpt": {"author": "Hong, Sirui and Zhuge, Mingchen and Chen, Jonathan and Zheng, Xiawu and Cheng, Yuheng and Wang, Jinlin and Zhang, Ceyao and Wang, Zili and Yau, Steven and Lin, Zijuan and Zhou, Liyang and Ran, Chenyu and Xiao, Lingfeng and Wu, Chenglin and Schmidhuber, J{\\\"u}rgen", "url": MANUAL["hong2024metagpt"][2], "volume": "", "pages": ""},
    "du2024multiagent_debate": {"booktitle": "Proceedings of the 41st International Conference on Machine Learning", "series": "Proceedings of Machine Learning Research", "volume": "235", "pages": "11733--11763", "publisher": "PMLR", "url": MANUAL["du2024multiagent_debate"][2]},
    "karpukhin2020dpr": {"doi": "10.18653/v1/2020.emnlp-main.550", "url": "https://aclanthology.org/2020.emnlp-main.550/"},
    "yang2018hotpotqa": {"doi": "10.18653/v1/D18-1259", "url": "https://aclanthology.org/D18-1259/"},
    "kwiatkowski2019natural_questions": {"author": "Kwiatkowski, Tom and Palomaki, Jennimaria and Redfield, Olivia and Collins, Michael and Parikh, Ankur and Alberti, Chris and Epstein, Danielle and Polosukhin, Illia and Devlin, Jacob and Lee, Kenton and Toutanova, Kristina and Jones, Llion and Kelcey, Matthew and Chang, Ming-Wei and Dai, Andrew M. and Uszkoreit, Jakob and Le, Quoc and Petrov, Slav", "doi": "10.1162/tacl_a_00276", "url": "https://doi.org/10.1162/tacl_a_00276"},
    "reddy2019coqa": {"doi": "10.1162/tacl_a_00266", "url": "https://doi.org/10.1162/tacl_a_00266"},
    "choi2018quac": {"doi": "10.18653/v1/D18-1241", "url": "https://aclanthology.org/D18-1241/"},
    "lewis2020rag": {"author": "Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and K{\\\"u}ttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rockt{\\\"a}schel, Tim and Riedel, Sebastian and Kiela, Douwe", "url": "https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html"},
    "yao2023react": {"year": "2023", "journal": "", "booktitle": "International Conference on Learning Representations", "url": "https://openreview.net/forum?id=WE_vluYUL-X"},
    "vaswani2017attention": {"url": MANUAL["vaswani2017attention"][2]},
    "devlin2019bert": {"doi": "10.18653/v1/N19-1423", "url": "https://aclanthology.org/N19-1423/"},
    "touvron2023llama": {"author": "Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\\'e}e and Rozi{\\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume", "url": "https://arxiv.org/abs/2302.13971"},
    "glm2024chatglm": {"title": "{ChatGLM}: A Family of Large Language Models from {GLM}-130B to {GLM}-4 All Tools", "author": "{GLM Team}", "url": "https://arxiv.org/abs/2406.12793"},
    "ouyang2022instructgpt": {"author": "Ouyang, Long and Wu, Jeffrey and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and Schulman, John and Hilton, Jacob and Kelton, Fraser and Miller, Luke and Simens, Maddie and Askell, Amanda and Welinder, Peter and Christiano, Paul and Leike, Jan and Lowe, Ryan", "url": "https://doi.org/10.52202/068431-2011"},
    "qian2024scaling_multiagent": {"author": "Qian, Chen and Xie, Zihao and Wang, Yifei and Liu, Wei and Zhu, Kunlun and Xia, Hanchen and Dang, Yufan and Du, Zhuoyun and Chen, Weize and Yang, Cheng and Liu, Zhiyuan and Sun, Maosong", "url": MANUAL["qian2024scaling_multiagent"][2], "volume": "", "pages": ""},
    "park2023generative_agents": {"doi": "10.1145/3586183.3606763", "url": "https://doi.org/10.1145/3586183.3606763"},
    "liang2024divergent_debate": {"doi": "10.18653/v1/2024.emnlp-main.992", "url": "https://aclanthology.org/2024.emnlp-main.992/"},
    "xiong2023inter_consistency": {"doi": "10.18653/v1/2023.findings-emnlp.508", "url": "https://aclanthology.org/2023.findings-emnlp.508/"},
    "qian2023chatdev": {"author": "Qian, Chen and Liu, Wei and Liu, Hongzhang and Chen, Nuo and Dang, Yufan and Li, Jiahao and Yang, Cheng and Chen, Weize and Su, Yusheng and Cong, Xin and Xu, Juyuan and Li, Dahai and Liu, Zhiyuan and Sun, Maosong", "doi": "10.18653/v1/2024.acl-long.810", "url": "https://aclanthology.org/2024.acl-long.810/"},
    "gao2024rag_survey": {"author": "Gao, Yunfan and Xiong, Yun and Gao, Xinyu and Jia, Kangxiang and Pan, Jinliu and Bi, Yuxi and Dai, Yi and Sun, Jiawei and Wang, Meng and Wang, Haofen", "url": "https://arxiv.org/abs/2312.10997"},
    "shen2024hugginggpt": {"url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/77c33e6a367922d003ff102ffb92b658-Abstract-Conference.html"},
    "zhao2024longagent": {"doi": "10.18653/v1/2024.emnlp-main.912", "url": "https://aclanthology.org/2024.emnlp-main.912/"},
    "khattab2024dspy": {"title": "{DSPy}: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines", "author": "Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and A, Sri Vardhamanan and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher", "url": MANUAL["khattab2024dspy"][2], "volume": "", "pages": ""},
    "duan2024langgraph_crewai": {"url": "https://arxiv.org/abs/2411.18241"},
    "zhuge2024gptswarm": {"url": "https://arxiv.org/abs/2402.16823"},
    "chen2024agentverse": {"author": "Chen, Weize and Su, Yusheng and Zuo, Jingwei and Yang, Cheng and Yuan, Chenfei and Chan, Chi-Min and Yu, Heyang and Lu, Yaxi and Hung, Yi-Hsin and Qian, Chen and Qin, Yujia and Cong, Xin and Xie, Ruobing and Liu, Zhiyuan and Sun, Maosong and Zhou, Jie", "url": MANUAL["chen2024agentverse"][2], "volume": "", "pages": ""},
    "kim2024mdagents": {"doi": "10.52202/079017-2522", "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/90d1fc07f46e31387978b88e7e057a31-Abstract-Conference.html"},
    "wang2023plan_and_solve": {"doi": "10.18653/v1/2023.acl-long.147", "url": "https://aclanthology.org/2023.acl-long.147/"},
    "packer2023memgpt": {"journal": "arXiv preprint arXiv:2310.08560", "url": "https://arxiv.org/abs/2310.08560"},
    "zhang2024memory_survey": {"doi": "10.1145/3748302", "url": "https://doi.org/10.1145/3748302"},
    "asai2024selfrag": {"url": MANUAL["asai2024selfrag"][2], "volume": "", "pages": ""},
    "jiang2023active_rag": {"doi": "10.18653/v1/2023.emnlp-main.495", "url": "https://aclanthology.org/2023.emnlp-main.495/"},
    "zhou2023least_to_most": {"author": "Zhou, Denny and Sch{\\\"a}rli, Nathanael and Hou, Le and Wei, Jason and Scales, Nathan and Wang, Xuezhi and Schuurmans, Dale and Cui, Claire and Bousquet, Olivier and Le, Quoc and Chi, Ed", "url": "https://arxiv.org/abs/2205.10625"},
    "wei2022chain_of_thought": {"author": "Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Ichter, Brian and Xia, Fei and Chi, Ed and Le, Quoc V. and Zhou, Denny", "url": "https://doi.org/10.52202/068431-1800"},
    "besta2024graph_of_thoughts": {"author": "Besta, Maciej and Blach, Nils and Kubicek, Ales and Gerstenberger, Robert and Podstawski, Michal and Gianinazzi, Lukas and Gajda, Joanna and Lehmann, Tomasz and Niewiadomski, Hubert and Nyczyk, Piotr and Hoefler, Torsten", "doi": "10.1609/aaai.v38i16.29720", "url": "https://doi.org/10.1609/aaai.v38i16.29720"},
    "madaan2023self_refine": {"author": "Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter", "url": "https://doi.org/10.52202/075280-2019"},
    "dhuliawala2023chain_of_verification": {"doi": "10.18653/v1/2024.findings-acl.212", "url": "https://aclanthology.org/2024.findings-acl.212/"},
    "tang2024medagents": {"doi": "10.18653/v1/2024.findings-acl.33", "url": "https://aclanthology.org/2024.findings-acl.33/"},
    "cui2023chatlaw": {"volume": "", "url": "https://arxiv.org/abs/2306.16092"},
    "li2024genmentor": {"doi": "10.1145/3701716.3715244", "url": "https://doi.org/10.1145/3701716.3715244"},
    "singhal2023medpalm": {"author": "Singhal, Karan and Azizi, Shekoofeh and Tu, Tao and Mahdavi, S. Sara and Wei, Jason and Chung, Hyung Won and Scales, Nathan and Tanwani, Ajay and Cole-Lewis, Heather and Pfohl, Stephen and Payne, Perry and Seneviratne, Martin and Gamble, Paul and Kelly, Chris and Babiker, Abubakr and Sch{\\\"a}rli, Nathanael and Chowdhery, Aakanksha and Mansfield, Philip and Demner-Fushman, Dina and Ag{\\\"u}era y Arcas, Blaise and Webster, Dale and Corrado, Greg S. and Matias, Yossi and Chou, Katherine and Gottweis, Juraj and Tomasev, Nenad and Liu, Yun and Rajkomar, Alvin and Barral, Joelle and Semturs, Christopher and Karthikesalingam, Alan and Natarajan, Vivek", "doi": "10.1038/s41586-023-06291-2", "url": "https://doi.org/10.1038/s41586-023-06291-2"},
    "guha2023legalbench": {"author": "Guha, Neel and Nyarko, Julian and Ho, Daniel and R{\\'e}, Christopher and Chilton, Adam and K, Aditya and Chohlas-Wood, Alex and Peters, Austin and Waldon, Brandon and Rockmore, Daniel and Zambrano, Diego and Talisman, Dmitry and Hoque, Enam and Surani, Faiz and Fagan, Frank and Sarfaty, Galit and Dickinson, Gregory and Porat, Haggai and Hegland, Jason and Wu, Jessica and Nudell, Joe and Niklaus, Joel and Nay, John and Choi, Jonathan and Tobia, Kevin and Hagan, Margaret and Ma, Megan and Livermore, Michael and Rasumov-Rahe, Nikon and Holzenberger, Nils and Kolt, Noam and Henderson, Peter and Rehaag, Sean and Goel, Sharad and Gao, Shang and Williams, Spencer and Gandhi, Sunny and Zur, Tom and Iyer, Varun and Li, Zehua", "url": "https://doi.org/10.52202/075280-1915"},
    "brynjolfsson2023generative_ai_work": {"doi": "10.1093/qje/qjae044", "url": MANUAL["brynjolfsson2023generative_ai_work"][2]},
    "yang2024swe_agent": {"url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c0c9adf4c162b5b1d5a51c-Abstract-Conference.html"},
    "jimenez2024swe_bench": {"url": MANUAL["jimenez2024swe_bench"][2], "volume": "", "pages": ""},
    "han2024mast": {"author": "Cemri, Mert and Pan, Melissa Z. and Yang, Shuyi and Agrawal, Lakshya A. and Chopra, Bhavya and Tiwari, Rishabh and Keutzer, Kurt and Parameswaran, Aditya and Klein, Dan and Ramchandran, Kannan and Zaharia, Matei A. and Gonzalez, Joseph E. and Stoica, Ion", "url": MANUAL["han2024mast"][2]},
    "tang2025llmmedqa": {"doi": "10.1109/IJCNN64981.2025.11228647", "url": "https://doi.org/10.1109/IJCNN64981.2025.11228647"},
    "legalgraphrag2026": {"doi": "10.18653/v1/2026.acl-long.1738", "url": "https://aclanthology.org/2026.acl-long.1738/", "publisher": "Association for Computational Linguistics"},
    "hu2024triad": {"doi": "10.18653/v1/2024.emnlp-main.101", "url": "https://aclanthology.org/2024.emnlp-main.101/"},
    "huang2023agentcoder": {"url": "https://arxiv.org/abs/2312.13010"},
    "zhang2024eduplanner": {"volume": "18", "pages": "416--427", "doi": "10.1109/TLT.2025.3561332", "url": "https://doi.org/10.1109/TLT.2025.3561332"},
    "fatemi2024financialqa": {"doi": "10.1145/3677052.3698686", "url": "https://doi.org/10.1145/3677052.3698686"},
    "peffers2007dsrm": {"doi": "10.2753/MIS0742-1222240302", "url": "https://doi.org/10.2753/MIS0742-1222240302"},
}

ADDITIONS = [
    {
        "entry_type": "inproceedings", "key": "chen2024reconcile",
        "title": "{ReConcile}: Round-Table Conference Improves Reasoning via Consensus among Diverse {LLM}s",
        "author": "Chen, Justin and Saha, Swarnadeep and Bansal, Mohit",
        "booktitle": "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
        "pages": "7066--7085", "year": "2024", "publisher": "Association for Computational Linguistics",
        "doi": "10.18653/v1/2024.acl-long.381", "url": "https://aclanthology.org/2024.acl-long.381/",
        "note": "Targeted update search; core included study.",
    },
    {
        "entry_type": "inproceedings", "key": "zhang2024chain_agents",
        "title": "Chain of Agents: Large Language Models Collaborating on Long-Context Tasks",
        "author": "Zhang, Yusen and Sun, Ruoxi and Chen, Yanfei and Pfister, Tomas and Zhang, Rui and Arik, Sercan O.",
        "booktitle": "Advances in Neural Information Processing Systems", "volume": "37", "year": "2024",
        "doi": "10.52202/079017-4202", "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/ee71a4b14ec26710b39ee6be113d7750-Abstract-Conference.html",
        "note": "Targeted update search; core included study.",
    },
    {
        "entry_type": "inproceedings", "key": "jiang2026cocoa",
        "title": "Collaborative Chain-of-Agents for Parametric-Retrieved Knowledge Synergy",
        "author": "Jiang, Yi and Zhao, Sendong and Li, Jianbo and Wang, Haochun and Zhang, Lizhe and Liu, Yan and Qin, Bing",
        "booktitle": "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
        "pages": "3663--3680", "year": "2026", "publisher": "Association for Computational Linguistics",
        "doi": "10.18653/v1/2026.acl-long.167", "url": "https://aclanthology.org/2026.acl-long.167/",
        "note": "Targeted update search; core included study.",
    },
]


def evidence_role(key: str, cited: bool) -> str:
    if key in CORE:
        return "I"
    if key in TECHNICAL:
        return "T"
    if key in SUPPORTING:
        return "S"
    if cited:
        return "B"
    return "X"


def render_bib(entry_type: str, key: str, fields: dict[str, str]) -> str:
    order = ["title", "author", "journal", "booktitle", "series", "volume", "number", "pages", "year", "publisher", "organization", "doi", "url", "howpublished", "note"]
    lines = [f"@{entry_type}{{{key},"]
    for name in order:
        value = fields.get(name, "").strip()
        if value:
            lines.append(f"  {name} = {{{value}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    inventory = json.loads((WORK / "reference_inventory.json").read_text(encoding="utf-8"))
    verification = {x["key"]: x for x in json.loads((WORK / "auto_verification.json").read_text(encoding="utf-8"))}
    current_contexts = citation_contexts()
    audit_rows = []
    retained = []

    for item in inventory:
        key = item["key"]
        cited = key in current_contexts
        role = evidence_role(key, cited)
        auto = verification[key]
        adopted_fields = parse_fields(item["raw"])
        adopted_fields.update(FIELD_OVERRIDES.get(key, {}))
        if key in MANUAL:
            existence, metadata, url, notes = MANUAL[key]
        else:
            existence = "verified" if auto["status"] in {"verified", "verified_preprint_id", "technical_source_url"} else "manual_needed"
            metadata = "verified" if existence == "verified" else "needs_follow_up"
            url = auto.get("official_url", "")
            notes = "; ".join(auto.get("notes", []))
        if existence == "verified" and re.search(r"\band\s+others\b", item["author"], flags=re.I):
            metadata = "corrected"
            expansion_note = "Truncated local author list expanded to the complete official author list."
            notes = f"{notes} {expansion_note}".strip()
        if cited and url and not adopted_fields.get("doi") and not adopted_fields.get("url"):
            adopted_fields["url"] = url
        # The delivery table reports the metadata adopted after verification.
        # Low-confidence API candidates remain in the cache but must not appear
        # as the authoritative match in the row-level audit.
        if existence == "verified":
            best = {
                "title": adopted_fields.get("title", item["title"]),
                "author": adopted_fields.get("author", item["author"]).split(" and ")[0],
                "year": adopted_fields.get("year", item["year"]),
            }
        else:
            best = {}
        consistency = "Yes"
        if metadata == "corrected":
            consistency = "Corrected"
        elif existence == "not_found":
            consistency = "Unverifiable"
        elif metadata == "duplicate":
            consistency = "Duplicate"
        audit_rows.append(
            {
                "sequence": item["sequence"], "key": key, "search_origin": "local_references_bib",
                "cited_in_manuscript": "yes" if cited else "no", "evidence_role": role,
                "existence_status": existence, "official_source": url,
                "authors_title_consistency": consistency, "metadata_status": metadata,
                "local_title": item["title"], "local_first_author": item["author"].split(" and ")[0],
                "local_year": item["year"], "matched_title": best.get("title", ""),
                "matched_first_author": best.get("author", ""), "matched_year": best.get("year", ""),
                "citation_count": len(current_contexts.get(key, [])), "notes": notes,
            }
        )
        if cited:
            retained.append((item["entry_type"], key, adopted_fields))

    for offset, addition in enumerate(ADDITIONS, start=1):
        fields = {k: v for k, v in addition.items() if k not in {"entry_type", "key"}}
        retained.append((addition["entry_type"], addition["key"], fields))
        audit_rows.append(
            {
                "sequence": len(inventory) + offset, "key": addition["key"], "search_origin": "targeted_update",
                "cited_in_manuscript": "yes", "evidence_role": "I", "existence_status": "verified",
                "official_source": addition["url"], "authors_title_consistency": "Yes",
                "metadata_status": "verified", "local_title": "", "local_first_author": "",
                "local_year": "", "matched_title": addition["title"],
                "matched_first_author": addition["author"].split(" and ")[0], "matched_year": addition["year"],
                "citation_count": len(current_contexts.get(addition["key"], [])),
                "notes": "Added after targeted gap search and verified against the official proceedings record.",
            }
        )

    fieldnames = list(audit_rows[0])
    with (ROOT / "literature_audit.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(audit_rows)

    search_rows = [
        {"date": "2026-08-02", "source": "Local BibTeX", "query": "All entries in references.bib", "purpose": "Reconstruct candidate corpus", "records_reviewed": 108, "records_added": 0},
        {"date": "2026-08-02", "source": "Crossref + OpenAlex + arXiv", "query": "Exact/near-exact title and first-author matching for every candidate", "purpose": "Existence and metadata verification", "records_reviewed": 108, "records_added": 0},
        {"date": "2026-08-02", "source": "ACL Anthology + OpenReview + publisher proceedings", "query": "multi-agent AND (question answering OR reasoning) AND (LLM OR large language model)", "purpose": "Targeted gap search: collaborative reasoning; top-ranked results inspected, no exhaustive hit count claimed", "records_reviewed": "not claimed", "records_added": 1},
        {"date": "2026-08-02", "source": "arXiv + NeurIPS proceedings", "query": "multi-agent AND long-context AND (QA OR question answering)", "purpose": "Targeted gap search: long-context QA; top-ranked results inspected, no exhaustive hit count claimed", "records_reviewed": "not claimed", "records_added": 1},
        {"date": "2026-08-02", "source": "ACL Anthology", "query": "multi-agent AND (RAG OR retrieval-augmented generation) AND (QA OR question answering)", "purpose": "Targeted gap search: multi-agent RAG; top-ranked results inspected, no exhaustive hit count claimed", "records_reviewed": "not claimed", "records_added": 1},
    ]
    with (ROOT / "search_log.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(search_rows[0]))
        writer.writeheader()
        writer.writerows(search_rows)

    header = "% Verified and normalised bibliography generated from literature_audit.csv.\n% Evidence roles are documented in that CSV; only sources cited in the manuscript are retained.\n\n"
    (ROOT / "references.bib").write_text(
        header + "\n\n".join(render_bib(*entry) for entry in retained) + "\n",
        encoding="utf-8",
    )

    role_counts = Counter(row["evidence_role"] for row in audit_rows if row["evidence_role"] != "X")
    status_counts = Counter(row["existence_status"] for row in audit_rows)
    summary = {
        "original_candidates": len(inventory), "targeted_additions": len(ADDITIONS),
        "active_bibliography": len(retained), "roles": dict(sorted(role_counts.items())),
        "existence_status": dict(sorted(status_counts.items())),
        "excluded_original_candidates": sum(row["evidence_role"] == "X" for row in audit_rows),
    }
    (WORK / "final_audit_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
