# 📞 Phone Number Validator

This is a Python script that validates phone numbers entered by users and provides additional information about the phone number, such as the carrier, time zone, and location.
### 🚀 Getting Started

To use this script, you'll need to have Python 3 and the following packages installed:

    phonenumbers
    pycountry

You can install these packages using pip:

pip install phonenumbers pycountry

### 📝 Usage

When you run the script, it will prompt you to enter your country code and phone number. The script will then validate the phone number and provide additional information about the phone number if it is valid.


$ python phone_number_validator.py
Select your country code from the list below:
AD - Andorra
AE - United Arab Emirates
AF - Afghanistan
...
Enter your country code: US
Enter the phone number to validate (including country code): +1 650-253-0000
Phone number validation results:
Parsed phone number: +16502530000
Phone number is valid for user's location: United States
(E.164 format): +16502530000(International format): +1 650-253-0000(National format): (650) 253-0000(RFC3966 format): tel:+1-650-253-## 📚 Explanation of the Code

The code uses the `phonenumbers` library to handle phone numbers, the `pycountry` library to handle country codes, and the Python `input()` function to get user input.

The `get_user_country()` function prompts the user to enter their two-letter country code and returns it. It uses the `pycountry` library to get a list of all country codes.

The `get_phone_number()` function prompts the user to enter a phone number and returns a parsed `phonenumbers` object.

The `validate_phone_number()` function takes a parsed `phonenumbers` object and a country code as input and returns a dictionary of validation results and additional information about the phone number. It uses the `phonenumbers` library to validate the phone number and get additional information about it.

The `print_validation_results()` function takes a parsed `phonenumbers` object, a dictionary of validation results, and a dictionary of additional information as input and prints the validation results and additional information about the phone number.

The `if __name__ == "__main__":` block runs the script and handles errors.

## 🤖 Future Improvements

Some possible improvements to this script could include:

- Adding support for more languages in the `carrier`, `timezone`, and `geocoder` functions.
- Adding support for validating phone numbers with extensions.
- Adding support for validating phone numbers with country codes that are different from the user's country code.
