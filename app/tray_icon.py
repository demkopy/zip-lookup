import pystray
from PIL import Image
import sys
import winreg as reg
import os # <-- Додано імпорт

APP_NAME = "LocationLookup"

def add_to_startup(executable_path):
    key = reg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        registry_key = reg.OpenKey(key, key_path, 0, reg.KEY_WRITE)
        reg.SetValueEx(registry_key, APP_NAME, 0, reg.REG_SZ, f'"{executable_path}"')
        reg.CloseKey(registry_key)
    except WindowsError:
        pass

def create_tray_icon(icon_path):
    try:
        image = Image.open(icon_path)
    except FileNotFoundError:
        print(f"Помилка: Файл іконки не знайдено за шляхом {icon_path}")
        return

    def on_quit(icon, item):
        icon.stop()
        os._exit(0) # <-- Додано примусовий вихід з програми

    menu = pystray.Menu(pystray.MenuItem('Вихід', on_quit))
    icon = pystray.Icon(APP_NAME, image, "Location Lookup", menu)

    if getattr(sys, 'frozen', False):
        executable_path = sys.executable
        add_to_startup(executable_path)

    icon.run()