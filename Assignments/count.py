def histogram(*args,design,flag):
    d={}
    for i in range(len(args)):
        a=args[i]
        count=0
        for j in range(i,len(args)):
            if args[j]==args[i]:
                count=count+1
        if flag:
            h=f'{count * design} {count}'
            c=dict({a:h})
            if a not in d.keys():
                d.update(c)
        else:
            h=f'{count * design}'
            c=dict({a:h})
            if a not in d.keys():
                d.update(c)
    for x,y in d.items():
        print(x,y)
    #print (d)
#l=list(map(int,input().split()))
histogram(1,2,3,4,1,2,3,4,1,2,3,1,2,1,design="+++++",flag=False)