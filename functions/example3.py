def  area_of_triangle():
    a = int(input("enter the length of side a:"))
    b = int(input("enter the lentgh of side b:"))
    c = int(input("enter the lentgh of side c:"))
    s = a + b + c / 2
    area = (s*(s - a) * (s - b) * (s - c) **0.5)
    print("the area of the triangle is: ", area)

def area_of_circle():
        r = int(input("enter the radius of the circle:"))
        area = 3.14*r**2
        print("the area of the circle is:", area)

def area_of_rectangle():
            l = int(input("enter the length of retangle"))
            b = int(input("enter the length of retangle"))
            area = l*b
            print("the area of rectangle is :", area)

#main program starts here
def menu():
    print("1.area of triangle") 
    print("2. area of circle")
    print("3. area of rectangle")
    print("4. quit")
    choice = int(input("enter your choice:"))
    if choice == 1:
        area_of_triangle()
    elif choice == 2:
        area_of_circle()
    elif choice == 3:
        area_of_rectangle()
    elif choice == 4:
        print("goodbye")
    else:
        print("invalid choice")
        menu()    

if __name__ == "__main__":
    menu()       

