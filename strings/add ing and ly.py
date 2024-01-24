s=input()
b=[]
if(len(s)<=3):
    print(s)
if(len(s)>3):
    for i in range(len(s)-3,len(s)):
        if(s[i]=='i'and s[i+1]=='n' and s[i+2]=='g'):
            print(s[:-3]+"ly")
            break
        else:
            print(s+"ing")
            break
