def caesar_encrypt(text):
    res=""
    for ch in text:
        if "A" <= ch <= "Z" :
            res+= chr((((ord(ch) - ord("A"))+ 3) % 26) + ord("A"))
        elif "a" <= ch <= "z":
            res+= chr((((ord(ch) - ord("a"))+ 3) % 26) + ord("a"))
        else:
             res+=ch
    return res

def main():
    text=input("enter text:")
    res=caesar_encrypt(text)
    print(f"output:{res}")
main()
