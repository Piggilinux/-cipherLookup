import sys
import requests
from termcolor import colored
import validators

def main():
	count, count2, count3, count4, count5 = 0, 0, 0, 0, 0
	# Base URL for the ciphersuite.info API
	base_url = "https://ciphersuite.info/api/cs/"
	
	# List of cipher suites to check
	# Check each cipher suite and print the result
	with open(sys.argv[1], 'r') as my_file:
		cipher_suites = my_file.read().splitlines()
		for cs in cipher_suites:
			cs = cs.replace("Cipher Suite: ", "")[:-9]
			
			if cs != "TLS_EMPTY_RENEGOTIATION_INFO_SCSV":
				url = base_url + cs
				response = requests.get(url)
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
					print(cs, colored("recommended", "green"))
					count4 += 1
				else:
					print(cs, colored("unidentified", "magenta"))

	print("")	
	print("insecure: ", count3)
	print("weak: ", count2)
	print("secure: ", count)
	print("recommended: ", count4)
	print("unidentified: ", count5)
 

if __name__ == "__main__":
    main()
