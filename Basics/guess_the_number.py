def main():
    number=83
    try_count=0
    while True:
        try:
            guess=int(input("please guess:"))
            try_count +=1
            if guess == number:
                print(f"congradulation.\n you try:")
                if try_count == 1:
                    print("1 time.")
                    break
                else:
                    print(f"you try {try_count}.")
                    break
            elif guess > number:
                print("your guess is bigger than the number,try again.") 
            else:
                print("your guess is smaller than the number,try again.")     
        except ValueError:
            print("please enter a number.")
    return
        
main()