import pytest
from unittest.mock import MagicMock

# Додаємо шлях до src, щоб можна було імпортувати app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.tray_icon import create_tray_icon

def test_create_tray_icon_calls(mocker):
    """
    Тестує, що функція створення іконки викликає необхідні методи бібліотеки pystray.
    Використовує pytest-mock (mocker).
    """
    # Мокаємо (імітуємо) системні виклики, щоб не створювати реальну іконку
    mocker.patch('PIL.Image.open', return_value=MagicMock())
    mock_icon_constructor = mocker.patch('pystray.Icon')

    # Викликаємо нашу функцію
    create_tray_icon("dummy_path/icon.png")

    # Перевіряємо, що конструктор іконки був викликаний один раз
    mock_icon_constructor.assert_called_once()
    
    # Перевіряємо, що був викликаний метод .run() для запуску іконки
    mock_icon_constructor.return_value.run.assert_called_once()