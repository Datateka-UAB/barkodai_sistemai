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



    scan_string = "\n Skanuokite QR kodą arba pridėkite prisijungimo kortelę ⮕ "
    bad_login = "\n Netinkamas prisijungimas"
    no_user = "\n Vartotojas nerastas"


    scaned = "\n Nuskanuota"
    error = "\n Klaida"

    pause = 2




    login = False


    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        #user_qr_code = lt_to_en_keyboard(getpass.getpass(login_name))
        if login:
            print("\n " + person["name"])
        scan_code = lt_to_en_keyboard(input(scan_string))


        #test login
        if login == False or "http" not in scan_code:
            #test login
            try:
                #login_payload = {'username': user_qr_code.split(login_separator)[0],'password':user_qr_code.split(login_separator)[1]}
                login_payload = {'token': scan_code}
            except:
                print(bad_login)
                time.sleep(pause)
                continue

            #login to proman
            try:
                response = requests.request("POST", login_url, data = login_payload, verify=False)
                person = response.json()["person"]
                token = response.json()["token"]
                login = True #set login  to true
                print()
                print(person["name"])
                print()
            except:
                print(no_user)
                time.sleep(pause)
                continue




        else:

            action_headers = {
                'Authorization': token
            }

            #send operation
            try:
                response = requests.request("GET", scan_code, headers=action_headers, verify=False)
                response.json()["status"]
                print(scaned)
            except:
                print(error)
                time.sleep(pause)



