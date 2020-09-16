import requests
import time
import os

requests.packages.urllib3.disable_warnings() 

login_url = "https://elga.proman.app/api/login_check"
login_name = "Prisijungimas, skanuokite QR kodą ⮕ "
login_separator = "_"
bad_login = "Netinkamas prisijungimas"
no_user = "Vartotojas nerastas"

scan_operation = "Skanuokite operaciją ⮕ "
scaned = "Nuskanuota"

error = "Klaida"

pause = 3



while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    user_qr_code = input(login_name)


    #test login
    try:
        login_payload = {'username': user_qr_code.split(login_separator)[0],'password':user_qr_code.split(login_separator)[1]}
    except:
        print(bad_login)
        continue


    #login to proman
    try:
        response = requests.request("POST", login_url, data = login_payload, verify=False)
        person = response.json()["person"]
        token = response.json()["token"]
        print()
        print(person["firstName"]+"  " + person["lastName"])
        print()
    except:
        print(no_user)
        continue





    #get operation
    action_url = input(scan_operation)

    action_headers = {
        'Authorization': token
    }

    #send operation
    try:
        response = requests.request("GET", action_url, headers=action_headers, verify=False)
        response.json()["status"]
        print(scaned)
    except:
        print(error)



    time.sleep(pause)



