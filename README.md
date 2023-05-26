# 📞 Phone Number Validator

This Python program uses the phonenumbers and pycountry libraries to validate and provide additional information about a phone number entered by the user. The program prompts the user to enter a phone number to validate, and then validates the phone number using the phonenumbers library. If the phone number is valid, the program uses the pycountry library to get the name of the country for the phone number, and uses the phonenumbers.carrier.name_for_number() and phonenumbers.geocoder.description_for_number() functions to get the name of the carrier and the location for the phone number, respectively. The program then prints the validation results and additional information about the phone number if it is valid.
## 📋 Requirements

This program requires the following libraries to be installed:

    phonenumbers: This library provides functions for parsing, formatting, and validating international phone numbers.
    pycountry: This library provides a database of country names and codes based on the ISO 3166 standard.

You can install these libraries using pip by running the following command:

    pip install phonenumbers pycountry


## 🚀 Usage

To use this program, simply run the phone_validator.py script and enter a phone number to validate when prompted. The program will then validate the phone number and print additional informationabout the phone number if it is valid.

    python
    $ python phone_number_validator.py
The program will prompt you to enter a phone number:
    Enter a phone number to validate:
    You can enter any phone number in international format, including the plus symbol (+) at the beginning. For example:

    

    Enter a phone number to validate: +65 8698 3053

    +65 8698 3053 is a valid phone number for Singapore
    Carrier: SingTel
    Location: Singapore

If the phone number is not valid or if an error occurs during the validation process, the program will print an error message instead:

    Enter a phone number to validate: abcdefg
    abcdefg is not a valid phone number 

