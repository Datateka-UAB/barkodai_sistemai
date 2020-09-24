import requests
import time
import os
#import getpass

requests.packages.urllib3.disable_warnings() 

def lt_to_en_keyboard(text):
    lt_eng = {
        "ą":"1",
        "č":"2",
        "ę":"3",
        "ė":"4",
        "į":"5",
        "š":"6",
        "ų":"7",
        "ū":"8",
        "9":"9",
        "ž":"=",    
    }

    for lt in lt_eng:
        text = text.replace(lt, lt_eng[lt])

    return text


if __name__ == "__main__":

    ### 
    login_url = "https://elga.proman.app/api/login_check"
#    login_separator = "EE3ii2joP5"



    login_name = "Prisijungimas, skanuokite QR kodą ⮕ "
    bad_login = "Netinkamas prisijungimas"
    no_user = "Vartotojas nerastas"


    scan_operation = "Skanuokite operaciją ⮕ "
    scaned = "Nuskanuota"
    error = "Klaida"

    pause = 2



    while True:
        time.sleep(pause)
        os.system('cls' if os.name == 'nt' else 'clear')
        #user_qr_code = lt_to_en_keyboard(getpass.getpass(login_name))
        user_token = lt_to_en_keyboard(input(login_name))


        #test login
        try:
            #login_payload = {'username': user_qr_code.split(login_separator)[0],'password':user_qr_code.split(login_separator)[1]}
            login_payload = {'token': user_token}
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
        action_url = lt_to_en_keyboard(input(scan_operation))

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



