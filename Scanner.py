import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\n Please enter the type of scan you want to Run
             1) SYN ACK Scan
             2) UDP Scan
             3) Comprehensive Scan \n""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr]:
        print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
    else:
        print("No open TCP ports found")
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'udp' in scanner[ip_addr]:
        print("Open Ports: ", list(scanner[ip_addr]['udp'].keys()))
    else:
        print("No open UDP ports found")
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sC')
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr]:
        print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
    else:
        print("No open TCP ports found")
else:
    print("Invalid option. Please select a valid scan type (1, 2, or 3)")
