#!/usr/bin/python3
import socket
import sys

def scanHost(ip, startPort, endPort):
    print('[*] Starting TCP port scan on host %s' % ip)

    # Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on host %s complete' % ip)

def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        # Create a new socket

        # socket.AF_UNIX
        # socket.AF_INET
        # socket.AF_INET6

        # socket.SOCK_STREAM =tcp
        # socket.SOCK_DGRAM  =udp
        # socket.SOCK_RAW
        # socket.SOCK_RDM
        # socket.SOCK_SEQPACKET
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        print(ip, port)

        # Print if the port is open
        if not tcp.connect_ex((ip, port)):
            print('[+] %s:%d/TCP Open' % (ip, port))
            tcp.close()

if __name__ == '__main__':
    # Timeout in seconds
    socket.setdefaulttimeout(0.1)

    host   = sys.argv[1]
    startPort = int(sys.argv[2])
    endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(host, startPort, endPort)