from cx_Freeze import setup,Executable
import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtCore

base = None
if sys.platform == "win32":
    base = "Win32GUI"
includefiles = ['667775.jpg','application.ui','notfound.png','Golden-Spotify-icon-png.ico']
includes = []
excludes = ['Tkinter']
packages = ['os','PyQt5','spotipy','PyQt5.QtGui','PyQt5.QtWidgets','PyQt5.uic','PyQt5.QtCore','sys']

setup(
    name = 'CoverImageDownloader',
    version = '0.1',
    description = 'A general enhancement utility',
    author = 'Yılmaz Güney',
    author_email = 'emirhanyilmazguney@hotmail.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable(script='main.py',base=base,icon='Golden-Spotify-icon-png.ico')]
)
