import pytest
from unittest.mock import MagicMock

# Додаємо шлях до src, щоб можна було імпортувати app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.text_monitor import TextMonitor

# --- ЗМІНА ТУТ: Перейменовуємо тести для ясності ---
def test_get_clipboard_text_success(mocker):
    """
    Тестує успішний сценарій, коли в буфері є текст.
    """
    mocker.patch('win32clipboard.OpenClipboard')
    mocker.patch('win32clipboard.CloseClipboard')
    mocker.patch('win32clipboard.IsClipboardFormatAvailable', return_value=True)
    mocker.patch('win32clipboard.GetClipboardData', return_value='очікуваний текст')

    monitor = TextMonitor()
    # --- ЗМІНА ТУТ: Викликаємо правильну функцію ---
    result = monitor._get_clipboard_text()

    assert result == 'очікуваний текст'

def test_get_clipboard_text_is_empty(mocker):
    """
    Тестує сценарій, коли в буфері обміну немає тексту.
    """
    mocker.patch('win32clipboard.OpenClipboard')
    mocker.patch('win32clipboard.CloseClipboard')
    mocker.patch('win32clipboard.IsClipboardFormatAvailable', return_value=False)
    
    monitor = TextMonitor()
    # --- ЗМІНА ТУТ: Викликаємо правильну функцію ---
    result = monitor._get_clipboard_text()

    assert result == ''