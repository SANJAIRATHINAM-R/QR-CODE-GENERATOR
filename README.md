
🧾 QR Code Generator (Tkinter GUI)

A simple Python GUI application to generate QR codes instantly using the Tkinter library.
You can enter any text, URL, or data — and it will create a QR code image that you can save as a PNG file.

🚀 Features

🧠 Easy-to-use GUI built with Tkinter

⚡ Generates QR codes instantly using pyqrcode

💾 Allows saving QR codes as .png files

🖼️ Displays the generated QR code inside the app

🔄 Reset button to clear input and preview

🧩 Requirements

Install the following Python libraries before running the app:

pip install pyqrcode pypng Pillow


💡 tkinter is included by default with Python (no need to install).

💻 How to Run

Clone or download this repository.

Open a terminal or command prompt in the project folder.

Run the Python script:

python qrcode_generator.py


Enter text or a URL in the input box.

Click Generate to create the QR code.

Choose a location to save the .png file.

Click Reset to clear and start over.

📸 Screenshot

(You can add a screenshot of your app here)
Example:

![QR Code Generator GUI](screenshot.png)

🛠️ Code Overview
from tkinter import *
import pyqrcode
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


create_code() → Generates and saves QR code

reset() → Clears input and removes displayed image

Tkinter Widgets → Entry, Button, Label for user interaction

📜 License

This project is open-source and free to use under the MIT License.
