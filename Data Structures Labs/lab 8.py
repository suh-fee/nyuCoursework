def pal(s):
    fin_lst = ['']
    leng = len(s) * 2
    fin_lst *= leng
    for i in range(len(s)):
        fin_lst[i] = s[i]
    for i in range(len(s) - 1, -1, -1):
        fin_lst[len(s) + i] = s[len(s) - i - 1]
    return ''.join(fin_lst)


print(pal('hello'))