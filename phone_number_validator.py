import phonenumbers
from phonenumbers import carrier, geocoder
import pycountry

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if phonenumbers.is_valid_number(parsed_number):
            country_code = phonenumbers.region_code_for_number(parsed_number)
            country_name = pycountry.countries.get(alpha_2=country_code).name
            carrier_name = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "en")
            return country_name, carrier_name, location
        else:
            return None, None, None
    except phonenumbers.phonenumberutil.NumberParseException:
        return None, None, None
    except Exception as e:
        print(f"An error occurred while validating the phone number: {e}")
        return None, None, None

try:
    phone_number = input("Enter a phone number to validate: ")
    country, carrier, location = get_phone_info(phone_number)
    if country:
        print(f"{phone_number} is a valid phone number for {country}")
        if carrier:
            print(f"Carrier: {carrier}")
        if location:
            print(f"Location: {location}")
    else:
        print(f"{phone_number} is not a valid phone number")
except pycountry.LookupError:
    print(f"Error: unsupported country code detected in {phone_number}")
except Exception as e:
    print(f"An error occurred: {e}")