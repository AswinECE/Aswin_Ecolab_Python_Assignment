def function(A):

    for key,value in A.items():
        print(f'{key}|{"++++"*value*1} {value}')

A = {1:5, 2:9, 3:4, 4:6, 5:2}
function(A)