def main():
    numbers_list=list(map(int, input("enter numbers after eachh other with space: ").split()))
    print(numbers_list)
    numbers_list_updated=[]
    for num in numbers_list:
        if num not in numbers_list_updated:
            numbers_list_updated.append(num)
    print(numbers_list_updated)  


main()