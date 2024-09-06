import subprocess
import time

# تأكد من استبدال هذا بمكتبة VPN المناسبة
try:
    import pyovpn
except ImportError:
    print("pyovpn not found. Install it with `pip install pyovpn`.")
    exit(1)

# إعداد اتصال VPN باستخدام pyovpn
vpn_config = '/home/user/Downloads/USA_freeopenvpn_udp.ovpn'
vpn_client = pyovpn.Client()

# الاتصال بشبكة VPN
print("Connecting to VPN...")
vpn_client.connect(config=vpn_config)

# انتظر حتى يتصل VPN (اضبط الوقت حسب الحاجة)
time.sleep(10)

# تحقق من اتصال VPN
if vpn_client.is_connected():
    print("VPN connected. Starting tmate...")
    
    # تشغيل tmate وعرض النتائج على الشاشة
    with subprocess.Popen(['tmate'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
        for line in process.stdout:
            print(line, end='')  # طباعة كل سطر من الإخراج على الشاشة

else:
    print("Failed to connect to VPN.")
