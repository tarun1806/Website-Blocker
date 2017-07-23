import time
from datetime import datetime as dt

hostpath = r"C:\Windows\System32\drivers\etc\HOSTS"
ip = "127.0.0.1"
websites = ["www.facebook.com","www.twitter.com"]


while True:
    if 16<int(dt.now().strftime("%H"))<18:
        with open(hostpath,"r+") as file:
            content = file.read();

            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(ip +"         "+ website + "\n")
    else:
        with open(hostpath,"r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
    time.sleep(5)
