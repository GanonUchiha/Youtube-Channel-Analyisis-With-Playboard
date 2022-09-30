pyinstaller --noconfirm src\main.py
copy dist\*.dll dist\main
copy chromedriver.exe dist\main