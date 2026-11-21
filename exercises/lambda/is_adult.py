is_adult= lambda age : "true" if age > 18 else "false"
age=int(input("enter your age:"))
print(f"are you an adult?{is_adult(age)}")