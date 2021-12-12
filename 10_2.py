scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

with open('tests/10_2.input', 'r') as inp:
    scores_list = []
    for line in inp:
        score = 0
        stack = []
        incomplete = True
        for sym in line[:-1]:
            if sym in ['(', '[', '{', '<']:
                stack.append(sym)
            else:
                if sym == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        incomplete = False
                        break
                elif sym == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        incomplete = False
                        break
                elif sym == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        incomplete = False
                        break
                elif sym == '>':
                    if stack[-1] == '<':
                        stack.pop()
                    else:
                        incomplete = False
                        break
        if incomplete:
            while len(stack) > 0:
                score = 5 * score + scores[stack.pop()]
            scores_list.append(score)
    scores_list.sort()
    print(scores_list[len(scores_list) // 2])