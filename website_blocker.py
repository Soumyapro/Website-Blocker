import time
from datetime import datetime as dt

hosts_name = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

localhost_ip = "127.0.0.1"

websites_list = ["www.facebook.com", "facebook.com",
                 "www.youtube.com", "youtube.com"]

while True:

    if dt(dt.now().year, dt.now().month, dt.now().day, 22) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):

        print("Working hours.......")
        print("Website Blocked")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:

                    file.write(localhost_ip + " " + website + "\n")

    else:

        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours.....")
        print("Website Unblocked")

    time.sleep(5)
