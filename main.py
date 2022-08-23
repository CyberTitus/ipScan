import requests
from tabulate import tabulate

def IPInfo(IP=""):
	URL = "http://ip-api.com/json/"+IP
	resp = requests.get(URL).json()
	# Display on Screen
	data = [[key.title(), value] for key, value in resp.items()]
	head = ["Key", "Value"]
	print(tabulate(data, headers=head, tablefmt="grid"))

try:
	IP = str(input("Enter IP Address (leave empty to check own IP Info): "))
except KeyboardInterrupt:
	exit(0)

IPInfo(IP)