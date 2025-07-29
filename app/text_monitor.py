import keyboard
import win32clipboard, win32con # type: ignore
from app.text_parser import parse_location_text
from app.api_client import fetch_location_data
from PyQt6.QtCore import QObject, pyqtSignal

class TextMonitor(QObject):
    # Сигнал для безпечної передачі даних з фонового потоку в головний (GUI)
    show_popup_signal = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()

    def _get_clipboard_text(self):
        """
        Правильна функція, що надійно читає текстовий вміст буфера обміну через pywin32.
        """
        try:
            win32clipboard.OpenClipboard()
            if win32clipboard.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
                text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
            else:
                text = ""
            win32clipboard.CloseClipboard()
            return text
        except Exception as e:
            print(f"Помилка при читанні буфера обміну: {e}")
            return ""

    def _on_hotkey(self):
        print("Гарячу клавішу натиснуто!")
        clipboard_text = self._get_clipboard_text()

        if clipboard_text and clipboard_text.strip():
            parsed_data = parse_location_text(clipboard_text)
            if parsed_data:
                print(f"Розпізнано: {parsed_data}. Роблю запит до API...")
                api_result = fetch_location_data(parsed_data)
                result_text = api_result if api_result else "Не знайдено"
                self.show_popup_signal.emit(result_text)
            # Якщо текст не розпізнано, нічого не робимо, щоб не заважати користувачу
        else:
            print("В буфері обміну немає тексту.")
    
    def start(self):
        keyboard.add_hotkey('ctrl+alt+s', self._on_hotkey)
        print("Слухач гарячих клавіш (ctrl+alt+s) запущено.")