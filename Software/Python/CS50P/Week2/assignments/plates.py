def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not valid_length(s):
        return False
    if not tw_lttr_strt(s):
        return False
    if not numbers_at_end(s):
        return False
    if not no_leading_zero(s):
        return False
    if not no_punctuation(s):
        return False
    return True

def tw_lttr_strt(s):
    return s[0].isalpha() and s[1].isalpha()        #s[0] is the first character and .isalpha checks if it is a letter

def valid_length(s):
    return 2 <= len(s) <= 6         #check if the length of s (also plate) is between 2 and 6

def numbers_at_end(s):
    reached_numbers = False
    for letter in s:
        if letter.isdigit():
            reached_numbers = True
        if reached_numbers and letter.isalpha():
            return False
    return True

def no_leading_zero(s):
    for letter in s:
        if letter.isdigit():
            return letter != "0" #!= means is not
    return True

def no_punctuation(s):
    for letter in s:
        if not letter.isalpha() and not letter.isdigit():
            return False
    return True



main()