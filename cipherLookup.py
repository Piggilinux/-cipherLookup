import sys
import re
import requests
from termcolor import colored

def main():
    count, count2, count3, count4, count5 = 0, 0, 0, 0, 0

    # Base URL for the ciphersuite.info API
    base_url = "https://ciphersuite.info/api/cs/"

    # Read input string from the "ciphers" file
    with open(sys.argv[1], 'r') as file:
        input_string = file.read()

    # Extract cipher strings using regex
    cipher_suites = re.findall(r'TLS_[A-Za-z0-9_]+', input_string)
    unique_cipher = list(set(cipher_suites))

    for cs in unique_cipher:
        url = base_url + cs
        response = requests.get(url)

        # Kontroll om svaret är tomt eller ogiltigt innan JSON-avkodning
        if response.status_code == 200 and response.text:
            try:
                result = response.json()
                if result[cs]['security'] == "secure":
                    print(cs, colored("secure", "green"))
                    count += 1
                elif result[cs]['security'] == "weak":
                    print(cs, colored("weak", "yellow"))
                    count2 += 1
                elif result[cs]['security'] == "insecure":
                    print(cs, colored("insecure", "red"))
                    count3 += 1
                elif result[cs]['security'] == "recommended":
                    print(cs, colored("recommended", "light_green"))
                    count4 += 1
                else:
                    print(cs, colored("unidentified", "magenta"))
            except ValueError as e:
                print(f"Error decoding JSON for {cs}: {e}")
        else:
            print(f"Error fetching data for {cs}")

    print("")    
    print("insecure: ", count3)
    print("weak: ", count2)
    print("secure: ", count)
    print("recommended: ", count4)
    print("unidentified: ", count5)

if __name__ == "__main__":
    main()
