import string
def has_digit(password):
    return any(char.isdigit() for char in password)
def has_special_char(password):
        return any(char in string.punctuation for char in password)
def get_password_strength(password):
      if len(password) >= 8 and has_special_char(password) and has_digit(password):
            return "strong"
      elif len(password) >= 6 and has_digit(password):
            return "Medium"
      else:
            return "Weak"
def count_strong_passwords(passwords):
    strong_passwords=0
    for password in passwords:
          if get_password_strength(password) == "strong":
                strong_passwords+=1
    return strong_passwords
      
