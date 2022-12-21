import requests
from bs4 import BeautifulSoup
from art import *

tprint("Web Scrapper For All")

def main_function():
	user_input = int(input("Enter '1' to go in onion func or '2' to go in regular func: "))
	if user_input == 1:
		onion_sites()
	elif user_input ==2:
		regular_sites()
		
		
'''
This function Gather information from onion sites.
But firstly you have to set up a tor browser and tor brower should be running in background, 
for this operation.
'''

def onion_sites():
	
	try:
		print("URL should be start from 'http' pr 'https'")
		print("-"*100)

		url1 = input("Enter Onion URL: ")
		if url1.startswith("http") or url1.startswith("https"):
			if url1.endswith("onion") or url1.endswith("/"):
				print("Valid URL")
		else:
			print("Invalid URL")
			
		print("-"*100)
	
		session = requests.session()
		session.proxies["http"] = "socks5h://localhost:9050"
		session.proxies["https"] = "socks5h://localhost:9050"
	
		response = session.get(url1)
		print(response)
#Parse the html page
		soup = BeautifulSoup(response.content, 'html.parser')
		print("[+] Page Title: " ,soup.find('title').string)
		print("-"*100)

		print("You can Scrap`s elements like 'a','p'")

		element = input('Enter the element: ')
		elements = soup.find_all(element)
		print("-"*100)

		for elem in elements:
			if element=='a':
				print(elem.get('href'))
		
			elif element=='p':
# extract text from the webpage
				print(elem.text)
			else:
				print("InfoError")
	except KeyboardInterrupt:
		print("KeyboardInterrupt occurred")
		
	main_function()




'''
Gathering information from Regualr sites.
Regular sites, like that can be open through google browser (normal browser).
'''
	
def regular_sites():
	try:
		print("URL - should be start from 'https' or 'http'")
		url2 = input("Enter Regular URL : ")
		if url2.startswith("http") or url2.startswith("https"):
			if url2.endswith("com") or url2.endswith("/"):
				print("Valid URL")
		else:
			print("Invalid URL")

		print("-"*100)
	
		response = requests.get(url2)
		print(response)

		soup = BeautifulSoup(response.content, 'html.parser')
		print("[+] Page Title: " ,soup.find('title').string)
		print("-"*100)

		print("You can Scrap`s elements like 'a','li','div','span','img','p'")

		print("-"*100)
		print('''
		This code can Scrap all you want to scrap from the website.
		Most Commonly Scrap elements is : 'a' , 'text' ''')
		print("-"*100)

		element = input('Enter the element: ')
		elements = soup.find_all(element)
		print("-"*100)

		for elem in elements:
			if element=='a':
				print(elem.get('href'))
		
			elif element=='img':
				print(elem.get('src'))
		
			elif element=='div':
				print(elem.text)
		
			elif element=='p':
				print(elem.text)
		
		
			elif element=='li':
				print(elem.text)
			else:
				print("InfoError!")
	except KeyboardInterrupt:
		print("KeyboardInterrupt occurred")

main_function()
	
	
