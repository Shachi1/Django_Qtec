text = input()
pattern = input()

textLength = len(text)
patternLength = len(pattern)

i, j, cnt = 0, 0, 0

while i < textLength:
    # when letter matches
    if text[i] == pattern[j]:
        i += 1
        j += 1
    else:
        i += 1
        j = 0
    # when pattern matches
    if j == patternLength:
        cnt += 1
        j = 0

print(cnt)
