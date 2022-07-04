def  area_of_triangle(a,b,c):
     s = (a + b + c) /2
    area = (s * (s- a) * (s -b) * (s - c)) ** 0.5
    return area
def  area_of_circle(r):
     area2 = 3.14 * r **2
     return area2

def area_of_rectangle(l,b):
    area3 = l*b
    return area3


if __name__ == "__main__":
    a = 3
    b = 4
    c = 3
    r = 5
    l = 5
    b = 2
    area1 = area_of_triangle(a,b,c)
    area2 = area_of_circle(r)
    area3 = area_of_rectangle(l,b)
    print(area_of_triangle is {area1})
    print(area_of_circle is {area2})
    print(area_of_rectangle is {area3})