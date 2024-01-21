import sys


def GetAnswer(n, a, q, three, queries):
    # Write your code here



def main():
    n = int(sys.stdin.readline().strip())
    
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline().strip()))
    
    q = int(sys.stdin.readline().strip())
    
    three = int(sys.stdin.readline().strip())
    
    queries = []
    for _ in range(q):
        queries.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split(" "))))

    result = GetAnswer(n, a, q, three, queries)

    print(result)


if __name__ == "__main__":
    main()


def solve(N, M, S, str):
    # Write your code here
    u = S[::-1];c = 0
    for s in str:
        if s in u: # s in S or 
            c+=len(s)*u.count(s); u = u.replace(s,''); # print(u); # print(s) ,1
    return c

def main():
    N = int(sys.stdin.readline().strip())
    
    M = int(sys.stdin.readline().strip())
    
    S = sys.stdin.readline().strip('\n')
    
    str = []
    for _ in range(M):
        str.append(sys.stdin.readline().strip('\n'))

    result = solve(N, M, S, str)

    print(result)


def GetAnswer(n, m, a, b):
    s = 0; bt = 0; c = b[0]; t = []
    # for bt in b:
    for at in range(0, n):
        # print(f"c={c}") # a
        # print(f"at={at}") # a
        if c:
            t.append(a[at]); c-=1;
            if at == n-1:
                if b[bt] == len(set(t)):
                    s+= max(t); # , key = t.count
                    # print(f"s = {s}, e={t}")
                else:
                    s+= max(set(t), key = t.count);
                    # print(f"ee={t}")
            # if bt == m: break
            # print(t)
            # print(c)
        elif b[bt] != len(set(t)):
            s+= max(t); # , key = t.count
            # print(f"s = {s}, e={t}")
            # print(s)
            t = [a[at]]; bt+=1; c = b[bt]-1
        else:
            s+= max(set(t)); # , key = t.count
            # print(f"s = {s}, e={t}")
            # print(s)
            t = [a[at]]; bt+=1; c = b[bt]-1
    return s
    
def main():
    n = int(sys.stdin.readline().strip())
    
    m = int(sys.stdin.readline().strip())
    
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline().strip()))
    
    b = []
    for _ in range(m):
        b.append(int(sys.stdin.readline().strip()))

    result = GetAnswer(n, m, a, b)

    print(result)
