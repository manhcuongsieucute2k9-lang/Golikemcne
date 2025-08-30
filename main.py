#-*- coding: utf-8 -*-
import os, sys, socket, time, requests, threading
from colorama import Fore, init
import config
gl_mc = "\033[1;0m ➲ "
gl_mc1 = "\033[1;0m==> "
init(autoreset=True)

# ================== Kiểm tra & giám sát mạng ==================
def lay_ip_hien_tai():
    try:
        return requests.get("https://api64.ipify.org", timeout=5).text.strip()
    except:
        return None

def kiem_tra_mang():
    ip = lay_ip_hien_tai()
    if not ip:
        print(Fore.RED + "❌ Không có kết nối mạng. Thoát tool.")
        sys.exit()
    return ip

def giam_sat_mang(ip_bandau):
    while True:
        time.sleep(5)  # kiểm tra mỗi 5 giây
        ip_hientai = lay_ip_hien_tai()
        if not ip_hientai:
            print(Fore.RED + "\n❌ Mạng bị mất kết nối. Tool sẽ thoát.")
            os._exit(0)
        if ip_hientai != ip_bandau:
            print(Fore.RED + f"\n⚠️ Mạng đã thay đổi (IP mới: {ip_hientai}). Tool sẽ thoát.")
            os._exit(0)

# ================== Kiểm tra trạng thái tool ==================
if config.TOOL_STATUS.lower() != "on":
    print(Fore.RED + "🔧 Tool đang bảo trì, vui lòng quay lại sau.")
    sys.exit()

# ================== Banner tool ==================
banner = f"""
      \033[1;32m██████\033[1;33m╗         \033[1;32m████████\033[1;33m╗ \033[1;32m██████\033[1;33m╗  \033[1;32m██████\033[1;33m╗ \033[1;32m██\033[1;33m╗
     \033[1;32m██\033[1;33m╔════╝         ╚══\033[1;32m██\033[1;33m╔══╝\033[1;32m██\033[1;33m╔═══\033[1;32m██\033[1;33m╗\033[1;32m██\033[1;33m╔═══\033[1;32m██\033[1;33m╗\033[1;32m██\033[1;33m║
    \033[1;32m ██\033[1;33m║       \033[1;32m█████\033[1;33m╗    \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║
    \033[1;32m ██\033[1;33m║       ╚════╝    \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║   \033[1;32m██\033[1;33m║\033[1;32m██\033[1;33m║
     ╚\033[1;32m██████\033[1;33m╗           \033[1;32m ██\033[1;33m║   ╚\033[1;32m██████\033[1;33m╔╝╚\033[1;32m██████\033[1;33m╔╝\033[1;32m███████\033[1;33m╗
      ╚═════╝            ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝\n
\033[1;32m════════════════════════════════════════════════════════════
         \033[1;0m            ADMIN INFORMATION
\033[1;32m════════════════════════════════════════════════════════════
\033[1;35mName                :  Cường Lập Trình
\033[1;35mPosition            :  Admin / Lead Developer
\033[1;34mPhone Zalo          :  0859652100
\033[1;0mFacebook Admin      :  https://fb.com/manhcuongutvl.dz
\033[1;32mTools               :  Gộp Golike Vip
\033[1;0mMua Paid Key Tại.   :  https://cardso1vn.x10.mx/add_key.php
\033[1;0mVersion             :  3.2.5
\033[1;32mLink Box Zalo       :  Đang Cập Nhật
\033[1;33mMomo/Mb             :  0859652100(Momo) - 666080629(MB)
\033[1;32m════════════════════════════════════════════════════════════
\033[1;32m════════════════════════════════════════════════════════════
                 TOOL GOLIKE - MULTI JOB
════════════════════════════════════════════════════════════
"""
os.system('cls' if os.name== 'nt' else 'clear')
print(banner)
# ================== Thông báo từ Admin ==================
print(gl_mc1+"\033[1;32m📢 THÔNG BÁO TỪ ADMIN")
for idx, msg in enumerate(config.UPDATE_MESSAGES, start=1):
    print(gl_mc1+f"\033[1;33m {idx}. {msg}")

print("\033[1;32m\n" + "─" * 60 + "\n")  # Ngăn cách giữa thông báo và menu

# ================== Menu tool ==================
TOOLS_URL = {
    "1": "https://raw.githubusercontent.com/manhcuongsieucute2k9-lang/Golikemcne/refs/heads/main/Golikesnap.py",
    "2": "https://raw.githubusercontent.com/manhcuongsieucute2k9-lang/Golikemcne/refs/heads/main/GolikeIg.py",
    "3": "https://raw.githubusercontent.com/manhcuongsieucute2k9-lang/Golikemcne/refs/heads/main/Golikex.py",
    "4": "https://raw.githubusercontent.com/manhcuongsieucute2k9-lang/Golikemcne/refs/heads/main/Golikeblue.py",
    "5": "https://raw.githubusercontent.com/manhcuongsieucute2k9-lang/Golikemcne/refs/heads/main/Golikelimkedin.py",
    "6": "https://raw.githubusercontent.com/manhcuongsieucute2k9-lang/Golikemcne/refs/heads/main/GolikeTik.py",
}

print("\033[1;32m╔═════════════════════════╗")
print("\033[1;32m║ \033[1;33mTOOL GOLIKE - MULTI JOB \033[1;32m║")
print("\033[1;32m╚═════════════════════════╝")
print(gl_mc+"\033[1;32mNhập [\033[1;33m1\033[1;32m] Tool Golike Snapchat \033[1;33m(Auto Click + ADB)")
print(gl_mc+"\033[1;32mNhập [\033[1;33m2\033[1;32m] Tool Golike Instagram \033[1;33m(Auto Làm Job)")
print(gl_mc+"\033[1;32mNhập [\033[1;33m3\033[1;32m] Tool Golike X / Twitter \033[1;33m(Auto Làm Job)")
print(gl_mc+"\033[1;32mNhập [\033[1;33m4\033[1;32m] Tool Golike Bluesky \033[1;33m(Auto Click)")
print(gl_mc+"\033[1;32mNhập [\033[1;33m5\033[1;32m] Tool Golike LinkedIn \033[1;33m(Auto Làm Job)")
print(gl_mc+"\033[1;32mNhập [\033[1;33m6\033[1;32m] Tool Golike Tiktok \033[1;33m(Auto Click + Adb)")
print(gl_mc+"\033[1;32mNhập [\033[1;33m0\033[1;32m] Thoát")

# ================== Nhập lựa chọn (while nếu sai) ==================
while True:
    print("\033[1;32m═══════════════════")
    choice = input(gl_mc1+"\033[1;32mNhập Lựa Chọn: \033[1;33m")
    if choice in ["0","1","2","3","4","5","6"]:
        break
    print("\033[1;31mLựa chọn không hợp lệ. Vui lòng nhập lại.")

# ================== Lưu IP ban đầu & bật giám sát mạng ==================
ip_bandau = kiem_tra_mang()
threading.Thread(target=giam_sat_mang, args=(ip_bandau,), daemon=True).start()

# ================== Xử lý lựa chọn ==================
if choice == "0":
    print("\033[1;31mThoát tool.")
    sys.exit()
else:
    print("\033[1;0mĐang tải tool...")
try:
    code = requests.get(TOOLS_URL[choice], timeout=10).text

    # Lọc bỏ những dòng in "TrinhCoder"
    blacklist = ["TrinhCoder"]
    clean_code = "\n".join(
        line for line in code.splitlines()
        if not any(bad in line for bad in blacklist)
    )

    exec(clean_code, globals())
except Exception as e:
    print(f"\033[1;31mLỗi tải tool: {e}")
    sys.exit()
