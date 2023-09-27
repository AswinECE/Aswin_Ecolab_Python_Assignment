min = int(input('Enter the min value: '))
max = int(input('Enter the max value: '))
for num in range(min, max+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)