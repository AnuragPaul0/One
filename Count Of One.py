def getCountOfOneNumbers(L, R):
    result= 0
    # write your Logis here:
    while(L<=R):
        if int(str(L)[0])==1:
            result+=1
        L+=1
    return result #INPUT #OUTPUT
    # print(getCountOfSantiagoNumbers(0, 500))
