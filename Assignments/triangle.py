def Triangle_perimeter(s1,s2,s3):
    if s3>0 and s2>0 and s1>0 and s1<s1+s2 and s2<s1+s3 and s3<s2+s1:
        return s1+s2+s3
    else:
        return float("NaN")

def Circle_perimeter(r):
    return 2* 3.14 *r

shape = input("Enter the shape of the geometry: ")
if shape == "triangle":
    print(Triangle_perimeter (4,5,6))
elif shape == "circle":
    print(Circle_perimeter(3))
    
'''class triangle():
    def perimeter_of_triangle(self, s1, s2, s3):
        P = s1+s2+s3
        return P
object1= triangle()
print(object1.perimeter_of_triangle(3,4,5))

class circle():
    def perimeter_of_cicle(self, r):
        P = 2*3.14*r
        return P
object2= circle()
print(object2.perimeter_of_cicle(8))'''