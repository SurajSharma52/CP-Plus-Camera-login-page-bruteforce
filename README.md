# REQUIREMENTS

- Python
- Create your own wordlist if possible

# ABOUT

This tool is designed specifically for the CP PLUS CAMERA login page and works only on Windows systems. It attempts 4 login attempts at a time and changes the MAC address of your device before the login page gets locked. This step also changes your IP address on your router, giving you 5 more attempts. However, it is not very fast compared to other tools. Its speed is approximately 12 words per minute.

This tool is designed for scenarios where the password is strongly encoded by the login page's algorithm before sending the POST request. Therefore, you should use it only for advanced purposes. You can intercept the requests using tools like Burp Suite to check whether the password is encoded or not. If it is encoded, this tool will definitely help you. However, if the password is not encoded before the POST request, I recommend using tools like Hydra or the Burp Suite Interceptor, which can also brute-force login pages effectively.

Future updates of this script will include a powerful wordlist generator and improved speed.

# WARNING 

This tool is only for educational and testing purposes. Do not use
this tool for malesious purposes. This is open source tool so we will
not responsible for anything if you caut darty handed using this tool.

# SET UP

- Install Python latest version https://www.python.org/downloads/
- run PowerShell as Administrator

# RUN THESE COMMANDS ON POWERSHELL

- Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
- Enter "A" and press enter { if asked! }
- python --version
- NAVIGATE TO THE DIRECTORY WHERE YOU DOWNLOAD THIS PROJECT AND RUN THESE COMMANDS

- python3 -m venv env
- cd env\Scripts
- ./activate
- cd ../..
- pip install pyautogui
- pip install pynput

# CHECK THESE PATHS

- PRESS Windows + r
- TYPE regedit
- find folder name HKEY_LOCAL_MACHINE
- find folder name SYSTEM
- find folder name CurrentControlSet
- find folder name Control
- find folder name Class
- find folder name 4D36E972-E325-11CE-BFC1-08002BE10318
- Tap on folder name 0001
- If you can see your wifi adapter name here for eg., 
(Intel(R) Wi-Fi 6E AX211 160MHz), then you can run this script without 
any error

# IF NOT WORKING PROPERLY 

- find correct path of your wifi adapter. And edit the { exploit.py } script and find the line

f"Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001' -Name NetworkAddress -Value {mac_address}"

- add the full path of your adapter folder in place of

{HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001}

# RUNNING SCRIPT

- python exploit.py

