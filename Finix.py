import time
from colorama import Fore, Style, init
import json
import os
import socket
import datetime
from datetime import datetime
import subprocess
import re
import requests
import cv2
import webbrowser
from ctypes import wintypes
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
import sys
import psutil
import platform
import qrcode # type: ignore
import ctypes
import calendar

def calend():
    print(Fore.CYAN + f"\n{calendar.month(int(parts[0]), int(parts[1]))}\n")

def download_chatgpt():
    import urllib.request

    url = "https://github.com/ersinuzahbaj-design/DARK-CILIENT-/releases/download/ChatGPT/ChatGpt.exe"
    filename = "ChatGPT.exe"
    path = os.path.join(DOWNLOADS, filename)
    temp_path = path + ".part"

    try:
        start = time.time()
        last_time = start
        last_bytes = 0
        downloaded = 0
        speed = 0

        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=30) as response:
            total = int(response.headers.get("Content-Length") or 0)

            with open(temp_path, "wb") as file:
                while True:
                    chunk = response.read(65536)
                    if not chunk:
                        break

                    file.write(chunk)
                    downloaded += len(chunk)

                    now = time.time()

                    if now - last_time >= 0.5:
                        speed = (downloaded - last_bytes) / (now - last_time)
                        last_bytes = downloaded
                        last_time = now

                    elapsed = int(now - start)
                    minutes, seconds = divmod(elapsed, 60)

                    if total:
                        percent = min(downloaded / total * 100, 100)
                        filled = int(percent / 2)
                        bar = "█" * filled + "░" * (50 - filled)
                        progress = f"{percent:.1f}%"
                    else:
                        bar = "Жүктелуде..."
                        progress = f"{downloaded / 1048576:.1f} MB"

                    speed_text = (
                        f"{speed / 1048576:.2f} MB/s"
                        if speed >= 1048576
                        else f"{speed / 1024:.1f} KB/s"
                    )

                    sys.stdout.write(
                        f"\r[{bar}] {progress} | "
                        f"{minutes:02}:{seconds:02} | {speed_text}   "
                    )
                    sys.stdout.flush()

        os.replace(temp_path, path)
        print()
        os.startfile(path)
        print(Fore.GREEN + f"[+] Claude жүктелді: {path}")

    except Exception:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print("\nЖүктеу қатесі!")

def download_claude():
    import urllib.request

    url = "https://github.com/ersinuzahbaj-design/DARK-CILIENT-/releases/download/v1/claude-org.exe"
    filename = "claude-org.exe"
    path = os.path.join(DOWNLOADS, filename)
    temp_path = path + ".part"

    try:
        start = time.time()
        last_time = start
        last_bytes = 0
        downloaded = 0
        speed = 0

        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=30) as response:
            total = int(response.headers.get("Content-Length") or 0)

            with open(temp_path, "wb") as file:
                while True:
                    chunk = response.read(65536)
                    if not chunk:
                        break

                    file.write(chunk)
                    downloaded += len(chunk)

                    now = time.time()

                    if now - last_time >= 0.5:
                        speed = (downloaded - last_bytes) / (now - last_time)
                        last_bytes = downloaded
                        last_time = now

                    elapsed = int(now - start)
                    minutes, seconds = divmod(elapsed, 60)

                    if total:
                        percent = min(downloaded / total * 100, 100)
                        filled = int(percent / 2)
                        bar = "█" * filled + "░" * (50 - filled)
                        progress = f"{percent:.1f}%"
                    else:
                        bar = "Жүктелуде..."
                        progress = f"{downloaded / 1048576:.1f} MB"

                    speed_text = (
                        f"{speed / 1048576:.2f} MB/s"
                        if speed >= 1048576
                        else f"{speed / 1024:.1f} KB/s"
                    )

                    sys.stdout.write(
                        f"\r[{bar}] {progress} | "
                        f"{minutes:02}:{seconds:02} | {speed_text}   "
                    )
                    sys.stdout.flush()

        os.replace(temp_path, path)
        print()
        os.startfile(path)
        print(Fore.GREEN + f"[+] Claude жүктелді: {path}")

    except Exception:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print("\nЖүктеу қатесі!")

def run_python_file():
    filename = input(Fore.BLUE + "└─$ Python File ~ ")
    if not filename:
        print(Fore.RED + "[-] ERROR: Файл атауы бос!")
        return
    if not filename.lower().endswith(".py"):
        print(Fore.RED + "[-] ERROR: Файл кеңейтімі .py болуы керек!")
        return
    else:
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        full_path = os.path.join(downloads, filename)

        if not os.path.isfile(full_path):
            print(Fore.RED + f"[-] ERROR: {filename} Downloads ішінде табылмады!")
            return

        try:
            subprocess.run(["python", full_path], check=True)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"[-] ERROR: {e}")
        except Exception as e:
            print(Fore.RED + f"[-] ERROR: {e}")


user32 = ctypes.windll.user32

ENUM_CURRENT_SETTINGS = -1
DISP_CHANGE_SUCCESSFUL = 0
DM_DISPLAYFREQUENCY = 0x400000

class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", wintypes.WCHAR * 32),
        ("dmSpecVersion", wintypes.WORD),
        ("dmDriverVersion", wintypes.WORD),
        ("dmSize", wintypes.WORD),
        ("dmDriverExtra", wintypes.WORD),
        ("dmFields", wintypes.DWORD),
        ("dmPositionX", wintypes.LONG),
        ("dmPositionY", wintypes.LONG),
        ("dmDisplayOrientation", wintypes.DWORD),
        ("dmDisplayFixedOutput", wintypes.DWORD),
        ("dmColor", wintypes.SHORT),
        ("dmDuplex", wintypes.SHORT),
        ("dmYResolution", wintypes.SHORT),
        ("dmTTOption", wintypes.SHORT),
        ("dmCollate", wintypes.SHORT),
        ("dmFormName", wintypes.WCHAR * 32),
        ("dmLogPixels", wintypes.WORD),
        ("dmBitsPerPel", wintypes.DWORD),
        ("dmPelsWidth", wintypes.DWORD),
        ("dmPelsHeight", wintypes.DWORD),
        ("dmDisplayFlags", wintypes.DWORD),
        ("dmDisplayFrequency", wintypes.DWORD),
        ("dmICMMethod", wintypes.DWORD),
        ("dmICMIntent", wintypes.DWORD),
        ("dmMediaType", wintypes.DWORD),
        ("dmDitherType", wintypes.DWORD),
        ("dmReserved1", wintypes.DWORD),
        ("dmReserved2", wintypes.DWORD),
        ("dmPanningWidth", wintypes.DWORD),
        ("dmPanningHeight", wintypes.DWORD),
    ]

def get_mode(index):
    mode = DEVMODE()
    mode.dmSize = ctypes.sizeof(DEVMODE)

    if user32.EnumDisplaySettingsW(None, index, ctypes.byref(mode)):
        return mode
    return None

def edhz():
    try:
        current = get_mode(ENUM_CURRENT_SETTINGS)

        if current is None:
            print(Fore.RED + "[-] Display information unavailable")
            return

        supported = set()
        index = 0

        while True:
            mode = get_mode(index)
            if mode is None:
                break

            # Тек ағымдағы ажыратымдылық
            if (mode.dmPelsWidth == current.dmPelsWidth and
                mode.dmPelsHeight == current.dmPelsHeight):
                supported.add(mode.dmDisplayFrequency)

            index += 1

        print(Fore.CYAN + f"[+] CURRENT: {current.dmDisplayFrequency} Hz")
        print(Fore.GREEN + f"[+] SUPPORTED: {sorted(supported)}")

        if len(parts) < 2:
            return

        hz = int(parts[1])

        if hz not in supported:
            print(Fore.RED + "[-] Unsupported refresh rate")
            return

        if hz == current.dmDisplayFrequency:
            print(Fore.YELLOW + "[-] Already using this refresh rate")
            return

        current.dmFields = DM_DISPLAYFREQUENCY
        current.dmDisplayFrequency = hz

        confirm = input(f"Change refresh rate to {hz} Hz? (y/n): ")

        if confirm.lower() != "y":
            print(Fore.YELLOW + "[-] Cancelled")
            return

        result = user32.ChangeDisplaySettingsW(
            ctypes.byref(current), 0
        )

        if result == DISP_CHANGE_SUCCESSFUL:
            print(Fore.GREEN + f"[+] Refresh rate changed: {hz} Hz")
        else:
            print(Fore.RED + f"[-] Windows error code: {result}")

    except ValueError:
        print(Fore.RED + "[-] Enter a valid number")
    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")


def create_qr():
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(downloads, exist_ok=True)
 
    link = input("Finix ~ link: ")
    filename = input("Finix ~ file name: ")

    if not link:
        print("[-] ERROR: Сілтеме бос!")
        return
 
    if not filename.lower().endswith(".png"):
        filename += ".png"
 
    filepath = os.path.join(downloads, filename)
 
    img = qrcode.make(link)
    img.save(filepath)
 
    os.startfile(filepath)
    print(f"QR код сақталды: {filepath}")
 

# Windows Downloads папкасы
DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

def sysinfo():
    try:
        print(Fore.CYAN + "\n========== SYSTEM INFO ==========")

        # WINDOWS
        print(Fore.GREEN + f"WINDOWS: {platform.system()} {platform.release()}")
        print(Fore.GREEN + f"VERSION: {platform.version()}")
        print(Fore.GREEN + f"ARCH: {platform.machine()}")

        # CPU
        cpu = platform.processor()
        print(Fore.YELLOW + f"CPU: {cpu or 'Unknown'}")
        print(Fore.YELLOW + f"CPU CORES: {psutil.cpu_count(logical=False)}")
        print(Fore.YELLOW + f"THREADS: {psutil.cpu_count(logical=True)}")
        print(Fore.YELLOW + f"CPU USAGE: {psutil.cpu_percent(interval=0.5)}%")

        # RAM
        ram = psutil.virtual_memory()
        gb = 1024 ** 3

        print(Fore.MAGENTA + f"RAM TOTAL: {ram.total / gb:.2f} GB")
        print(Fore.MAGENTA + f"RAM AVAILABLE: {ram.available / gb:.2f} GB")
        print(Fore.MAGENTA + f"RAM USAGE: {ram.percent}%")

        # DISK (Windows жүйелік дискі)
        drive = os.environ.get("SystemDrive", "C:") + "\\"
        disk = psutil.disk_usage(drive)

        print(Fore.BLUE + f"DISK TOTAL: {disk.total / gb:.2f} GB")
        print(Fore.BLUE + f"DISK FREE: {disk.free / gb:.2f} GB")
        print(Fore.BLUE + f"DISK USAGE: {disk.percent}%")

        # GPU (Windows PowerShell)
        result = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "(Get-CimInstance Win32_VideoController).Name"
            ],
            capture_output=True,
            text=True,
            errors="replace",
            timeout=10
        )

        gpu = result.stdout.strip()
        print(Fore.CYAN + f"GPU: {gpu or 'Unknown'}")

        # Қосымша ақпарат
        print(Fore.WHITE + f"PC NAME: {platform.node()}")
        print(Fore.WHITE + f"PYTHON: {platform.python_version()}")

        print(Fore.CYAN + "=================================")
        print(Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")

# Windows-та жасырын файлды анықтау
def is_hidden(path):
    attrs = ctypes.windll.kernel32.GetFileAttributesW(str(path))
    return attrs != 0xFFFFFFFF and bool(attrs & 2)

# 1. ls - Барлық көрінетін элементтер
def ls():
    try:
        for name in os.listdir(DOWNLOADS):
            path = os.path.join(DOWNLOADS, name)

            if is_hidden(path):
                continue

            if os.path.isdir(path):
                print(Fore.CYAN + "[DIR] " + name)
            else:
                print(Fore.GREEN + "[FILE] " + name)

    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")

# 2. ls -a - Жасырын элементтерді де көрсету
def ls_a():
    try:
        for name in os.listdir(DOWNLOADS):
            path = os.path.join(DOWNLOADS, name)

            if os.path.isdir(path):
                print(Fore.CYAN + "[DIR] " + name)
            else:
                print(Fore.GREEN + "[FILE] " + name)

    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")

# 3. ls -f - Тек файлдар
def ls_f():
    try:
        for name in os.listdir(DOWNLOADS):
            path = os.path.join(DOWNLOADS, name)

            if os.path.isfile(path) and not is_hidden(path):
                print(Fore.GREEN + "[FILE] " + name)

    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")

# 4. ls -d - Тек папкалар
def ls_d():
    try:
        for name in os.listdir(DOWNLOADS):
            path = os.path.join(DOWNLOADS, name)

            if os.path.isdir(path) and not is_hidden(path):
                print(Fore.CYAN + "[DIR] " + name)

    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")

def camera():
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")

    # Downloads бумасы жоқ болса, жасап қоямыз
    if not os.path.exists(downloads):
        os.makedirs(downloads)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(Fore.RED + "[Қате] Камера табылмады немесе ашылмады")
        return

    print(Fore.CYAN + "Камера ашылды. Enter - суретке түсіру, q - жабу")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(Fore.RED + "[Қате] Кадр оқылмады")
            break

        cv2.imshow("FinixShell Camera", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 13:  # Enter
            filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            full_path = os.path.join(downloads, filename)

            success, encoded_img = cv2.imencode(".png", frame)

            if success:
                with open(full_path, "wb") as f:
                    f.write(encoded_img.tobytes())
                print(Fore.GREEN + f"[+] Сурет сақталды -> {full_path}")
            else:
                print(Fore.RED + "[Қате] Кадрды кодтау сәтсіз болды")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def winfo():
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True, text=True
        )
        output = result.stdout

        ssid = re.search(r"^\s*SSID\s*:\s*(.+)$", output, re.MULTILINE)
        speed = re.search(r"Receive rate \(Mbps\)\s*:\s*(\d+)", output)

        wifi_name = ssid.group(1).strip() if ssid else "Табылмады"
        wifi_speed = speed.group(1) if speed else "Табылмады"

        print(Fore.CYAN + f"[+] WIFI  - {wifi_name}")
        print(Fore.GREEN + f"[+] SPEED - {wifi_speed} MB/S")

    except Exception as e:
        print(Fore.RED + f"[Қате] Wi-Fi ақпаратын алу мүмкін болмады: {e}")

def getip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except Exception as e:
        local_ip = f"Қате: {e}"

    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5).text
    except Exception as e:
        public_ip = f"Қате: {e}"   # <-- нақты қатені көрсетеді

    print(Fore.CYAN + f"[+] Local IP  - {local_ip}")
    print(Fore.GREEN + f"[+] Public IP - {public_ip}")

def ping():
    result = subprocess.run(
        ["ping", "-n", "4", "google.com"],
        capture_output=True, text=True
    )
    output = result.stdout

    sent = re.search(r"Sent = (\d+)", output)
    received = re.search(r"Received = (\d+)", output)
    lost = re.search(r"Lost = (\d+)", output)
    loss = re.search(r"\((\d+)% loss\)", output)
    minimum = re.search(r"Minimum = (\d+)ms", output)
    maximum = re.search(r"Maximum = (\d+)ms", output)
    average = re.search(r"Average = (\d+)ms", output)

    print(Fore.CYAN + "[+] Packets  -")
    print(Fore.GREEN + f"[+] Sent     - {sent.group(1) if sent else '?'}")
    print(Fore.GREEN + f"[+] Received - {received.group(1) if received else '?'}")
    print(Fore.RED + f"[+] Lost     - {lost.group(1) if lost else '?'}")
    print(Fore.YELLOW + f"[+] Loss     - {loss.group(1) if loss else '?'}%")
    print(Fore.CYAN + f"[+] Minimum  - {minimum.group(1) if minimum else '?'}ms")
    print(Fore.CYAN + f"[+] Maximum  - {maximum.group(1) if maximum else '?'}ms")
    print(Fore.CYAN + f"[+] Average  - {average.group(1) if average else '?'}ms")

def save_data():
    data = {
        "files": files,
        "logcat": logcat,
        "log": log,
        "inst": inst
    }
    with open("data.json", "w", encoding="Utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("SAVED DATA")

def load_data():
    global files, logcat, log, inst
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            files = data.get("files", ["Pro.mp4"])
            logcat = data.get("logcat", ["PRO,MP4 = ??"])
            log = data.get("log", ["www.ers.com"])
            inst = data.get("inst", [])

files = []
logcat = []
log = []
inst = []

def matrix():
    yes = input(Fore.GREEN + "└─$ Started Matrx ? ~ ")
    if yes == "yes":
        try:
            while True:
                print("01001010100110010101010101001010011010101010101010101010101010101010010101000101010111001010101001100101010101101010110101010101001010011001010")
                print("11010010110100101010101010100111010100101010101011101001010101101010101001010101010010100101010101011110110101100101001010101110100111010101011")
                print("10101010011010011010010101101010101010101001100101010010101010010101101001010101011001100101111010101010100101010110100110010101111001010111010")
        except KeyboardInterrupt:
            print("\nMATRIX STOPED")
    if yes == "no":
        print("STOPED")
        print("Бастағың келсе: mtrx")

def matrix1():
    inst.append("mtrx")
    loading_bar(label="Downloading Matrix", total=20, delay=0.1)
    mtr = "mtrx"
    inst.append(mtr)

def loading_bar(label="Loading", total=20, delay=0.1):
    for i in range(total + 1):
        percent = int((i / total) * 100)
        filled = "█" * i
        empty = "░" * (total - i)
        sys.stdout.write(f"\r{Fore.CYAN}{label} [{filled}{empty}] {percent}%")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def nwf():
    file = input(Fore.BLUE + "└─$ NewFile ~ ")

    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    full_path = os.path.join(downloads, file)

    if os.path.exists(full_path):
        print(Fore.YELLOW + f"[Ескерту] {file} бұрыннан бар!")
        return

    loading_bar(label="Creating file", total=20, delay=0.08)

    with open(full_path, "w", encoding="utf-8") as f:
        pass   # бос файл жасайды

    print(Fore.GREEN + f"{file} Created -> {full_path}")
    files.append(file)

def edf():
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")

    print(Fore.BLUE + "==============================================")
    print(Fore.BLUE + "DOWNLOADS:")
    all_files = os.listdir(downloads)
    for f in all_files:
        print(" -", f)
    print(Fore.BLUE + "==============================================")

    name = input(Fore.BLUE + "└─$ EditFile ~ ").strip()
    full_path = os.path.join(downloads, name)

    if not os.path.exists(full_path):
        print(Fore.RED + f"[Қате] {name} Downloads ішінде табылмады!")
        return

    allowed_ext = [".txt", ".py", ".html", ".css", ".js", ".json", ".md", ".cpp", ".c"]
    ext = os.path.splitext(name)[1].lower()
    if ext not in allowed_ext:
        print(Fore.RED + f"[Қате] {ext} кеңейтімі қолдау көрсетілмейді.")
        return

    # Ескі мазмұнды көрсету
    with open(full_path, "r", encoding="utf-8") as f:
        old_content = f.read()
    print(Fore.YELLOW + "--- Қазіргі мазмұны ---")
    print(old_content if old_content else "(бос файл)")
    print(Fore.YELLOW + "-----------------------")

    print(Fore.BLUE + "Жаңа мазмұн жазыңыз. Аяқтау үшін жеке жолға :save деп жазыңыз")
    lines = []
    while True:
        line = input()
        if line == ":save":
            break
        lines.append(line)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    if name not in files:
        files.append(name)
    logcat.append(name)
    print(Fore.GREEN + f"{name} өңделді -> {full_path}")

def ins():
    los2 = "ins"
    log.append(los2)

def help():
    print(Fore.RED + "=============================================")
    print("COMMANDS:")
    print("nwf - жаңа файыл жасау")
    print("edf - файылды өңдеу")
    print("ins - кітапханалар жүктеп алу")
    print("cam - камераны ашу жабу үшін")
    print("getip - мекенжайыңызды алу")
    print("winfo - желіңіздің жылдамдығы мен атауы")
    print("ping - серверлермен жылдамдығын тексеру")
    print("=============================================")

def info():
    try:
        filename = " ".join(parts[:-1])
        path = os.path.join(DOWNLOADS, filename)

        if not os.path.isfile(path):
            print(Fore.RED + "[-] Файл табылмады")
            return

        # Файл түрі
        extension = os.path.splitext(filename)[1]

        # Файл көлемі
        size = os.path.getsize(path)

        # Жасалған уақыты
        created = os.path.getctime(path)

        # Өзгертілген уақыты
        modified = os.path.getmtime(path)

        # Уақытты форматтау
        created = datetime.fromtimestamp(created)
        modified = datetime.fromtimestamp(modified)

        print(Fore.GREEN + f"[+] Файл: {filename}")
        print(f"[+] Түрі: {extension or 'Белгісіз'}")
        print(f"[+] Көлемі: {size} байт")
        print(f"[+] Жасалған: {created:%d.%m.%Y %H:%M}")
        print(f"[+] Өзгертілген: {modified:%d.%m.%Y %H:%M}")

    except Exception as e:
        load_data()


def openyt():
    if len(parts) < 3:
        print(Fore.RED + "[-] ERROR: Сілтеме табылмады")
        return

    url = parts[2].strip()

    if url.startswith("https://youtu.be/"):
        print(Fore.LIGHTGREEN_EX + "[+] БҰЛ ЮТУБ СІЛТЕМЕСІ")
        webbrowser.open(url)
    else:
        print(Fore.RED + "[-] ERROR: Бұл YouTube сілтемесі емес")

servers = {}

def hostweb():
    try:
        if len(parts) < 2:
            print(Fore.RED + "[-] Файл атауын енгіз!")
            return

        filename = " ".join(parts[:-1])
        action = parts[-1]

        if action != "-http":
            return

        path = os.path.abspath(os.path.join(DOWNLOADS, filename))

        if os.path.commonpath([DOWNLOADS, path]) != DOWNLOADS:
            print(Fore.RED + "[-] Жарамсыз файл жолы")
            return

        if not os.path.isfile(path) or not filename.lower().endswith(".html"):
            print(Fore.RED + "[-] HTML файлы табылмады")
            return

        # HTTP серверге арналған өңдегіш
        class Handler(SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path.split("?")[0] == "/":
                    self.path = "/" + filename
                super().do_GET()

        handler = partial(Handler, directory=DOWNLOADS)

        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        port = server.server_address[1]

        thread = threading.Thread(
            target=server.serve_forever,
            daemon=True
        )
        thread.start()

        servers[port] = server

        print(Fore.GREEN + "[+] HTTP SERVER STARTED")
        print(Fore.GREEN + f"[+] URL: http://localhost:{port}")
        print(Fore.YELLOW + "[!] Сервер бағдарлама жабылғанша жұмыс істейді")

    except Exception as e:
        print(Fore.RED + f"[-] ERROR: {e}")


def anim_finix():
        print(Fore.BLUE + "███████╗██╗███╗   ██╗██╗██╗  ██╗")
        time.sleep(0.25)
        print(Fore.BLUE + "██╔════╝██║████╗  ██║██║╚██╗██╔╝")
        time.sleep(0.25)
        print(Fore.BLUE + "█████╗  ██║██╔██╗ ██║██║ ╚███╔╝ ")
        time.sleep(0.25)
        print(Fore.BLUE + "██╔══╝  ██║██║╚██╗██║██║ ██╔██╗ ")
        time.sleep(0.25)
        print(Fore.BLUE + "██║     ██║██║ ╚████║██║██╔╝ ██╗")
        time.sleep(0.25)
        print(Fore.BLUE + "╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝")
        time.sleep(0.25)
        print("   F I N I X   T E R M I N A L")

os.system("cls")

acaunts  = []

anim_finix()
loading_bar(label="Loading Data...", total=20, delay=0.1)
loaded = 'loaded data'
load_data()
print(Fore.GREEN + f"[+] {loaded.upper()}")

while True:
    terminal = input(Fore.BLUE + "┌──(" + Fore.LIGHTCYAN_EX + "Finix@Shell" + Fore.BLUE + ")\n" + Fore.BLUE + "└─$ ")
    parts = terminal.split(" ", 2)
    try:
        filename = parts[0]
        action = parts[1]

        if action == "-d":
            path = os.path.join(DOWNLOADS, filename)

            if os.path.isfile(path):
                os.remove(path)
                print("[+] Файл жойылды")
            else:
                print("[-] Файл табылмады")
    except Exception as e:
        load_data()
    try:
        filename = parts[0]
        action = parts[1]

        if action == "-o":
            path = os.path.join(DOWNLOADS, filename)

            if os.path.isfile(path):
                os.startfile(path)
                print(Fore.GREEN + f"[+] Ашылды: {filename}")

    except Exception as e:
        load_data()
    if parts[0] == "web" and parts[1] == "ytv":
        openyt()
    log.append(terminal)
    if terminal == "nwf":
        nwf()
    elif terminal == "edf":
        edf()
    elif terminal == "ins":
        ins()
    elif terminal == "help":
        help()
    elif terminal == "lcat":
        print("==============================================")
        print("LOGTXT:")
        print(logcat)
        print("==============================================")
    elif terminal == "lsy":
        print("==============================================")
        print("LOG STORY:")
        print(log)
        print("==============================================")
    elif terminal == "ins mtrx":
        matrix1()
        inst.append("mtrx")
    elif terminal == "mtrx":
        if "mtrx" in inst:
            for item in inst:
                matrix()
        else:
            print("Алдымен 'ins mtrx' командасын орындаңыз")
    elif terminal == "mtrx -y":
        if "mtrx" in inst:
                    try:
                        while True:
                            print(Fore.LIGHTGREEN_EX + "01001010100110010101010101001010011010101010101010101010101010101010010101000101010111001010101001100101010101101010110101010101001010011001010")
                            print("11010010110100101010101010100111010100101010101011101001010101101010101001010101010010100101010101011110110101100101001010101110100111010101011")
                            print("10101010011010011010010101101010101010101001100101010010101010010101101001010101011001100101111010101010100101010110100110010101111001010111010")
                    except KeyboardInterrupt:
                            print("\nMATRIX STOPED")
        else:
            print("Алдымен 'ins mtrx' командасын орындаңыз")
    elif terminal == "save":
        save_data()
    elif terminal == "getip":
        getip()
    elif terminal == "exit":
        print("STOPED")
        print("=============================================================================================================")
        print("STATUS:","LOGCAT-",logcat,"FILES-",files,"LOG-",log,"INSTALING-",inst)
        print("=============================================================================================================")
        save_data()
        break
    elif terminal == "dtime":
        dtime = datetime.now()
        print("[+] YOUR DATA TIME:", dtime)
    elif terminal == "ping":
        ping()
    elif terminal == "winfo":
        winfo()
    elif terminal == "cls":
        os.system("cls")
        anim_finix()
    elif terminal == "cam":
        camera()
    elif terminal == "about":
        print("Fiix Terminal V 0.0.1 BETA")
        print("Finix Terminal - бұл Windows үшін жасалған командалық жол интерфейсі")
        time.sleep(0.15)
        print("Finix Terminal - бұл Finix Shell-дің бөлігі, ол әртүрлі командаларды орындауға мүмкіндік береді")
        time.sleep(0.25)
        print("Finix Terminal ді жасап шығарған: Ersin ол не бәрі 14 жасында жасады")
        time.sleep(0.3)
        print("Finix for Windows - алдыда Security, Hacking, Programming, Development, Design, and more үшін жаңартулар болады")
    elif terminal == "version":
        print("V 0.0.1 BETA")
    elif terminal == "web yt":
        webbrowser.open("https://www.youtube.com/index")
    elif terminal == "web git":
        webbrowser.open("https://github.com/")
    elif terminal == "web ggl":
        webbrowser.open("https://www.google.com/")
    elif terminal == "web tik":
        webbrowser.open("https://www.tiktok.com/")
    elif terminal == "ls":
        ls()
    elif terminal == "ls -a":
        ls_a()
    elif terminal == "ls -f":
        ls_f()
    elif terminal == "ls -dir":
        ls_d()
    elif terminal == "ins claude":
        download_claude()
    elif len(parts) >= 2 and parts[-1] == "-i":
        info()
    elif len(parts) >= 2 and parts[1] == "-http":
        hostweb()
    elif terminal == "sysinfo":
        sysinfo()
    elif terminal == "makeqr":
        create_qr()
    elif terminal == "infhz":
        edhz()
    elif len(parts) >= 3 and parts[2] == "-cld":
        calend()
    elif terminal == "rpy":
        run_python_file()
    elif terminal == "ins gpt":
        download_chatgpt()
    elif len(parts) >= 2 and parts[1] == "-cki":
        try:
            filename = input(Fore.BLUE + "└─$ Cookie File Name ~ ").strip()
            if not filename.lower().endswith(".json"):
                filename += ".json"
            DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")
            file_path = os.path.join(DOWNLOADS, filename)
            response = requests.get(parts[0], timeout=10)
            requests.message = f"FinixShell - Cookie Downloader"
            response.raise_for_status()
            cookies = response.cookies.get_dict()
            with open(file_path, "w") as f:
                json.dump(cookies, f)
            print(Fore.GREEN + f"[+] Cookies saved to {file_path}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"[-] ERROR: {e}")
    elif len(parts) >= 2 and parts[1] == "-find":
        webbrowser.open(f"https://www.google.com/search?q={parts[0]}")
        print(Fore.GREEN + f"[+] Google search opened for: {parts[0]}")
    elif len(parts) >= 2 and parts[1] == "-findyt":
        webbrowser.open(f"https://www.youtube.com/results?search_query={parts[0]}")
        print(Fore.GREEN + f"[+] YouTube search opened for: {parts[0]}")
    elif len(parts) >= 2 and parts[1] == "-findtt":
        webbrowser.open(f"https://www.tiktok.com/search?q={parts[0]}")
        print(Fore.GREEN + f"[+] TikTok search opened for: {parts[0]}")
    elif len(parts) >= 2 and parts[1] == "-findgit":
        webbrowser.open(f"https://github.com/search?q={parts[0]}")
        print(Fore.GREEN + f"[+] GitHub search opened for: {parts[0]}")
    elif len(parts) >= 2 and parts[1] == "-findyx":
        webbrowser.open(f"https://www.yandex.com/search/?text={parts[0]}")
        print(Fore.GREEN + f"[+] Yandex search opened for: {parts[0]}")
    elif len(parts) >= 2 and parts[1] == "-findddg":
        webbrowser.open(f"https://duckduckgo.com/?q={parts[0]}")
        print(Fore.GREEN + f"[+] DuckDuckGo search opened for: {parts[0]}")

            
