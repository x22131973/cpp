age =int(input("Please Enter your age : "))
height = int(input("Please Enter your heigh in cms: "))
Rw = (height - 100 + age % 10) * 0.90
print(f"Recommended weight is {Rw} ")