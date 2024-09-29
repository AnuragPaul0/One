def nicePair(S):
    result = 0
    n = len(S)
    for i in range(n-1):
        # print(i)
        for j in range(i,n-1-1):
            if S[i]=='a' and S[j+1] == 'b': result += 1
    return result
print(nicePair('ababasbsbsb'))
# 9
