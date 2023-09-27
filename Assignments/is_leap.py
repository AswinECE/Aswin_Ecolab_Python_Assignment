def is_leap(year):
    dr=4
    if year%100==0:
        dr=400
    if year%dr==0:
        return True
    else:
        return False

print(is_leap(2000))
print(is_leap(1700))
                 