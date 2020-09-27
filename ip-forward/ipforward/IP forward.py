import requests
from getpass import getpass
import hashlib
from datetime import datetime
import subprocess
import random
import click

version = 1.5
IP = "sub-ip.bbayugt.xyz"

#check update
try:
    lastver = requests.get("http://" + IP + "/ipforward/ver").text.split()
except:
    print('Update available! please update in github.com/BbayuGt/ip-forward')
    getpass("Press enter to exit")
    exit()
if version < float(lastver[0]):
    if lastver[1] == "1":
        print('Update available! please update in github.com/BbayuGt/ip-forward')
        getpass("Press enter to exit")
        exit()
    else:
        print("The current version is "+str(version)+" However, V"+str(lastver[0])+" is available, update at github.com/BbayuGt/ip-forward")

#info
text = requests.get(f"http://{IP}/ipforward/info").text
if text != "":
    print("Information : \n"+text+"")

#Check UUID
hwid = str(subprocess.check_output('wmic csproduct get IdentifyingNumber, UUID')).split("\\r\\r\\n")[1].split()
hwid = hashlib.sha512(bytes(hwid[0]+ hwid[1] + ".Encrypted.Unhashable.BbayuGt", "utf-8")).hexdigest()
db = requests.get("http://"+IP+"/data.json")
length = len(db.json())
username = None
expdate = None

for x in range(length):
    if hwid in db.json()[list(db.json())[x]]["hwid"]:
        username = list(db.json())[x]
        break

if username is None:
    print("Your account and hwid is not registered.")
    getpass("Press enter to continue")
    exit()

for x in range(len(db.json()[username]["hwid"])):
    if hwid in db.json()[username]["hwid"]:
        expdate = db.json()[username]["expire"][x]
        type_ = db.json()[username]["type"][x]

#get date/time
try:
    timenow = requests.get("http://worldtimeapi.org/api/timezone/Asia/Jakarta")
except requests.ConnectionError:
    print("Oops! Looks like your connection is blocked! i'll let you in, but i will take this information from you")
    print("- Your IP Address")
    print("- Your Current date")
    print("- Your username")
    yes = input("Continue? <y/N> ")
    if yes == "":
        yes = "N"
    if yes.lower() == "n":
        exit()
    elif yes.lower() == "y":
        datepost = datetime.datetime.now()
        datepost = int(datepost.strftime("%Y-%m-%d"))

        post = {
            "date":datepost,
            "username":username
        }

        print("Thank you...")
        requests.post("http://"+IP+"/ipforward/logger.php", headers=post)
    else:
        exit()

timenow = timenow.json()
timenow = timenow['datetime']
timenow = str(datetime.strptime(timenow[0:10], "%Y-%m-%d")).replace("-", "")
timenow = timenow[0:8]

#check is account is expired or not
if int(timenow) > int(expdate):
    if int(expdate) == 0:
        expdate = "Unlimited!"
    else:
        print("This account is expired!")
        getpass('Press enter to exit')
        exit()
elif int(expdate) == int(timenow):
    expdate = "Today!"
    pass
else:
    expdate = str(expdate)
    expdate = str(expdate[:4]) + "/" + str(expdate[4:6]) + "/" + str(expdate[6:]) 

requests.post(f"http://" + IP + "/{username}")
print("Login successfully!")
print("logged in with", username)
print("version :", version)
print("expired :", expdate)
print("Account type :", type_)
if type_ == "pro":
    print("Pro Power granted!")
    print("- Randomized error message!")

ip = input("IP : ")
port = input("PORT : ")
        
httpd = None
if type_ == "pro":
    code = [400, 401, 403, 404, 408, 500, 501, 502, 503]
else:
    code = [200]

try:
    import http.server



    class ServerHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(random.choice(code))
            self.end_headers()

        
        def do_POST(self):
            self.send_response(random.choice(code))
            self.end_headers()
            self.wfile.write(str.encode(f"""server|{ip}\nport|{port}\ntype|1\n#maint|Mainetrance message (Not used for now) -- Growtopia Noobs\n\nbeta_server|{ip}\nbeta_port|{port}\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001"""))


    server_address = ('', 80)
    httpd = http.server.HTTPServer(server_address, ServerHandler)
    print("Connected to", ip)
    httpd.serve_forever()

except:
    print("Port 80 is already used! please close xampp or any other app!")
    getpass("Press enter to continue")
