import whois


def run():
    print("Tool Launched....")
    print("--------------------------------")

    domain = input("Enter domain: ").strip()

    if not domain:
        print("You didn't enter a domain retard")
        input("\nPress Enter to exit..")
        return

    try:
        information = whois.whois(domain)

        print("\n========================================")
        print("           WHOIS INFORMATION")
        print("========================================")

        print("\n[ DOMAIN ]")
        print("----------------------------------------")
        print("Domain Name:      ", information.domain_name)
        print("Registrar:        ", information.registrar)
        print("WHOIS Server:     ", information.whois_server)
        print("Registry Domain:  ", information.registry_domain_id)

        print("\n[ DATES ]")
        print("----------------------------------------")
        print("Created:          ", information.creation_date)
        print("Updated:          ", information.updated_date)
        print("Expires:          ", information.expiration_date)

        print("\n[ STATUS ]")
        print("----------------------------------------")
        print("Domain Status:    ", information.status)

        print("\n[ NAME SERVERS ]")
        print("----------------------------------------")
        print(information.name_servers)

        print("\n[ REGISTRANT ]")
        print("----------------------------------------")
        print("Name:             ", information.name)
        print("Organization:     ", information.org)
        print("Email:            ", information.emails)
        print("Phone:            ", information.phone)
        print("Address:          ", information.address)
        print("City:             ", information.city)
        print("State:            ", information.state)
        print("Country:          ", information.country)
        print("ZIP:              ", information.zipcode)

        print("\n[ ADMINISTRATIVE CONTACT ]")
        print("----------------------------------------")
        print("Name:             ", information.admin_name)
        print("Organization:     ", information.admin_organization)
        print("Email:            ", information.admin_email)
        print("Phone:            ", information.admin_phone)

        print("\n[ TECHNICAL CONTACT ]")
        print("----------------------------------------")
        print("Name:             ", information.tech_name)
        print("Organization:     ", information.tech_organization)
        print("Email:            ", information.tech_email)
        print("Phone:            ", information.tech_phone)

        print("\n========================================")
        print("        WHOIS LOOKUP COMPLETE")
        print("========================================")

    except Exception as error:
        print("\nWHOIS lookup failed..")
        print("Error:", error)

    input("\nPress Enter to exit..")