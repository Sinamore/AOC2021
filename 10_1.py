scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

with open('tests/10_1.input', 'r') as inp:
    score = 0
    for line in inp:
        stack = []
        for sym in line[:-1]:
            if sym in ['(', '[', '{', '<']:
                stack.append(sym)
            else:
                if sym == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        score += scores[')']
                        break
                elif sym == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        score += scores[']']
                        break
                elif sym == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        score += scores['}']
                        break
                elif sym == '>':
                    if stack[-1] == '<':
                        stack.pop()
                    else:
                        score += scores['>']
                        break
    print(score)