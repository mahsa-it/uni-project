#02. Shopping Cart


#- کاربر نام ۵ محصول رو وارد کنه.
#- محصولات داخل یک لیست ذخیره بشن.
#- امکان اضافه کردن محصول جدید وجود داشته باشه.
#- امکان حذف محصول وجود داشته باشه.
#- امکان مرتب‌سازی محصولات به ترتیب حروف الفبا وجود داشته باشه.
#- در پایان لیست نهایی نمایش داده بشه.
# append()، insert()، remove()، pop()، sort()، reverse()
# برای حذف و اضافه کردن محصولات از کاربر ورودی بگیر


#- کاربر نام ۵ محصول رو وارد کنه.
#- محصولات داخل یک لیست ذخیره بشن.
def get_list(item_count):
    item_list=[]

    for i in range(item_count):
        item=input(f"please enter item {i+1}: ")
        item_list.append(item)
    return item_list


#- امکان اضافه کردن محصول جدید وجود داشته باشه.
def add_item(shopping_list):
    while True:
        ask=input("Do you want to add more items? if yes type y if no type n: ")
 
        if ask == "y":
            y=int(input("how many items do you want to add?"))
            for i in range(y):
                item=input("enter item :")
                shopping_list.append(item)
            break    
        elif ask == "n":
            print("okkay.you dont want to add any item.")
            break
        else:
            print("incorrect input.")
    return shopping_list        

#- امکان حذف محصول وجود داشته باشه.
def remove_item(shopping_list):
        while True:
            ask=input("Do you want to remove any item? if yes type y if no type n: ")
        
            if ask == "y":
                y=int(input("how many items do you want to remove?"))
                for i in range(y):
                    item=input("enter item :")
                    shopping_list.remove(item)
                break
            elif ask == "n":
                print("okkay.you dont want to remove any item.")
                break
            else:
                print("incorrect input.")
        return shopping_list     

def print_shopping_list(shopping_list):
    shopping_list.sort()
    for i in range(len(shopping_list)):
        print(f"{i+1}: {shopping_list[i]}")
    

def main():
    while True:

        try:
            item_count=int(input("how many items you want to buy?(please enter a number.) "))
            if item_count > 0:
                break
        except ValueError:
            print("please enter a number.")
    
    shopping_list=get_list(item_count)
    print_shopping_list(shopping_list)
    shopping_list=add_item(shopping_list)
    print_shopping_list(shopping_list)
    shopping_list=remove_item(shopping_list)
    print_shopping_list(shopping_list)
main()