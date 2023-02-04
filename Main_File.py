import webbrowser
import wikipedia
import datetime
import random
###
print("Welcome to the Mini Assistant!")
option = input('''Please type in what you what to open or display:
                NT for New Tab,
                NW for New Window,
                OL to open a link,
                W for Wikipedia,
                CDT for current date and time,
                TD for today's date,
                MT to display a number's multiplication table,
                CL for Calculator,
                AST for Astronomical Sign Teller,
                LS for Letter Sorter,
                EO for Even or Odd identifier,
                LY for Leap Year identifier,
                VC for Vowel or Consonant identifier,
                RN for Random Number generator,
                SC for Savings Calculator,
                MR for Mini Restaurant
                   ''')
option = option.lower()
###
if option == "nt":
    link = input("What link do you want to open in a new tab? Please be careful and type the right url: ")
    webbrowser.open_new_tab(link)
###
elif option == "nw":
    NT = input("What link do you want to open in a new window? Please be careful and type the right url.")
    webbrowser.open_new(NT)
###
elif option == "ol":
    OL = input("What link do you want to open? Please be careful and type the right url.")
    webbrowser.open(OL)
###
elif option == "w":
    W = input("What Wikipedian article do you want to open. Please be careful and check your capitalization.")
    lang = input("What language do you want it in? Please go to this article: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes and type in the language code. Remember to type it in lowercase letters.")
    wikipedia.set_lang(lang)
    info = wikipedia.summary(W,sentences=7)
    print('''Here is your info from Wikipedia:
            ''')
          
    print(info)
###
elif option == "cdt":
    datetime_object = datetime.datetime.now()
    print("The date and time is {}.".format(datetime_object))
###
elif option == "td":
    date_object = datetime.date.today()
    print("The today's date is {}.".format(date_object))
###
elif option == "mt":
    num = int(input("What number's multiplication table do you want me to display?"))
    num2 = int(input("What number do you want your previous number to be multiplied until?"))
    for i in range(1,num2 + 1):
        print(num, 'x', i, '=', num*i)
###
elif option == "cl":
    while True:
        operation = input('''
        Please type in the math operation you would like to complete:
            + for addition
            - for subtraction
            * for multiplication
            / for division
            // for floor division
            % for modulo
            ** for exponents
                            ''')

        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))

        if operation == '+':
            print('{} + {} = '.format(num1, num2))
            print(num1 + num2)

        elif operation == '-':
            print('{} - {} = '.format(num1, num2))
            print(num1 - num2)

        elif operation == '*':
            print('{} * {} = '.format(num1, num2))
            print(num1 * num2)

        elif operation == '/':
            print('{} / {} = '.format(num1, num2))
            print(num1 / num2)
            
        elif operation == '//':
            print('{} // {} = '.format(num1, num2))
            print(num1 // num2)

        elif operation == '%':
            print('{} % {} = '.format(num1, num2))
            print(num1 % num2)

        elif operation == '**':
            print('{} ** {} == '.format(num1,num2))
            print(num1 ** num2)
            
        again = input("Do you want to use the calculator again? Please enter yes or no: ")
        again = again.lower()
        if again == "yes":
            pass
        elif again == "no":
            print("Thank you for using the Calculator! Have a nice day!")
            break
        else:
            print("Invalid input.")
            break
    
###
elif option == "ast":
    month = input("Please enter in the month you were born in: ")
    day = int(input("Please enter in the day you were born on: "))
    month = month.upper()
    if month == 'DECEMBER':
       astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 'JANUARY':
       astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'FEBRUARY':
       astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'MARCH':
       astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'APRIL':
       astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'MAY':
       astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'JUNE':
       astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'JULY':
       astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'AUGUST':
       astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'SEPTEMBER':
       astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'OCTOBER':
       astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'NOVEMBER':
       astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    print("Your astrological sign is {}.".format(astro_sign))
###
elif option == "ls":
    string_word_value = input("Enter a word: ")
    sorted_string_word = sorted(string_word_value)
    print(sorted_string_word)
###
elif option == "eo":
    number = int(input("Please tell me a number."))
    if number % 2 == 0:
        print("{} is an even number.".format(number))
    else:
        print("{} is an odd number.".format(number))
###
elif option == "ly":
    year = int(input("Enter a year of your choice: "))
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is not a Leap Year")
    elif year % 400 ==0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")
###
elif option == "vc":
    letter = input("Enter a letter of your choice.")
    letter = letter.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print(letter.upper(), "is a Vowel.")
    else:
        print(letter.upper(), "is a Consonant.")
###
elif option == "rn":
    num = int(input("How many random numbers do you want?"))
    operation = input("Do you want them to be whole numbers or decimals?")
    start = int(input("What number is the starting point?"))
    end = int(input("What number is the ending point?"))
    operation = operation.lower()
    for i in range(0,num):
        if operation == "decimals" or operation == "decimal":
            print(random.uniform(start,end))
        else:
            print(random.randint(start,end))
    print("These are your random numbers.")
###
elif option == "sc":
    print("How many years will you be saving?")
    years = int(input("Enter years: "))

    print("How much money is currently in your account?")
    principal = float(input("Enter current amount in account: "))

    print("How much money do you plan on investing monthly?")
    monthly_invest = float(input("Enter amount: "))

    print("What do you estimate will be the yearly interest of this investment?")
    interest = float(input("Enter interest in decimal numbers (10% = 0.1): "))

    print(" ")

    monthly_invest = monthly_invest * 12
    final_amount = 0

    for i in range(0, years):
        if final_amount == 0:
            final_amount = principal
        final_amount = (final_amount + monthly_invest) * (1 + interest)
    fin_final_amount = round(final_amount)
    print("This is how much money you would have in your account after {} years: ".format(years) + str("$") + str(final_amount))
    print("________________________")
    print("This is the rounded amount: {}".format("$") + str(fin_final_amount))
###
elif option == "mr":
    import Macon
    print(Macon.final_restaurant())
