# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0
def strings_xor(s, t):
    '''
    Table XOR
    # 0 0 0
    # 0 1 1
    # 1 0 1
    # 1 1 0
    '''
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = input()
t = input()
print(strings_xor(s,t))
print(strings_xor('10101','00101'))