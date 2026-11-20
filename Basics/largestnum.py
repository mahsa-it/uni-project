def largest(numbers):
    large=numbers[0]
    #if large < numbers[1]:
    #   large=numbers[1]
    #if large < numbers[2]:
    #   large=numbers[2]
    for i in range(1,3):
        if numbers[i] > large:
            large=numbers[i]
    return large

def main():
    try:
        numbers=[]
        for i in range(3):
            num=float(input(f"enter number {i+1}:")) 
            numbers.append(num)
        res=largest(numbers)
        print(f"largest number is {res}")
    except ValueError:
        print("error: enter a valid number not character")
main()
   
