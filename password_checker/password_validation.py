from password_data import get_passwords
def validate_password(password):
        if type(password) != str:
            raise TypeError("Password must be a string")
        if len(password) < 1:
            raise ValueError("Password cannot be empty")
  
