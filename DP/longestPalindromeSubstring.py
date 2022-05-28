def longestPalSubstr(st):
    n = len(st)
    tab = [[0 for i in range(n)] for j in range(n)]
    maxLength = 1
    i = 0
    while(i < n):
        tab[i][i] = True
        i = i+1
    i = 0
    x = 0
    while i < n-1:
        if(st[i] == st[i+1]):
            tab[i][i+1] = True
            x = i
            maxLength = 2
        i = i+1
    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if(st[i] == st[j] and tab[i+1][j-1]=True):
                tab[i][j] = True
                if k > maxLength:
                    maxLength = k
                    start = i
            i = i+1
        k = k+1
    return maxLength