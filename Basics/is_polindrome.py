def is_palindrome(word):
    word=word.strip()
    rev_word=word[::-1]
    if word == rev_word:
        print("is polindrome.")
    else:
        print("is not polindrome.")

def main():
    word=input("please enter a word:")
    is_palindrome(word)
main()