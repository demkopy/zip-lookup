from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt, QTimer

class ResultPopup(QWidget):
    def __init__(self, text_to_display):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("""
            QWidget {
                background-color: #333;
                color: #FFF;
                border-radius: 5px;
                border: 1px solid #555;
                font-family: Segoe UI;
                font-size: 10pt;
                padding: 5px;
            }
            QPushButton {
                background-color: #555;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #777;
            }
        """)

        layout = QHBoxLayout(self)
        self.label = QLabel(text_to_display)
        self.copy_button = QPushButton("Скопіювати")
        
        layout.addWidget(self.label)
        layout.addWidget(self.copy_button)
        
        self.copy_button.clicked.connect(self.copy_and_close)
        QTimer.singleShot(5000, self.close)

    def copy_and_close(self):
        QApplication.clipboard().setText(self.label.text())
        self.close()

    def show_at_cursor(self):
        # --- ЗМІНА ТУТ: Нова логіка позиціонування ---
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        cursor_pos = QCursor.pos()
        window_size = self.sizeHint()

        x = cursor_pos.x() + 10
        y = cursor_pos.y() + 10

        # Перевірка, чи не виходить вікно за правий край екрану
        if x + window_size.width() > screen_geometry.right():
            x = cursor_pos.x() - window_size.width() - 10
        
        # Перевірка, чи не виходить вікно за нижній край екрану
        if y + window_size.height() > screen_geometry.bottom():
            y = cursor_pos.y() - window_size.height() - 10

        self.move(x, y)
        self.show()