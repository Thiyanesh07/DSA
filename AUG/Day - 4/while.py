# palindrome using while loop

text = input()
i, j = 0, len(text) - 1
is_palindrome = True

while i < j:
    if text[i] != text[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

print("String:", text)
print("Is Palindrome?", is_palindrome)
