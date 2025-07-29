[Українська](#українська) | [English](#english)

<a name="українська"></a>

## 🇺🇦 Location Lookup Utility (Українська)

### Короткий опис проєкту

**Location Lookup Utility** — це легка фонова утиліта для Windows, створена для миттєвого пошуку та форматування адресних даних США. Програма працює у фоновому режимі та активується за допомогою глобальної гарячої клавіші, аналізуючи текст, попередньо скопійований у буфер обміну.

### Основні функції

* **Активація гарячою клавішею:** Запускає пошук за допомогою комбінації `Ctrl+Alt+S`.
* **Гнучке розпізнавання:** Аналізує різноманітні формати даних: поштовий індекс, "Місто, Штат", "Місто Штат Індекс" та інші варіації.
* **Інтеграція з API:** Використовує API [Zippopotam](http://api.zippopotam.us/) для отримання точних даних про місцезнаходження.
* **Спливаюче вікно:** Миттєво відображає результат у невеликому вікні біля курсора.
* **Робота з буфером обміну:** Дозволяє скопіювати фінальний, відформатований результат (`Місто, Штат Індекс`) одним кліком.
* **Робота у фоні:** Запускається разом з Windows і працює через іконку в системному треї.

### Встановлення та Використання

#### Для Користувачів (простий спосіб)

1.  Перейдіть на сторінку **[Releases](https://github.com/denkopy/zip-lookup/releases)** справа на головній сторінці репозиторію.
2.  Завантажте останній файл `LocationLookup.exe`.
3.  Запустіть завантажений файл. Програма з'явиться в системному треї.

#### Для Розробників (якщо ви хочете змінити код)

1.  Клонуйте репозиторій:
    ```bash
    git clone [https://github.com/denkopy/zip-lookup.git](https://github.com/denkopy/zip-lookup.git)
    cd zip-lookup
    ```
2.  Створіть та активуйте віртуальне середовище:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Встановіть залежності:
    ```bash
    pip install -r requirements.txt
    ```
4.  Запустіть програму:
    ```bash
    python main.py
    ```

### Створення `.exe` файлу

Для створення єдиного виконуваного файлу використайте `PyInstaller`:
```bash
pyinstaller --onefile --windowed --add-data "assets/icon.png;assets" --name LocationLookup main.py
````

Готовий файл `LocationLookup.exe` буде знаходитись у теці `dist/`.

### Як користуватися програмою

1.  Запустіть `LocationLookup.exe`. В системному треї з'явиться іконка.
2.  У будь-якій програмі скопіюйте текст, що містить адресу США (`Ctrl+C`).
3.  Натисніть гарячу клавішу **`Ctrl + Alt + S`**.
4.  Біля курсора з'явиться вікно з відформатованим результатом.
5.  Натисніть кнопку "Скопіювати", щоб скопіювати результат.

-----

<a name="english"></a>

## 🇬🇧 Location Lookup Utility (English)

### Short Description

**Location Lookup Utility** is a lightweight background utility for Windows designed for instant searching and formatting of U.S. location data. The program runs in the background and is activated by a global hotkey, analyzing text previously copied to the clipboard.

### Core Features

  * **Hotkey Activation:** Triggers a search using the `Ctrl+Alt+S` combination.
  * **Flexible Parsing:** Analyzes various data formats: ZIP code, "City, State", "City State ZIP", and other variations.
  * **API Integration:** Uses the [Zippopotam](http://api.zippopotam.us/) API to retrieve accurate location data.
  * **Popup Display:** Instantly shows the result in a small window near the cursor.
  * **Clipboard Functionality:** Allows copying the final, formatted result (`City, ST ZIP Code`) with a single click.
  * **Background Operation:** Starts with Windows and runs via a system tray icon.

### Installation & Usage

#### For Users (Simple Way)

1.  Go to the **[Releases](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/denkopy/zip-lookup/releases)** page on the right side of the main repository page.
2.  Download the latest `LocationLookup.exe` file.
3.  Run the downloaded file. The application will appear in your system tray.

#### For Developers (If you want to modify the code)

1.  Clone the repository:
    ```bash
    git clone [https://github.com/denkopy/zip-lookup.git](https://github.com/denkopy/zip-lookup.git)
    cd zip-lookup
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the application:
    ```bash
    python main.py
    ```

### Creating the `.exe` file

To create a single executable file, use `PyInstaller`:

```bash
pyinstaller --onefile --windowed --add-data "assets/icon.png;assets" --name LocationLookup main.py
```

The final `LocationLookup.exe` file will be located in the `dist/` folder.

### How to Use

1.  Run `LocationLookup.exe`. A program icon will appear in the system tray.
2.  In any application, copy a text containing a U.S. location to your clipboard (`Ctrl+C`).
3.  Press the hotkey **`Ctrl + Alt + S`**.
4.  A window with the formatted result will appear near your cursor.
5.  Click the "Скопіювати" (Copy) button to copy the result.

<!-- end list -->

```
```
