############################  REQUIREMENTS  ###########################

# Python
# Create Your Own Password Wordlist

###########################  WARNING  ################################

This tool is only for educational and testing purposes. Do not use
this tool for malesious purposes. This is open source tool so we will
not responsible for anything if you caut darty handed using this tool.

-------------------------------ABOUT-----------------------------------

This tool is designed according to [CP PLUS CAMERA] login page and only 
work in Windows System. This tool attempt 4 login at once and changes
the MacAddress of your device before locking the login page. This step
changes your IP Address in your router. So you will get 5 more attempts.
And it is not vary fast like other tools. It's speed is approx 12 words 
per minute. It is designed only for those scenarios where password is 
[strongly encoded] by algorithms by Login page, before sending the POST 
request. That's way you should use it only for advanced perposes. You
can intersept the requests using tools like [burpsuit] and check wether 
the password is encoded or not. If yes then this tool Definitely helps 
you. If password is not encoded before POST request then I recommend 
you to use [hydra] and second one is [burpsuit intersepter], which 
can also bruteforce login pages. update of version of this script 
contain powerful wordlist maker and speed will also be increased.

------------------------------SET UP-----------------------------------

1. Install Python latest version https://www.python.org/downloads/
2. run PowerShell as Administrator

-----------------RUN THESE COMMANDS ON POWERSHELL-----------------------

3. Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# Enter y and press enter [if asked!]
4. python --version

--------NAVIGATE TO THE DIRECTORY WHERE YOU DOWNLOAD THIS PROJECT--------- 

5. python3 -m venv env
6. cd env\Scripts
7. ./activate
8. cd ../..
9. pip install pyautogui
10. pip install pynput

------------------------------CHECK THESE PATHS--------------------------

11. PRESS Windows + r
12. TYPE regedit
13. find folder name HKEY_LOCAL_MACHINE
14. find folder name SYSTEM
15. find folder name CurrentControlSet
16. find folder name Control
17. find folder name Class
18. find folder name 4D36E972-E325-11CE-BFC1-08002BE10318
19. Tap on folder name 0001
20. If you can see your wifi adapter name here for eg., 
(Intel(R) Wi-Fi 6E AX211 160MHz), then you can run this script without 
any error [otherwise] find correct path of your wifi adapter.
And edit the [exploit.py] script and find the line
f"Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001' -Name NetworkAddress -Value {mac_address}"
add the full path of your adapter folder in place of 
{HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001}

----------------------------RUNNING SCRIPT---------------------------------

21. python exploit.py

