def check_prime(number):
    if number <= 1:
        print("it is not prime.")
    else :
        for i in range(2,number):
            if number % i == 0:
                print(f"{number}%{i}=0, so it is not prime.")
                break
        else:
            print("is  prime.")


def main():
    while True:
        try:
            number=int(input("enter number:"))
            break
        except ValueError:
            print("enter a number like 1,2,...")
    check_prime(number)
main()