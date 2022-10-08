
import re
fpath='/home/kivi/algebra-artin/2/'
# fpath='/home/kivi/algebra-artin/unsolved/2/'
fname='2.10.4.md'

keywords=[r'[A-Z0-9.-]+',r'[b-z]{1,1}']
# keyw=[r'[A-Z]+',r'[0-9.-]+']
arr=[]
f=open(fpath+fname,'rt+',encoding="utf-8")
for line in f:
    print(line)
    arr.append(line)
page=''.join(arr)
words=page.split()
lens=len(words)
tail=[',','?']

for i in range(lens):
    for pattern in keywords:
        res=re.findall(pattern,words[i])
        if res and (len(res[0])==len(words[i])):
            if words[i][-1]=='.':
                words[i]=''.join(['$',res[0][0:-1],'$',words[i][-1]])
            else:
                words[i]=''.join(['$',res[0],'$'])
            break
        elif res and (len(res[0])==len(words[i])-1) and (words[i][-1] in tail):
            words[i]=''.join(['$',res[0],'$',words[i][-1]])
            break 

page=' '.join(words)

f.seek(0)    
f.write(page)
f.truncate()
f.close()