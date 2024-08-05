def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ': continue
        correction = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr((ord(s[i]) - correction + n)% 26 + correction)
    return ''.join(s)