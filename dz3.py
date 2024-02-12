def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(text):
    words = text.split()

    palindromes = [word for word in words if is_palindrome(word)]

    return palindromes

input_text = input("Введите текст: ")
palindromes = find_palindromes(input_text)

if palindromes:
    print("Слова-палиндромы в тексте: ")
    for palindrome in palindromes:
        print(palindrome)
else:
    print("В тексте нет слов-палиндромов. ")