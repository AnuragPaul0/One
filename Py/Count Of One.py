def getCountOfOneNumbers(L, R):
    # SantiagoNumbers
    result = 0
    while(L<=R):
        if int(str(L)[0])==1:
            result+=1
        L+=1
    return result #INPUT #OUTPUT
# print(getCountOfOneNumbers(0, 500))
# 111
