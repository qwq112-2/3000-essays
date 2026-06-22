import json, re

# Read the cleaned transcript
with open('interview_raw.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()

# Read existing articles
with open('articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Create article with full transcript
interview = {
    "id": 11,
    "title": "Inside the Mind of Anthropic CEO Dario Amodei",
    "title_zh": "站在AI风暴中心：对话Anthropic CEO达里奥·阿莫迪（完整专访）",
    "level": "intermediate",
    "type": "interview",
    "description": "Bloomberg The Circuit full 69-minute interview with Emily Chang. Covers: AI exponential growth, leaving OpenAI, Mythos superweapon, job losses, civilization collapse probability, AI warfare, Szilard vs Oppenheimer, and why we should trust him.",
    "description_zh": "彭博社《The Circuit》Emily Chang 69分钟完整专访。涵盖：AI指数增长、离开OpenAI内幕、Mythos超级武器、就业冲击、文明崩溃概率、AI军事应用、西拉德vs奥本海默、以及为什么应该相信他。",
    "content": full_text.strip(),
    "translation_zh": """【编者按】这是彭博社《The Circuit》主持人Emily Chang对Anthropic CEO达里奥·阿莫迪（Dario Amodei）的69分钟深度专访全文。访谈于2026年6月17日发布于Anthropic旧金山总部。

本次访谈被认为是Dario Amodei迄今最坦诚、信息密度最大的一次公开对话，涉及AI能力跃升、就业冲击、文明崩溃概率、秘密模型Mythos、军事AI应用、与Sam Altman的分歧、为何认同西拉德而非奥本海默等重磅话题。

—— 全文中文要点导航 ——

【指数增长的体感】Amodei用相对论比喻AI发展：就像乘坐宇宙飞船以近光速离开地球，睡一觉地球上已过去两天，再睡三天，再睡四天。\"什么都没发生、什么都没发生，然后轰——一切都疯狂了。\"他不偏执，但保持理性警觉。

【离开OpenAI】\"当你感到无法信任某人，当他们的价值观不是他们说的那样，当你看到不诚实的行为模式——就很难继续共事。何必争论？各奔前程，市场见分晓。\"

【为何押注企业级】\"选一个与价值观冲突的商业模式，要么背叛价值观要么变得无足轻重。企业客户重视信任和长期关系，与我们安全部署AI的目标高度协同。\"

【就业：一半白领岗位可能消失】\"我的担忧程度没有变化。自动化90%的工作后，最终会接近100%——必须为人类找到其他事做。\"三类可能幸存的工作：物理世界、人际关系型、指导AI。他痛斥\"末日营销\"指控为\"懒惰\"。

【Mythos超级武器】内部模型能自主完成网络攻击链。早期测试公司说：\"这是超级武器，你应该要持枪证才能用。求你别发布。\"在Firefox中发现271个新漏洞，前代模型零发现。\"我们因为不发布在商业上遭受了巨大损失。\"

【AI与战争】\"更强的军事能力不会引发战争——它能遏制战争。Claude辅助，但人类做最终决定。\"对于伊朗学校被炸事件：\"战争中发生的这些错误真的可怕。\"

【文明崩溃概率10%-25%】\"25%太高了。我们要把它降到低得多。\"用航空公司比喻：你造了比别人安全10倍的飞机，但没法保证永不坠毁。

【西拉德而非奥本海默】\"我实际上把奥本海默看作失败案例。我们需要的不是伟大人物，而是权力制衡——无处不在的制衡。\"

【写作与思考】\"我还没到让Claude直接代写的地步。写作能帮你与想法搏斗。如果端到端用AI写，首先它写不出我的见解，其次我会失去写作的益处。\"

【为什么要相信你？】\"硅谷已失去世界的信任，必须重新赢回来。我们在中国问题上言出必行，花费数亿美元切断模型访问。纵观整个历史，最一致的假设是：我们真的在努力做正确的事。\""""
}

articles.append(interview)

with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False)

print(f'Added full interview. Total articles: {len(articles)}')
print(f'English transcript: {len(interview["content"])} chars, ~{len(interview["content"].split())} words')
print(f'Chinese notes: {len(interview["translation_zh"])} chars')
