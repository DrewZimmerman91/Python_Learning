#Import random library
import random

print('Welcome To Your Password Generator')
#Characters available for the generator to use
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'
#Number of passwords to generate
number = input('Amount of passwords to generate: ')
#Sets number variable to an integer 
number = int(number)
#Length the user wants the generated passwords to be
length = input('Your password length: ')
#Sets the length variable to an integer
length = int(length)
#Prints generated passwords for user
print('\nhere are your passwords:')
#For loop generates passwords based off of the range of characters needed and random uses the character sets set by chars variable then prints the passwords for the user
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)