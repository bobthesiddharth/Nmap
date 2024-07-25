# Nmap

# Nmap Automation Tool

Welcome to the Nmap Automation Tool repository! This tool provides a simple interface to automate network scanning using Nmap, a powerful network scanning tool.

![Nmap Logo](https://nmap.org/images/nmap-header.png)

## Features

- **SYN ACK Scan:** Fast and stealthy scan using SYN ACK packets.
- **UDP Scan:** Scan for open UDP ports on the target.
- **Comprehensive Scan:** In-depth scan using default scripts and comprehensive detection.

## Prerequisites

Before using this tool, ensure you have:

- Python installed (`python3` recommended).
- `nmap` Python library (`python3-nmap`) installed. You can install it using:
  ```bash
  pip install python3-nmap



Usage

    Clone the repository:

    bash

git clone https://github.com/your-username/nmap-automation.git
cd nmap-automation

Run the script:

bash

python nmap_automation.py



  $ python nmap_automation.py

Welcome, this is a simple nmap automation tool
<----------------------------------------------------------->
Please enter the IP address you want to scan: 192.168.1.1
The IP you entered is:  192.168.1.1

Please enter the type of scan you want to Run
1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan 
2
You have selected option:  2
Nmap Version:  7.91
Starting Nmap 7.91 ( https://nmap.org ) at 2024-07-25 15:20 EDT
Nmap scan report for 192.168.1.1
Host is up (0.0026s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE
53/udp  open  domain
68/udp  open  dhcpc
137/udp open  netbios-ns

