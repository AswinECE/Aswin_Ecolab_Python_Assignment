def freq_distribution(list):
    S={}

    for i in range(len(list)):
        d=list[i]
        count=0

        for j in range(i,len(list)):
            if list[j]==list[i]:
                count+=1
        P=dict({d:count})
        if d not in S.keys():
            S.update(P)
    print('The frequency distribution of the given sequence is ','\n',S)

list = [1,1,1,2,2,2,3,3,3,4,4,5,6,7,8]
freq_distribution(list)