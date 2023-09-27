class Circle:
    pass

def create(r):
    c=Circle()
    c.r=r
    return c

def perimeter(c):
    return 2*(3.14)*c.r

def area(c):
    return (3.14)*c.r*c.r

def info(c):
    print(f'Circle<{c.r}>')

def result_circle(r):
    c=create(r)
    info(c)
    print(f'Area={area(c)}')
    print(f'Perimeter={perimeter(c)}')

result_circle(7)
