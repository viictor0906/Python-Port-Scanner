import socket
import pyfiglet
import threading

ascii_banner=pyfiglet.figlet_format("PORT SCANNER!")
print(ascii_banner)

host=input("Wich host do you want to scan?: ")
while True:
    try:
        portLimit=int(input("How many ports do you want to scan?: "))
        break
    except ValueError:
        print("Please enter a valid number.")

def scanPort(host,port):
    s=socket.socket()
    ip=socket.gethostbyname(host)
    s.settimeout(0.5)
    try:
        s.connect((ip,port))
        print(f"Port {port} is OPEN!")
    except:
        print(f"Port {port} is CLOSED or FILTERED!")
    finally:
        s.close()

def threadScanner(host,portLimit):
    threads=[]
    for port in range(1,portLimit+1):
        t=threading.Thread(target=scanPort,args=(host,port))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def portScanner(host,portLimit):
    #Setting host to valid ip address.
    ip=socket.gethostbyname(host)

    #Work.
    for i in range(1,portLimit+1):
        s=socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((ip,i))
            print(f"Port {i} is OPEN!")
        except:
            print(f"Port {i} is CLOSED or FILTERED.")
        finally:
            s.close()

#portScanner(host,portLimit)
threadScanner(host,portLimit)
