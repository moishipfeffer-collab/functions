from password_data import get_passwords
from password_validation import validate_password
from password_logic import get_password_strength,count_strong_passwords
from password_output import print_password_result,print_skipped_password,print_strong_passwords_count
def run_password_checker():
    passwords = get_passwords()
    valid_passwords = []

    for password in passwords:
        try:
            validate_password(password)

            strength = get_password_strength(password)
            print_password_result(password, strength)

            valid_passwords.append(password)

        except (TypeError, ValueError) as error:
            print_skipped_password(error)

    count = count_strong_passwords(valid_passwords)
    print_strong_passwords_count(count)

run_password_checker()