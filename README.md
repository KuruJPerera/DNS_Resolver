Domain/IP Resolver in Python:

This project demonstrates a simple Python script for performing DNS lookups. Using the built-in socket module, the program can convert a domain name to its corresponding IP address, or perform a reverse lookup to find the domain name associated with an IP address.

What is DNS Resolution?

DNS (Domain Name System) is like the phonebook of the internet. It translates human-friendly domain names (e.g., example.com) into machine-friendly IP addresses (e.g., 93.184.216.34). Reverse DNS does the opposite — it takes an IP and returns the associated domain name.

This script showcases how to access DNS resolution features directly in Python using minimal code and standard libraries.

How It Works:

The script offers two options:

Domain to IP: Converts a given domain name into its IP address using socket.gethostbyname().

IP to Domain: Finds the domain name associated with a given IP address using socket.gethostbyaddr().

It prompts the user for input and prints the result to the terminal.

Getting Started: Requirements:

To run this project, you’ll need:

. Python 3 installed on your computer

. A basic code editor or IDE

. An internet connection (for DNS resolution)

. If Python isn’t already installed, download it here:
  https://www.python.org/downloads/

Installation:

Download or clone this repository to your local machine
Open the script file in your preferred code editor

Running the Program:

Run the script

Choose an option when prompted:

. Enter 1 to convert a domain name to an IP address

. Enter 2 to resolve an IP address to a domain name

The program will display the result directly in the terminal
