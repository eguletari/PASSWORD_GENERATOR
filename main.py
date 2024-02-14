import random  #import random module that would be used to generate our password


#manually popullate a list with letters number and symbols that would be usedd to generate a user password

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols =['!','#','$','%','&','(',')','*','+']

ai = letters
ai += numbers
ai += symbols


#based on our users choices we wouldd create a random password for them
print("WELCOME TO GERMAN PASSWORD GENERATOR")
choice =int(input('There are 4 types of combination to have in your password.\n1.type 1 for "only letters and numbers"\n2. type 2 for "only letters and symbols"\n3. type 3 for "only numbers and symbols"\n4. type 4 for "letters, numbers and symbols"\n5. type 5 for me to generate a random password for you\n which combination you want?:'))

password = ""

#if statement for each choice the user picks
if choice == 1:
    upl_letters = int(input("\nhow many letters would you like in your password?\n"))
    upl_numbers = int(input("\nhow many numbers do you want in your password\n"))

    #using the for loop andd the random.randint function we would generate a password
    for n in range(0, upl_letters):
        password += letters[random.randint(0, len(letters)-1)]

    for n in range(0,upl_numbers):
        password += numbers[random.randint(0, len(numbers)-1)]

elif choice == 2:
    upl_letters = int(input("\n how many letters would you like in your password?\n"))
    upl_symbol = int(input("\n how many symbols do you want in your password?\n"))

    for n in range(0, upl_letters):
        password += letters[random.randint(0, len(letters)-1)]

    for n in range(0,upl_symbol):
        password += symbols[random.randint(0, len(symbols)-1)]

elif choice == 3:
    upl_numbers = int(input("\n how many numbers would you like in your password?\n"))
    upl_symbol = int(input("\n how many symbols do you want in your password?\n"))

    for n in range(0, upl_numbers):
        password += letters[random.randint(0, len(numbers) - 1)]

    for n in range(0, upl_symbol):
        password += symbols[random.randint(0, len(symbols) - 1)]

elif choice == 4:
    upl_letters = int(input("\n how many letters would you like in your password?\n"))
    upl_numbers = int(input("\n how many numbers would you like in your password?\n"))
    upl_symbol = int(input("\n how many symbols do you want in your password?\n"))

    for n in range(0, upl_letters):
        password += letters[random.randint(0, len(letters) - 1)]

    for n in range(0, upl_numbers):
        password += letters[random.randint(0, len(numbers) - 1)]

    for n in range(0, upl_symbol):
        password += symbols[random.randint(0, len(symbols) - 1)]

elif choice == 5:
    gen_ai = int(input("\nhow long do you want the password to be?\n"))
    for n in range(0, gen_ai):
        password += ai[random.randint(0, len(ai) - 1)]

else:
    print("\n You entered a wrong number!\n Try again")

print(f"\n Total character of your password is:  {len(password)}")
if len(password)  >= 8 and len(password) < 12:
    password = ''.join(random.sample(password, len(password)))
    print(f"your password is {password} \n but be careful you could still be hacked")

elif len(password) >= 12 and len(password) < 17:
    password = ''.join(random.sample(password, len(password)))
    print(f"your password is {password} \n you just managed to escape hacking, watch your back")

elif len(password) >= 17:
    password = ''.join(random.sample(password, len(password)))
    print(f"your password is {password} \n you are lucky I cant guess this password")


else:
    print("\nare you trying to get hacked?\n Try again")

