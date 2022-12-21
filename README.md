# web-scrapper
With the help of this tool you can scrap, both dark websites and normal websites (basically runs on google).

## Web Scrap

CLI based tool for you to scrape .onion websites info on the go.
Tor brower will run in background for extracting the links from onion sites & for normal sites there is no need.

## Installation

Install Tor:

```bash
  kali@kali:~$ sudo apt update
  kali@kali:~$
  kali@kali:~$ sudo apt install -y tor torbrowser-launcher
  kali@kali:~$

```
As user run the following command:

```bash
 kali@kali:~$ torbrowser-launcher
 kali@kali:~$ 
 kali@kali:~$ tor

```
Install Moduals

```bash
 kali@kali:~$ install pip
 kali@kali:~$ 
 kali@kali:~$ pip install art
 kali@kali:~$ pip install beautifulsoup4
 kali@kali:~$ pip install requests

```

Start Tor Service 

```bash
 kali@kali:~$ sudo service tor start
 kali@kali:~$ 
 kali@kali:~$ sudo service tor status
```
Usage

```bash
 kali@kali:~$ python3 scrapper.py

```
