

if __name__=='__main__':
    chapter=3
    arr=[11,2,8,5,3,4]
   
    fpath='/home/kivi/algebra-artin/'+str(chapter)+'/'
    fpath2='/home/kivi/algebra-artin/solution/'+str(chapter)+'/'

    section=len(arr)

    for i in range(section):
        
        for j in range(arr[i]):
            fname='.'.join([str(num) for num in [chapter,i+1,j+1]]+['md'])
            f2=fpath+fname
            f3=fpath2+fname
            f=open(f2,'x')
            f.close()
            f=open(f3,'x')
            f.close()


