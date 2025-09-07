# replace vowels with *

def censor_vowels(s_list):
    vowels = "aeiouAEIOU"
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i] = "*"

text = list("Education")
print("Before:", "".join(text))
censor_vowels(text)
print("After :", "".join(text))

