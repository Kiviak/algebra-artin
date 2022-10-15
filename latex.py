

def katex(mfile):
    import re
    # fpath='/home/kivi/algebra-artin/2/'
    # fpath='/home/kivi/algebra-artin/unsolved/2/'
    # fname='2.10.4.md'

    keywords=[r'[A-Z0-9.-]+',r'[b-z]{1,1}']
    # keyw=[r'[A-Z]+',r'[0-9.-]+']
    arr=[]
    f=open(mfile,'rt+',encoding="utf-8")
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


if __name__=='__main__':
    chapter=3
    arr=[11,2,8,5,3,4]

    fpath='/home/kivi/algebra-artin/'+str(chapter)+'/'
    # fpath2='/home/kivi/algebra-artin/solution/'+str(chapter)+'/'

    section=len(arr)
    section=6

    for i in range(section):
        # fname='.'.join([str(chapter),str(i+1),str(arr[i]),'md'])
        if i+1<section:
            continue
        for j in range(arr[i]):
            fname='.'.join([str(num) for num in [chapter,i+1,j+1]]+['md'])
            f2=fpath+fname
            katex(f2)