import socket
import requests
import socks

def connect_to_proxy():
    proxy_server = input("Enter proxy server): ")
    proxy_port = input("Enter proxy port: ")
    url = input("Enter website URL: ")

    socks.set_default_proxy(socks.SOCKS5, proxy_server, int(proxy_port))
    socket.socket = socks.socksocket

    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

connect_to_proxy()
