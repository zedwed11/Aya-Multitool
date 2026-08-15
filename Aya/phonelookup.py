import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


def run():
    print("Tool Launched....")
    print("-------------------------------")

    phone = input("Enter phone number: ").strip()

    try:
        number = phonenumbers.parse(phone, None)

        if not phonenumbers.is_possible_number(number):
            print("\nInvalid phone number.")
            input("\nPress Enter to exit..")
            return

        print("\n========== PHONE INFORMATION ==========")

        print("\nNumber:")
        print(phonenumbers.format_number(
            number,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        ))

        print("\nCountry Code:")
        print("+" + str(number.country_code))

        print("\nNational Number:")
        print(number.national_number)

        print("\nLocation:")
        print(geocoder.description_for_number(number, "en"))

        print("\nCarrier:")
        print(carrier.name_for_number(number, "en"))

        print("\nTime Zone:")
        print(timezone.time_zones_for_number(number))

        print("\nNumber Type:")
        number_type = phonenumbers.number_type(number)

        types = {
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Landline",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Landline or Mobile",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Toll Free",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumbers.PhoneNumberType.PAGER: "Pager",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
        }

        print(types.get(number_type, "Unknown"))

        print("\nValid Number:")
        print(phonenumbers.is_valid_number(number))

        print("\n========================================")

    except Exception as error:
        print("\nPhone lookup failed..")
        print("Error:", error)

    input("\nPress Enter to exit..")