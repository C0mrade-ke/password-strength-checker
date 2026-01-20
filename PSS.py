

import re
import time


RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
PURPLE = "\033[95m"
RESET = "\033[0m"




print(PURPLE+ r"""
                                                         
  
ppppp   ppppppppp       ssssssssss       cccccccccccccccc
p::::ppp:::::::::p    ss::::::::::s    cc:::::::::::::::c
p:::::::::::::::::p ss:::::::::::::s  c:::::::::::::::::c
pp::::::ppppp::::::ps::::::ssss:::::sc:::::::cccccc:::::c
 p:::::p     p:::::p s:::::s  ssssss c::::::c     ccccccc
 p:::::p     p:::::p   s::::::s      c:::::c             
 p:::::p     p:::::p      s::::::s   c:::::c             
 p:::::p    p::::::pssssss   s:::::s c::::::c     ccccccc
 p:::::ppppp:::::::ps:::::ssss::::::sc:::::::cccccc:::::c
 p::::::::::::::::p s::::::::::::::s  c:::::::::::::::::c
 p::::::::::::::pp   s:::::::::::ss    cc:::::::::::::::c
 p::::::pppppppp      sssssssssss        cccccccccccccccc
 p:::::p                                                 
 p:::::p                                                 
p:::::::p                                                
p:::::::p                                                
p:::::::p                                                
ppppppppp                                                
                                                         
𝒑𝒂𝒔𝒔𝒘𝒐𝒓𝒅 𝒔𝒕𝒓𝒆𝒏𝒈𝒕𝒉 𝒄𝒉𝒆𝒄𝒌𝒆𝒓
                                                        ａｕｔｈｏｒ Ｃ０ｍｒａｄｅ
 """ + RESET)
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return (
            RED + "weak password" + RESET,
            RED + "Suggestion: Use uppercase, lowercase, numbers, and symbols. Length ≥ 8." + RESET
        )
    elif score == 3:
        return (
            YELLOW + "Medium password" + RESET,
            YELLOW + "Tip: Add symbols and more characters to make it stronger." + RESET
        )
    elif score == 4:
        return (
            GREEN + "strong password" + RESET,
            GREEN + "Could take weeks to finally crack it." + RESET
        )
    else:
        return (
            PURPLE + "Very strong password" + RESET,
            PURPLE + "Could take months or years to crack. Elite level!" + RESET
        )

while True:
    print("\n" + PURPLE + "=== C0mrade Password Analyzer ===" + RESET)
    print("1 Test a password")
    print("99 Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        password = input("\nEnter a password to check: ")
        result, comment = check_password_strength(password)
        print(f"\nResult: {result}")
        print(comment)
        time.sleep(1)
    elif choice == "99":
        print("\n" + PURPLE + "Exiting... Stay secure, C0mrade" + RESET)
        break
    else:
        print("\n" + RED + "Invalid option. Pick 1 or 99." + RESET)
