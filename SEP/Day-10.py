def is_palindrome(s):
    cleaned_s = s.replace(" ", "").lower()
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("A man a plan a canal Panama")) 
print(is_palindrome("hello")) 