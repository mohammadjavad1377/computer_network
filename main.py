import argparse
import socket


def scan_ports(host, start_port, end_port):
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get IP of remote host
    remote_ip = socket.gethostbyname(host)

    # Scan ports
    end_port += 1
    for port in range(start_port, end_port):
        try:
            sock.connect((remote_ip, port))
            print('Port ' + str(port) + ' is open')
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            pass


