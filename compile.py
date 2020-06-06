import os
import PyInstaller.__main__

# https://pyinstaller.readthedocs.io/en/stable/usage.html

PyInstaller.__main__.run([
    '--name=%s' %"UrbanDictionary-Shitpost",
    '--onefile',
    '--icon=%s' %os.path.join("", "", "yare.ico"),
    os.path.join('', 'main.py')
    ])
