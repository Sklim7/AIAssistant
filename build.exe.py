'''


PyInstaller


    pip install pyinstaller
'''

import PyInstaller.__main__
import os
import shutil


if os.path.exists("dist"):
    shutil.rmtree("dist")


PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--noconsole',
    '--name=project',
    '--clean',
    '--icon=NONE',
    '--noconfirm',
    '--windowed'
])