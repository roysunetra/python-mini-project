print("Hi!! I am a password generator\n")
password_length = int(input("Enter the length of the password : \n"))
import string
import random
lowercase_letter = string.ascii_lowercase
uppercase_letter = string.ascii_uppercase
digit_please = string.digits
punctuation_please = string.punctuation
final_password = []
final_password.extend(list(lowercase_letter))
final_password.extend(list(uppercase_letter))
final_password.extend(list(digit_please))
final_password.extend(list(punctuation_please))
random.shuffle(final_password)
print("Here is your password :")
print("".join(final_password[0:password_length]))