# Read input from STDIN. Print output to STDOUT
al = "abcdefghijklmnopqrstuvwxyz"
s = input()
ca = 1
for c in al:
    if c not in s.lower():
        print("false") # F
        ca = 0
        break
if ca:
    print("true") # T
print(s)
# 0abcdefghijklmnopqrstuvwxyZ
