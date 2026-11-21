def factorial(num):
    res=1
    for i in range(num):
        res *= num
        num -=1
    return res

def main():
    while True:
        try:
            num=int(input("enter a number :"))
            if num > 0:
                break
            else:
                print("please enter a positive number.")
        except ValueError:
            print("please enter a number like 1, 2 ,..:")
    print(f"result is :{factorial(num)}")

main()