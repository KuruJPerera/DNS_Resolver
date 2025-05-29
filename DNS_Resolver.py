import socket  # Import socket module

def resolve_domain(domain_name):
    ip_address = socket.gethostbyname(domain_name)  # Get IP from domain
    print(f"Domain: {domain_name} -> IP: {ip_address}")

def resolve_ip(ip_address):
    domain_name = socket.gethostbyaddr(ip_address)[0]  # Get domain from IP
    print(f"IP: {ip_address} -> Domain: {domain_name}")

# Usage
choice = input("Enter '1' for domain to IP, '2' for IP to domain: ")

if choice == '1':
    resolve_domain(input("Enter domain name: "))

elif choice == '2':
    resolve_ip(input("Enter IP address: "))
