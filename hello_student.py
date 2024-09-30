#use print() function
print('hi student from ET574!\n')
try:
    courseNum = eval(input("Enter your course number: "))
    print(f"\nHello, welcome to the course ET{courseNum}!")
except:
    print("Hello, world!")