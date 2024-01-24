'''
def comp(s):
    c=1
    res=''
    for i in range(1,len(s)):
        if(s[i]==s[i-1]):
            c=c+1
        else:
            res+=s[i-1]+str(c)
            c=1
    res+=s[-1]+str(c)
    return res
s=input()
res=comp(s)
print(res)
'''
class Solution:
    def compress(self, ch: list[str]) -> int:
        res = []
        c = 1
        for i in range(1, len(ch)):
            if ch[i] == ch[i - 1]:
                c = c + 1
            else:
                if c > 1:
                    res.extend([ch[i - 1], str(c)])
                else:
                    res.append(ch[i - 1])
                c = 1
            if c > 1:
                res.extend([ch[-1], str(c)])
            else:
                res.append(ch[-1])
        return len(res)
solution=Solution()
ch=input()
ress=compress(ch)
print(ress)
