#Personal Expense Tracker

# برنامه‌ای بنویس که هزینه‌های شخصی کاربر رو ثبت و مدیریت کنه.
# ۱. ثبت هزینه‌ها
# - از کاربر بپرس چند هزینه می‌خواد ثبت کنه.
# - نام هر هزینه و مبلغ اون رو دریافت کن.
# - نام هزینه‌ها رو در یک لیست و مبلغ‌ها رو در یک لیست جداگانه ذخیره کن.
# - مبلغ باید عدد معتبر و مثبت باشه.

# ۲. نمایش گزارش
# برنامه باید اطلاعات زیر رو نمایش بده:
# - تمام هزینه‌ها و مبلغ هرکدوم
# - مجموع هزینه‌ها
# - میانگین هزینه‌ها
# - بیشترین هزینه
# - کمترین هزینه

# ۳. جست‌وجوی هزینه
# - کاربر نام یک هزینه رو وارد کنه.
# - برنامه بررسی کنه آیا این هزینه وجود داره یا نه.
# - جست‌وجو نباید به حروف کوچک و بزرگ حساس باشه.

# ۴. ویرایش هزینه
# - کاربر نام هزینه‌ای که می‌خواد ویرایش کنه رو وارد کنه.
# - اگر وجود داشت، نام یا مبلغش رو تغییر بده.

# ۵. حذف هزینه
# - کاربر بتونه یک هزینه رو از لیست حذف کنه.
# - حواست باشه اطلاعات دو لیست هماهنگ باقی بمونن.

# ۶. گزارش نهایی
# در پایان یک گزارش مرتب چاپ کن که شامل موارد زیر باشه:
# - تعداد هزینه‌ها
# - مجموع مخارج
# - میانگین مخارج
# - گران‌ترین هزینه
# - ارزان‌ترین هزینه

# ۱. ثبت هزینه‌ها
def create_expense_list(expense_count):
    expense_name_list=[]
    expense_amount_list=[]
    for i in range(expense_count):
        name=input(f"please enter the expense name {i+1}:")
        expense_name_list.append(name)
        while True:
            try:
                amount=float(input(f"please enter the expense amount {i+1}:"))
                if amount >=1 :
                    expense_amount_list.append(amount)
                    break
                else:
                    print("amount should be at least 1.")
            except ValueError:
                print("please enter amount in number.")

    return expense_name_list,expense_amount_list

# # ۲. نمایش گزارش
def display_report(expense_name_list,expense_amount_list):
    print("Expense list:")
    for i in range(len(expense_name_list)):
        print(f"{i+1}){expense_name_list[i]}:{expense_amount_list[i]}")
    total=0
    for i in range(len(expense_amount_list)):
        total += expense_amount_list[i]
    print(f"expenses count: {len(expense_amount_list)}")
    print(f"sum:{total}")
    if len(expense_amount_list) >= 1:
        print(f"average is : {sum(expense_amount_list) / len(expense_amount_list)}")
        print(f"highest expense amount : {max(expense_amount_list)} ")
        print(f"lowest expense amount : {min(expense_amount_list)} ")
    else:
        print("your list is empty.")



def search_expense(expense_name_list,expense_amount_list):
    while True:
        try:
            ask=input("do you want to search or check any expense?(y for yes, n for n.)")
            if ask == "y":
                break
            elif ask == "n":
                print("no search or change.")
                return expense_name_list,expense_amount_list
            else:
                print("wrong input.")
        except ValueError:
            print("please enter y for yes, n for no.")

    while True:
        try:
            search_count=int(input("how many expenses you want to search for?"))
            if search_count < 1:
                print("please enter a positive number and it must not be 0. ")
            else:
                break
        except ValueError:
            print("please enter a number")
    for i in range(search_count):
        search_name=input("please enter the expense name to search for:")
        search_name=search_name.lower()
        expense_name_list_lower=[item.lower() for item in expense_name_list]
        if search_name not in expense_name_list_lower:
            print("this expense is not in your list.")
            continue
        search_name_index=expense_name_list_lower.index(search_name)

        print(f"it is in your list. {search_name} : {expense_amount_list[search_name_index]}")
        while True:
            try:
                ask_change_name=input("do you want to change this expense name?(y for yes, n for no.): ")
                if ask_change_name == "y":
                    break
                elif ask_change_name == "n":
                    print("name wont change.")
                    break
                else:
                    print("wromg input.")
            except ValueError:
                print("please enter y for yes, n for no.")
        if ask_change_name == "y":
            changed_name=input(f"please enter new name for {search_name}: ")
            expense_name_list[search_name_index]=changed_name
            print(f"{search_name} changed in to {changed_name}.")
        while True:
            try:
                ask_change_amount=input("do you want to change this expense amount?(y for yes, n for no.): ")
                if ask_change_amount == "y":
                    break
                elif ask_change_amount == "n":
                    print("amount wont change.")
                    break
                else:
                    print("wrong input")
            except ValueError:
                print("please enter y for yes, n for no.")
        if ask_change_name == "y":
            if ask_change_amount == "y":
                while True:
                    try:
                        changed_amount=float(input(f"please enter new amount for {changed_name}: "))
                        if changed_amount <= 0:
                            print("it can not be negative or 0.")
                        else:
                            break
                    except ValueError:
                        print("incorrect input.")
                expense_amount_list[search_name_index]=changed_amount
                print(f"{changed_name} amount changed in to {changed_amount}.")
        if ask_change_name== "n":
            if ask_change_amount == "y":
                while True:
                    try:
                        changed_amount=float(input(f"please enter new amount for {search_name}: "))
                        if changed_amount <= 0:
                            print("it can not be negative or 0")
                        else:
                            break
                    except ValueError:
                        print("incorrect input.")
                expense_amount_list[search_name_index]=changed_amount
                print(f"{search_name} amount changed in to {changed_amount}.")
                        
    return expense_name_list,expense_amount_list

# # ۵. حذف هزینه
def delete_expense(expense_name_list,expense_amount_list):
    while True:
        try:
            ask=input("do you want to delete any expense?(y for yes, n for no.)")
            if ask == "y":
                break
            elif ask == "n":
                print("no action.")
                return expense_name_list,expense_amount_list
            else:
                print("please enetr y for yes, n for no.")
        except ValueError:
            print("wrong input.")
    while True:
        try:
            delete_count=int(input("how many expense you want to delete?enter a number bgger than 0:"))
            if delete_count < 1:
                print("please enter a number bigger than 0.")
            else:
                break
        except ValueError:
            print("incorrect input.")
    for i in range(delete_count):
        expense_name_list_lower=[item. lower() for item in expense_name_list]
        delete_exp_name=input("please enter the expense you want to delete:")
        delete_exp_name=delete_exp_name.lower()
        if delete_exp_name not in expense_name_list_lower :
            print("this expense is not in your list.")
            continue
        delete_exp_name_index=expense_name_list_lower.index(delete_exp_name)
        expense_name_list.pop(delete_exp_name_index)
        expense_amount_list.pop(delete_exp_name_index)
    return expense_name_list,expense_amount_list
    
# # ۶. گزارش نهایی
# def final_reprt():

def main():
    while True:
        try:
            expense_count=int(input("how many expense you want to add:"))
            if expense_count >= 1:
                break
            else:
                print("wrong input.")
                
        except ValueError:
            print("please enter a number.")
    expense_name_list,expense_amount_list = create_expense_list(expense_count)
    display_report(expense_name_list,expense_amount_list)
    expense_name_list,expense_amount_list=search_expense(expense_name_list,expense_amount_list)
    expense_name_list,expense_amount_list=delete_expense(expense_name_list,expense_amount_list)
    display_report(expense_name_list,expense_amount_list)
main()








# # # ۳. جست‌وجوی هزینه
# def search_expense(expense_name_list,expense_amount_list):
#     while True:
#         try:
#             ask=input("Do you want to search for an expense?(y for yes, n for no)")
#             while True:
#                 try:
#                     if ask== "y":
#                         search_count=int(input("how many expenses you want to search for?"))
#                         if search_count >= 1:
#                             for i in range(search_count):
#                                 search_name=input("please enter expense name:")
#                                 search_name=search_name.lower()
#                                 expense_name_list=[item.lower() for item in expense_name_list ]
#                                 if search_name in expense_name_list:
#                                     index_search_name=expense_name_list.index(search_name)
#                                     print(f"it is in your list. expense number{index_search_name+1}:{search_name}={expense_amount_list[index_search_name]}")

#                                     while True:
#                                         try:
#                                             ask_change_amount=input("do you want to change the amount?(y for yes, n for no.)")
#                                             if ask_change_amount == "y":
#                                                 ask_change_amount=float(input(f"please enter new amount for {search_name}: "))
#                                                 expense_amount_list[index_search_name]=ask_change_amount
#                                                 print(expense_name_list,expense_amount_list)
#                                                 break
#                                             elif ask_change_amount == "n":
#                                                 print("amount is not changed")
#                                                 break
#                                             else:
#                                                 print("wrong input.")
#                                         except ValueError:
#                                             print("wrong input.")
#                                     while True:
#                                             try:
#                                                 ask_change_name=input("do you want to change the name?(y for yes, n for no.)")
#                                                 if ask_change_name == "y":
#                                                     ask_change_name=input(f"please enter new name for {search_name}: ")
#                                                     expense_name_list[index_search_name]=ask_change_name
#                                                     print(expense_name_list,expense_amount_list)
#                                                     break
#                                                 elif ask_change_name == "n":
#                                                     print("name is not changed")
#                                                     break
#                                                 else:
#                                                     print("wrong input.")
#                                             except ValueError:
#                                                 print("wrong input.")
#                                 else:
#                                     print("you dont have this expense.")
#                             break
#                         else:
#                             print("wrong input.")
#                     elif ask == "n":
#                         break
#                     else:
#                         print("incorrect input")
#                 except ValueError:
#                     print("please enter a number.")
#         except ValueError:
#             print("please ennter y for yes, n for no")