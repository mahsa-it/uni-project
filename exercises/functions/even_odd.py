def even_or_odd(num):
    if num % 2 == 0 :
        return "even"
    else:
        return "odd"
    
def main():
    while True:
        try:
            num=int(input("please enter a number to check: "))
            print(f"number {num} is {even_or_odd(num)}")
            break
        except ValueError:
            print("please enter a number like 1,2,..: ")


main()