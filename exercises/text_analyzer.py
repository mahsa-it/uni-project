# String Methods
#1. Text Analyzer
#برنامه‌ای بنویس که یک جمله از کاربر دریافت کنه و اطلاعات زیر رو نمایش بده:


#- تبدیل تمام حروف به حروف کوچک
#- تبدیل تمام حروف به حروف بزرگ
#- جایگزینی یک کلمه با کلمه جدید
#- بررسی اینکه یک کلمه خاص در جمله وجود داره یا نه
#مفاهیم مورد استفاده: split()، join()، strip()، replace()، find()، lower()، upper()
# hello my name is mahsa           5 18 

#- تعداد کلمات جمله
def word_count(user_text):
    word_list=user_text.split()
    res=len(word_list)
    return res

#- تعداد کاراکترها بدون احتساب فاصله‌ها
def character_count(user_text):
    x=len(user_text.replace(" ",""))
    return x 

#- جایگزینی یک کلمه با کلمه جدید
def replace_word(user_text):
    ask=input("do you want to replace any words? type y for yes and n for no: ")
    if ask == "y":
        replace_count=int(input("how many words do you want to replace?(enter a number.) "))
        
        for i in range(replace_count):
                tword=input(f"please enter word {i+1} from text to replace: ")
                rword=input(f"please enter the word you want to replace with: ")
                text_list=user_text.split()
                for j in range(len(text_list)):
                    if text_list[j] == tword:
                        text_list[j]=rword
                user_text=" ".join(text_list)
                #user_text=user_text.replace(tword,rword)
    else:
        print("no rplace.")
    return user_text


#- بررسی اینکه یک کلمه خاص در جمله وجود داره یا نه
def check_special_word(user_text):
    ask=input("do you want to check any words? type y for yes and n for no: ")
    if ask == "y":
        wword=input(f"please enter word from text to chheck: ")
        if wword in user_text.split():
            return "yes"
        else:
            return "no"
    else:
        return "no word to check"
          
def check_sound(user_text):
    user_text=user_text.lower()
    if "a" in user_text:
        print(f"you have {user_text.count('a')} a.")
    if "e" in user_text:
        print(f"you have {user_text.count('e')} e.")
    if "i" in user_text:
        print(f"you have {user_text.count('i')} i.")
    if "o" in user_text:
        print(f"you have {user_text.count('o')} o.")
    if "u" in user_text:
        print(f"you have {user_text.count('u')} u.")



def main():
    user_text=input("please enter your text:")

    #- تعداد کلمات جمله
    print(f"word count:{word_count(user_text)}")

    #- تعداد کاراکترها با احتساب فاصله‌ها
    print(f"character count with counting space: {len(user_text)}")

    #- تعداد کاراکترها بدون احتساب فاصله‌ها
    print(f"character count without counting space: {character_count(user_text)}")

    #- جایگزینی یک کلمه با کلمه جدید
    x=replace_word(user_text)
    print(f"result:{x}")

    #- تبدیل تمام حروف به حروف بزرگ
    print(f"text in uppercase: {user_text.upper()}")

    #- تبدیل تمام حروف به حروف کوچک
    print(f"text in lowercase: {user_text.lower()}")

    #- بررسی اینکه یک کلمه خاص در جمله وجود داره یا نه
    y=check_special_word(user_text)
    print(f"result : {y}")
    check_sound(user_text)
main()