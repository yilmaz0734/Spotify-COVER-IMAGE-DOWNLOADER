from spotipy.oauth2 import SpotifyClientCredentials
from io import StringIO
import spotipy
import sys
import requests
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
from pathlib import Path
import numpy as np
from PIL import Image
import warnings
import PIL
from bs4 import BeautifulSoup
from PIL import ImageEnhance
from selenium import webdriver
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtCore
desktopPath = os.path.normpath(os.path.expanduser("~/Desktop/AksoyApp Cover Images"))
if not os.path.exists(desktopPath):
    os.makedirs(desktopPath)
desktopPath2 = os.path.normpath(os.path.expanduser("~/Desktop/AksoyApp Cover Images/Required Files"))
if not os.path.exists(desktopPath2):
    os.makedirs(desktopPath2)
sys.stdout = sys.stderr = open(f'{desktopPath}/example.log', 'a')

class spotify_data():
    def __init__(self,name):
        
        os.environ['SPOTIPY_CLIENT_ID'] = '<Your spotify client id>'  
        os.environ['SPOTIPY_CLIENT_SECRET'] = '<Your spotify client secret>'
        self.desktop = os.path.expanduser("~/Desktop")
        self.name=name
        
       
        search_str = self.name

        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.result = sp.search(search_str,4)
      
    def downloader(self):
        for i in range(4):
            try:
                self.veri=self.result['tracks']['items'][i]['album']['images'][0]['url']
                response = requests.get(self.veri)
                file1=open(f"{desktopPath2}/cover{i+1}.png","wb")
                file1.write(response.content)
            except:
                with open('notfound.png', 'rb') as f:
                    data = f.read()

                with open(f"{desktopPath2}/cover{i+1}.png","wb") as f:
                    f.write(data)
            
    
    def enhancer(self,image):
        img=Image.open(image)
        mywidth = 1080
        wpercent = (mywidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
        contrast = ImageEnhance.Contrast(img)
        contrast.enhance(1.2).save(image)
        filem=Image.open(image)
        sharpness = ImageEnhance.Sharpness(filem)
        sharpness.enhance(1.5).save(image)
    
        
        
        img_path="{}/{}.png".format(desktopPath,self.name)
        if not os.path.exists(img_path):
            filem.save("{}/{}.png".format(desktopPath,self.name))
        else:
            filem.save("{}/{}1.png".format(desktopPath,self.name))
           
        


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('uygulamam.ui', self)
        path = Path(__file__).parent / "667775.jpg"
        path=str(path).replace("\\","/")
        self.setStyleSheet('background-image : url("{}");'.format(path))
        self.le=self.findChild(QtWidgets.QLineEdit,'lineEdit')
        self.button = self.findChild(QtWidgets.QPushButton,'pushButton')
        self.button2=self.findChild(QtWidgets.QPushButton,'pushButton_2')
        self.button3=self.findChild(QtWidgets.QPushButton,'pushButton_3')
        self.button4=self.findChild(QtWidgets.QPushButton,'pushButton_4')
        self.button5=self.findChild(QtWidgets.QPushButton,'pushButton_5')
        self.button.clicked.connect(self.printButtonPressed)
        self.button2.clicked.connect(self.function2)
        self.button3.clicked.connect(self.function3)
        self.button4.clicked.connect(self.function4)
        self.button5.clicked.connect(self.function5)
        
        self.show()
        

    def printButtonPressed(self):
        # This is executed when the button is pressed
        try:
            print(self.le.text())
            self.data=spotify_data(str(self.le.text()))
            self.data.downloader()
            c1=Image.open(f'{desktopPath2}/cover1.png')
            
            c2=Image.open(f'{desktopPath2}/cover2.png')
            
            c3=Image.open(f'{desktopPath2}/cover3.png')
            
            c4=Image.open(f'{desktopPath2}/cover4.png')
        
            
            mywidth = 160
            wpercent = (mywidth/float(c1.size[0]))
            hsize = int((float(c1.size[1])*float(wpercent)))
            c5 = c1.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
            c5.save(f'{desktopPath2}/cover5.png')
            wpercent = (mywidth/float(c2.size[0]))
            hsize = int((float(c2.size[1])*float(wpercent)))
            c6 = c2.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
            c6.save(f'{desktopPath2}/cover6.png')
            wpercent = (mywidth/float(c3.size[0]))
            hsize = int((float(c3.size[1])*float(wpercent)))
            c7 = c3.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
            c7.save(f'{desktopPath2}/cover7.png')
            wpercent = (mywidth/float(c4.size[0]))
            hsize = int((float(c4.size[1])*float(wpercent)))
            c8 = c4.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
            c8.save(f'{desktopPath2}/cover8.png')
            path=str(desktopPath2).replace("\\","/")
            self.button2.setStyleSheet("background-image : url('{}/cover5.png');".format(path)) 
            self.button3.setStyleSheet("background-image : url('{}/cover6.png');".format(path)) 
            self.button4.setStyleSheet("background-image : url('{}/cover7.png');".format(path)) 
            self.button5.setStyleSheet("background-image : url('{}/cover8.png');".format(path)) 
            
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Here is the photos.')
            error_dialog1.exec_()
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('This doesn't exist in spotify database. {}'.format(e))
            error_dialog.exec_()
        
    def function2(self):
        try:
            self.data.enhancer(f'{desktopPath2}/cover1.png')
            
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Downloaded!')
            error_dialog1.exec_()
        except:
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Please provide a song name.')
            error_dialog1.exec_()
        


    def function3(self):
        try:
            self.data.enhancer(f'{desktopPath2}/cover2.png')
            
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Downloaded!')
            error_dialog1.exec_()
        except:
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Please provide a song name.')
            error_dialog1.exec_()

    def function4(self):
        try:
            self.data.enhancer(f'{desktopPath2}/cover3.png')
           
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Downloaded!')
            error_dialog1.exec_()
        except:
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Please provide a song name.')
            error_dialog1.exec_()
    def function5(self):
        try:
            self.data.enhancer(f'{desktopPath2}/cover4.png')
          
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Downloaded!')
            error_dialog1.exec_()
        except:
            error_dialog1 = QtWidgets.QErrorMessage()
            error_dialog1.showMessage('Please provide a song name..')
            error_dialog1.exec_()


        


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

