#-*- coding: utf-8 -*-
import os, sys, requests, threading
from colorama import Fore, init

gl_mc = "\033[1;0m ➲ "
gl_mc1 = "\033[1;0m==> "
init(autoreset=True)

# ================== API CONFIG ==================
CONFIG_URL = "https://raw.githubusercontent.com/Manhcuongdzcuti/Manhcuongdzcuti/refs/heads/main/config.py"

def tai_config():
    try:
        code = requests.get(CONFIG_URL, timeout=5).text
        context = {}
        exec(code, context)  # chạy config.py từ GitHub
        return context.get("TOOL_STATUS", "off"), context.get("UPDATE_MESSAGES", [])
    except Exception as e:
        print(Fore.RED + f"⚠️ Không thể tải config: {e}")
        return "off", []
    
TOOL_STATUS, UPDATE_MESSAGES = tai_config()

# ================== Kiểm tra trạng thái tool ==================
if TOOL_STATUS.lower() != "on":
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
if UPDATE_MESSAGES:
    for idx, msg in enumerate(UPDATE_MESSAGES, start=1):
        print(gl_mc1+f"\033[1;33m {idx}. {msg}")
else:
    print(gl_mc1+f"\033[1;31m Không có thông báo nào.")

print("\033[1;32m\n" + "─" * 60 + "\n")
