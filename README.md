
# Domain/IP Resolver in Python

This project demonstrates a simple Python script for performing DNS lookups. Using Python's built-in `socket` module, the program can convert a domain name to its corresponding IP address, or perform a reverse lookup to find the domain name associated with an IP address.

---

## What is DNS Resolution?

DNS (Domain Name System) is like the phonebook of the internet. It translates human-friendly domain names (e.g., `example.com`) into machine-friendly IP addresses (e.g., `93.184.216.34`).  
Reverse DNS does the opposite — it takes an IP and returns the associated domain name.

This script showcases how to access DNS resolution features directly in Python using minimal code and standard libraries.

---

## How It Works

The script offers two options:

- **Domain to IP**: Converts a given domain name into its IP address using `socket.gethostbyname()`.
- **IP to Domain**: Finds the domain name associated with a given IP address using `socket.gethostbyaddr()`.

The user selects an option and enters the input when prompted. The result is displayed in the terminal.

---

## Getting Started

### Requirements

- Python 3 installed  
- Basic terminal or code editor  
- An internet connection (for DNS resolution)

If Python is not installed, download it here:  
https://www.python.org/downloads/

---

## Installation

1. Clone or download the script  
2. No additional packages are required — uses Python's standard library

---

## Running the Program

1. Open a terminal  
2. Run the script:
   ```bash
   python domain_ip_resolver.py
   ```

3. Choose an option when prompted:
   - Enter `1` to convert a domain name to an IP address
   - Enter `2` to resolve an IP address to a domain name

4. View the result in the terminal

---

## Example Usage

```
Enter '1' for domain to IP, '2' for IP to domain: 1
Enter domain name: example.com
Domain: example.com -> IP: 93.184.216.34
```

```
Enter '1' for domain to IP, '2' for IP to domain: 2
Enter IP address: 93.184.216.34
IP: 93.184.216.34 -> Domain: example.com
```

---

## Notes

- This script depends on your network and DNS server configuration for accuracy.
- Some IP addresses may not have reverse DNS records and could raise exceptions.
