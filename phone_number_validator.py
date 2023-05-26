import phonenumbers
from phonenumbers import carrier, timezone, geocoder
import pycountry




def get_user_country():
    """
    Prompts the user to enter their two-letter country code from a list of all country codes.
    Returns the user's country code.
    """
    all_country_codes = [country.alpha_2 for country in pycountry.countries]
    while True:
        print("Select your country code from the list below:")
        for country_code in all_country_codes:
            print(f"{country_code} - {pycountry.countries.get(alpha_2=country_code).name}")
        user_country = input("Enter your country code: ").strip().upper()
        if user_country in all_country_codes:
            return user_country
        else:
            print("Invalid country code. Please try again.")



def get_phone_number():
    """
    Prompts the user to enter a phone number to validate.
    Returns the phone number.
    """
    while True:
        phone_number = input("Enter the phone number to validate (including country code): ").strip()
        try:
            parsed_number = phonenumbers.parse(phone_number)
            return parsed_number
        except phonenumbers.phonenumberutil.NumberParseException:
            print("Invalid phone number. Please try again.")



def validate_phone_number(parsed_number, user_country):
    """
    Validates the phone number for the given user country code.
    Returns a tuple of validation results and additional information about the phone number.
    """
    is_possible = phonenumbers.is_possible_number(parsed_number)
    parsed_number_with = phonenumbers.parse(phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164), user_country)
    is_valid_4_region = phonenumbers.is_valid_number_for_region(parsed_number_with, user_country)
    validation_results = {
        "is_possible": is_possible,
        "is_valid_4_region": is_valid_4_region
    }
    additional_info = {}
    if is_valid_4_region:
        additional_info["country"] = pycountry.countries.get(alpha_2=user_country).name
        additional_info["carrier"] = carrier.name_for_number(parsed_number_with, "en")
        additional_info["time_zone"] = timezone.time_zones_for_number(parsed_number_with)
        additional_info["location"] = geocoder.description_for_number(parsed_number_with, 'en')
    return validation_results, additional_info




def print_validation_results(parsed_number, validation_results, additional_info):
    """
    Prints the validation results and additional information about the phone number.
    """
    print("Phone number validation results:")
    print(parsed_number)
    if validation_results["is_possible"]:
        if validation_results["is_valid_4_region"]:
            print(f"Phone number is valid for user's location: {additional_info['country']}")

            # Print different formats of the phone number
            print("All possible formats: ")
            print(f"(E.164 format): {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
            print(f"(International format): {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            print(f"(National format): {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")
            print(f"(RFC3966 format): {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.RFC3966)}")

            # Print additional information about the phone number
            print(f"Carrier (TSP): {additional_info['carrier']}")
            print(f"Time zone: {additional_info['time_zone']}")
            print(f"Location: {additional_info['location']}")
        else:
            print(f"Currently, phone number is invalid for user's location, which is {pycountry.countries.get(alpha_2=user_country).name}")
    else:
        print(f"Phone number {parsed_number} is not possible")
        print(f"The format of phone numbers for {pycountry.countries.get(alpha_2=user_country).name} is {phonenumbers.country_code_for_region(user_country.upper())}### ### ###")





if __name__ == "__main__":
    try:
        user_country = get_user_country()
        parsed_number = get_phone_number()
        validation_results, additional_info = validate_phone_number(parsed_number, user_country)
        print_validation_results(parsed_number, validation_results, additional_info)
    except pycountry.LookupError:
        print("Error looking up country code. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")