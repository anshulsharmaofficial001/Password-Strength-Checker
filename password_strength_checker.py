import re


def check_password_strength(password):
     strength=0

     if len(password) >= 8:
         strength += 1
     if re.search("[a-z]" , password):
         strength += 1
     if re.search("[A-Z]" , password):
         strength += 1
     if re.search("[0-9]" , password):
         strength += 1
     if re.search("[!@#$%^&*()_+=-]" , password):
         strength += 1
         
     if (strength <= 2):
          return "weak password"
     elif (strength == 3 or strength == 4):
          return "medium password"
     else:
          return "strong password"


password =input("Enter your password: ")
result = check_password_strength(password)
print(result)
