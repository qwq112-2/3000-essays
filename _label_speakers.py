import re, json

# Read current file (with partial labels)
with open('interview_raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Strip ALL existing labels for a clean start
text = re.sub(r'\*\*Emily Chang:\*\*\s*', '', text)
text = re.sub(r'\*\*Dario Amodei:\*\*\s*', '', text)

# Split into paragraphs
raw_paras = [p.strip() for p in re.split(r'\n\n+', text) if p.strip()]
raw_paras = [p for p in raw_paras if p not in ('[music]', '(laughter)')]

result = []

for para in raw_paras:
    para = para.strip()
    words = len(para.split())

    # Emily's known lines (short pushbacks, setups, quips)
    if para in ('Okay. But everyone else held hands. Come on.',
                'Explain that.',
                'Just a little powder.',
                'But that\'s not my question. My question is a decision making over what we do.'):
        result.append(('Emily', para))
        continue

    # Check if paragraph starts with a question-answer pattern
    # Find the first sentence that ends with ?
    q_match = re.match(r'^([^?]*\?)', para)
    if q_match:
        q_end = q_match.end()
        question = para[:q_end].strip()
        answer = para[q_end:].strip()
        q_words = len(question.split())
        a_words = len(answer.split()) if answer else 0

        # If question is short and there's a substantial answer → split
        if q_words < 50 and a_words > 5:
            result.append(('Emily', question))
            result.append(('Dario', answer))
            continue
        elif q_words < 20 and a_words <= 5:
            # Just a question, no answer
            result.append(('Emily', para))
            continue
        elif q_words >= 50:
            # Long text with embedded question - likely Dario speaking
            result.append(('Dario', para))
            continue

    # No clear question split - use heuristics
    # Short paragraphs that are clearly Emily
    short_emily_starts = [
        'So my son', 'Okay.', 'All right.', 'But that\'s not',
        'Just a', 'We will see', 'Uh hopefully', 'That\'s right',
        'I love writing', 'I think we could', 'You\'ve been really',
        'You put out', 'So play this', 'There has been',
        'One of the leading', 'The standoff', 'You\'ve had a long',
        'You\'ve been working', 'So, you know, you drew',
        'Do you mind', 'A US official', 'Bloomberg has reported',
        'This school had', 'Is AI warfare', 'Have you had',
        'But what about', 'If this helps', 'There was a lot',
        'You know, there\'s this', 'I understand one',
        'You\'ve said there\'s', 'You are building',
        'You worked at', 'Did what you', 'Will you tell me',
        'Your product', 'Your biggest', 'Does it feel',
        'But winning', 'For most of', 'Soon after',
        'I know how', 'There\'s a moment',
    ]

    is_emily = any(para.startswith(s) for s in short_emily_starts)

    # Long paragraphs are always Dario
    if words > 60:
        result.append(('Dario', para))
    elif is_emily:
        result.append(('Emily', para))
    elif words < 15 and '?' in para:
        result.append(('Emily', para))
    else:
        # Default: medium length → probably Dario
        result.append(('Dario', para))

# Merge consecutive Dario paragraphs
merged = []
for speaker, text in result:
    if merged and speaker == 'Dario' and merged[-1][0] == 'Dario':
        merged[-1] = ('Dario', merged[-1][1] + '\n\n' + text)
    else:
        merged.append((speaker, text))

# Write final output
lines = []
for speaker, text in merged:
    label = '**Emily Chang:**' if speaker == 'Emily' else '**Dario Amodei:**'
    lines.append(f'{label} {text}')

output = '\n\n'.join(lines)

with open('interview_raw.txt', 'w', encoding='utf-8') as f:
    f.write(output)

# Count
e_count = output.count('**Emily Chang:**')
d_count = output.count('**Dario Amodei:**')
print(f'Emily sections: {e_count}, Dario sections: {d_count}')
print(f'Total length: {len(output)} chars')
