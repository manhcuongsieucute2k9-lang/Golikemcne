try:
    from curl_cffi import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    import os
    import sys
    os.system("pip install curl_cffi")
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    gl_mc = "\033[1;0m ➲ "
    gl_mc1 = "\033[1;0m==> "
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            "\033[1;37mC\033[1;36m-\033[1;35mT\033[1;32mO\033[1;31mO\033[1;34mL \033[1;33m- \033[1;36mT\033[1;36mO\033[1;36mO\033[1;31mL \033[1;33mV\033[1;35mI\033[1;33mP",
            "\033[1;33mC\033[1;32m-\033[1;0mT\033[1;34mO\033[1;35mO\033[1;36mL \033[1;33m- \033[1;32mT\033[1;34mO\033[1;35mO\033[1;31mL \033[1;32mV\033[1;34mI\033[1;32mP",
            "\033[1;37mC\033[1;36m-\033[1;35mT\033[1;32mO\033[1;31mO\033[1;34mL \033[1;33m- \033[1;36mT\033[1;36mO\033[1;36mO\033[1;31mL \033[1;33mV\033[1;35mI\033[1;33mP",
            "\033[1;32mC\033[1;31m-\033[1;34mT\033[1;35mO\033[1;32mO\033[1;31mL \033[1;33m- \033[1;33mT\033[1;31mO\033[1;34mO\033[1;32mL \033[1;34mV\033[1;36mI\033[1;31mP",
            "\033[1;37mC\033[1;36m-\033[1;35mT\033[1;32mO\033[1;31mO\033[1;34mL \033[1;33m- \033[1;36mT\033[1;36mO\033[1;36mO\033[1;31mL \033[1;33mV\033[1;35mI\033[1;33mP",
            "\033[1;34mC\033[1;33m-\033[1;33mT\033[1;31mO\033[1;34mO\033[1;35mL \033[1;32m- \033[1;34mT\033[1;35mO\033[1;31mO\033[1;32mL \033[1;35mV\033[1;34mI\033[1;31mP",
            "\033[1;37mC\033[1;36m-\033[1;35mT\033[1;32mO\033[1;31mO\033[1;34mL \033[1;33m- \033[1;36mT\033[1;36mO\033[1;36mO\033[1;31mL \033[1;33mV\033[1;35mI\033[1;33mP",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m            ", end="")
            time.sleep(0.12)
                                  
    print("\r                          \r", end="") 
    print("\033[1;33mĐang Nhận Tiền                        ",end = "\r")

def INSTAGRAM():
    url1_2 = 'https://gateway.golike.net/api/instagram-account'
    resp = ses.get(url1_2, headers=headers).json()

    user_INS = []
    account_id1 = []
    STT = []
    STATUS = []
    i = 1

    for data in resp['data']:
        usernametk = data['instagram_username']
        user_INS.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN + "Hoạt Động" + Fore.RED)
        print(f'\033[1;32m[\033[1;33m{i}\033[1;32m] \033[1;32mTài Khoản\033[1;33m| \033[1;32m: \033[1;33m{usernametk} '
              f'\033[1;33m|\033[1;32m {STATUS[-1]}')
        i += 1

    print('\033[1;32m════════════════════════════════════════════════')
    choose = int(input(gl_mc1+'\033[1;32mNhập Tài Khoản: \033[1;33m'))
    os.system('cls' if os.name== 'nt' else 'clear')
    if 1 <= choose <= len(user_INS):
        user_INS = user_INS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        account_id = account_id1[0]

        checkfile2 = os.path.isfile('COOKIEINS'+str(account_id)+'.txt')
        if checkfile2 == False:
            banner()
            cookieX = input(gl_mc1+'\033[1;32mNhập Cookie Instagram: \033[1;33m')
            with open('COOKIEINS'+str(account_id)+'.txt','w') as f:
                f.write(cookieX)

        with open('COOKIEINS'+str(account_id)+'.txt','r') as f:
            cookieINS = f.read()

        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        so_job = int(input(gl_mc1+'\033[1;32mNhập Số Lượng Job: \033[1;33m'))
        DELAY = int(input(gl_mc1+'\033[1;32mNhập Delay: \033[1;33m'))
        print("\033[1;32m════════════════════════════════════════════════════════════")
        dem = 0
        tong = 0

        headerINS = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookieINS,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
            'x-csrftoken': cookieINS.split('csrftoken=')[1].split(';')[0],
            'x-ig-app-id': '936619743392459',
            'x-requested-with': 'XMLHttpRequest',
        }

        # 🔁 chạy vô hạn cho tới khi cookie die
        while True:
            try:
                job_url = f'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id={account_id}&data=null'
                nos = ses.get(job_url, headers=headers).json()

                if nos.get('status') != 200:
                    print('Không có nhiệm vụ nào',            end='\r')
                    countdown(15)
                    continue

                ads_id = nos['data']['id']
                object_id = nos['data']['object_id']
                job_type = nos['data']['type']

                # Follow job
                if job_type == 'follow':
                    url = f'https://www.instagram.com/api/v1/friendships/create/{object_id}/'
                    data = {'user_id': object_id}
                    response = requests.post(url, headers=headerINS, data=data).text

                # Like job
                elif job_type == 'like':
                    like_id = nos['data']['description']
                    url = f'https://www.instagram.com/api/v1/web/likes/{like_id}/like/'
                    response = requests.post(url, headers=headerINS).text

                # Check cookie die
                if '"checkpoint_required"' in response or '"require_login":true' in response:
                    print(Fore.RED + "⚠️ Cookie Instagram DIE rồi!")
                    os.remove(f'COOKIEINS{account_id}.txt')
                    break

                # Thành công
                if '"status":"ok"' in response:
                    complete_url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                    json_data = {
                        'instagram_account_id': account_id,
                        'instagram_users_advertising_id': ads_id,
                        'async': True,
                        'data': 'null',
                    }
                    time.sleep(2)
                    res2 = requests.post(complete_url, headers=headers, json=json_data).json()

                    if res2.get('success'):
                        dem += 1
                        prices = res2['data']['prices']
                        tong += prices
                        h,m,s = [f"{t:02d}" for t in time.localtime()[3:6]]
                        print(f"\033[1;31m| \033[1;36m{dem} | \033[1;33m{h}:{m}:{s} | "
                              f"\033[1;32msuccess | \033[1;31m{job_type} | "
                              f"\033[1;32m+{prices} | \033[1;33m{tong} vnđ")
                    else:
                        print("                                              ", end="\r")
                        print(Fore.RED+"Job bị skip",end="\r")
                else:
                    print("                                              ", end="\r")
                    print(Fore.RED+"Job thất bại hoặc bị chặn", end="\r")

                countdown(DELAY)

            except Exception as e:
                print("                                              ", end="\r")
                print('\033[1;31mGolike Hết Job', end='\r')
                countdown(10)
                continue

def banner():
    import os
    os.system("cls" if os.name == "nt" else "clear")
    banner_text = """
      \033[1;32m██████\033[1;33m╗         \033[1;32m████████\033[1;33m╗ \033[1;32m██████\033[1;33m╗  \033[1;32m██████\033[1;33m╗ \033[1;32m██\033[1;33m╗
     \033[1;32m██\033[1;33m╔════╝         ╚══\033[1;32m██\033[1;33m╔══╝\033[1;32m██\033[1;33m╔═══\033[1;32m██\033[1;33m╗\033[1;32m██\033[1;33m╔═══\033[1;32m██\033[1;33m╗\033[1;32m██\033[1;33m║
    \033[1;32m ██\033[1;33m║       \033[1;32m█████\033[1;33m╗    \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║
    \033[1;32m ██\033[1;33m║       ╚════╝    \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║
     ╚\033[1;32m██████\033[1;33m╗           \033[1;32m ██\033[1;33m║   ╚\033[1;32m██████\033[1;33m╔╝╚\033[1;32m██████\033[1;33m╔╝\033[1;32m███████\033[1;33m╗
      ╚═════╝            ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝

\033[1;32m════════════════════════════════════════════════════════════
         \033[1;0m            ADMIN INFORMATION
\033[1;32m════════════════════════════════════════════════════════════
\033[1;35mName                :  Cường Lập Trình
\033[1;35mPosition            :  Admin / Lead Developer
\033[1;34mPhone Zalo          :  0859652100
\033[1;0mFacebook Admin      :  https://fb.com/manhcuongutvl.dz
\033[1;32mTools               :  Golike IG Auto Click
\033[1;0mMua Paid Key Tại.   :  https://cardso1vn.x10.mx/add_key.php
\033[1;0mVersion             :  3.2.5
\033[1;32mLink Box Zalo       :  Đang Cập Nhật
\033[1;33mMomo/Mb             :  0859652100(Momo) - 666080629(MB)
\033[1;32m════════════════════════════════════════════════════════════
"""
    print(banner_text)


# ------------------------------------------------------------
# Ở dưới file (main), thay vì viết print(banner_text) thì dùng:0859652100
def LIST():
  os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(gl_mc+'\033[1;32mNhập Authorization Golike: \033[1;33m')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
    import requests

ses = requests.Session()
import random
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; Android 7.0; LG-H920 Build/NRD90C) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/54.0.2474.261 Mobile Safari/601.1",
"android|Mozilla/5.0 (Android; Android 5.0; LG-D722 Build/LRX22G) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/55.0.2275.143 Mobile Safari/602.2",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G928I Build/MMB29K) AppleWebKit/602.37 (KHTML, like Gecko) Chrome/49.0.2276.245 Mobile Safari/535.1",
])
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1, headers=headers).json()
    #user
if checkurl1['status']== 200 :
        import time
        from time import sleep
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        # banner()
        # print(Fore.BLUE + '1.Tool Golike Mobile')
        # choose = int(input(Fore.WHITE + 'Nhập Lựa Chọn : '))
        # if choose == 1 :
        LIST()
        from colorama import Fore, init
        init(autoreset=True)

        username = checkurl1['data']['username']
        coin = checkurl1['data']['coin']
        user_id = checkurl1['data']['id']
        banner()
print(f"{gl_mc}\033[1;32mTài Khoản : \033[1;33m{username}")
print(f"{gl_mc}\033[1;32mTổng Tiền : \033[1;33m{coin}")
print('\033[1;32m════════════════════════════════════════════════')
print(gl_mc + "\033[1;32mNhập [\033[1;33m1\033[1;32m] Để Vào Tool Instagram")
print(gl_mc + "\033[1;32mNhập [\033[1;33m2\033[1;32m] Để Xóa Authorization Hiện Tại")

while True:
    choice = input(gl_mc1 + '\033[1;32mNhập Lựa Chọn: \033[1;33m')
    if choice.isdigit():
        choose = int(choice)
        break
    else:
        print("\033[1;31m[!] Vui lòng nhập số hợp lệ.\033[0m")

if choose == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    username = checkurl1['data']['username']
    coin = checkurl1['data']['coin']
    user_id = checkurl1['data']['id']
    banner()
    print(f"{gl_mc}\033[1;32mTài Khoản : \033[1;33m{username}")
    print(f"{gl_mc}\033[1;32mTổng Tiền : \033[1;33m{coin}")
    print(Fore.RED + '\033[97m════════════════════════════════════════════════')
    INSTAGRAM()

elif choose == 2:
    os.remove('user.txt')

else:
    print(Fore.RED + 'ĐĂNG NHẬP THẤT BẠI')
    os.remove('user.txt')
