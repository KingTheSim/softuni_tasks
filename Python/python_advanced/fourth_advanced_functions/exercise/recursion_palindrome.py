def palindrome(word, ind):
    if word[ind] == word[-ind - 1] and ind == len(word) // 2:
        return f"{word} is a palindrome"
    if word[ind] == word[-ind - 1]:
        return palindrome(word, ind + 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
