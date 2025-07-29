import sys
import os
import threading
from PyQt6.QtWidgets import QApplication

from app.tray_icon import create_tray_icon
from app.text_monitor import TextMonitor
from app.popup_ui import ResultPopup

def resource_path(relative_path):
    """ Отримуємо абсолютний шлях до ресурсу, працює для розробки та для PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Глобальне посилання, щоб вікно не зникало одразу після створення
current_popup = None

def show_popup(text):
    """ Слот, який безпечно створює та показує вікно у головному потоці GUI """
    global current_popup
    current_popup = ResultPopup(text)
    current_popup.show_at_cursor()

def main():
    # 1. Створюємо екземпляр QApplication. Це має бути зроблено в першу чергу.
    app = QApplication(sys.argv)

    # 2. Налаштовуємо фоновий монітор гарячих клавіш
    monitor = TextMonitor()
    # 3. З'єднуємо сигнал з фонового потоку (де працює слухач) зі слотом у головному потоці
    monitor.show_popup_signal.connect(show_popup)
    monitor.start()

    # 4. Знаходимо іконку за допомогою нашої надійної функції
    icon_path = resource_path("assets/icon.png")

    # 5. Запускаємо іконку в треї в окремому потоці, щоб вона не блокувала GUI
    tray_thread = threading.Thread(target=create_tray_icon, args=(icon_path,), daemon=True)
    tray_thread.start()
    
    print("Запуск утиліти Location Lookup...")
    # 6. Запускаємо головний цикл подій PyQt. Це блокуючий виклик.
    sys.exit(app.exec())

if __name__ == "__main__":
    main()