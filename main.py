from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.config import Config
from kivy.core.window import Window
from kivy.metrics import dp, sp
import mysql.connector
import hashlib




db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ubunto123",
    database="TFW"
)
mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Users (username VARCHAR(20) NOT NULL, password VARCHAR(100) NOT NULL, admin_rights boolean NOT NULL, userID int PRIMARY KEY AUTO_INCREMENT)")
#hash_object = hashlib.sha256('daviid'.encode('utf-8'))
#hex_dig = hash_object.hexdigest()


#mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", ("daviid", "daviid", True))
#db.commit()


class NavDemoWindow(NavigationDrawer):
    pass


class LoginPage(Screen):
    def verify_credentials(self):

        user = self.ids.login
        pwd = self.ids.passw
        info = self.ids.info

        username = user.text
        password = pwd.text
        mycursor.execute("SELECT * FROM Users WHERE username = '"+username+"' AND password = '"+password+"'")
        results = mycursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[0])
                info.text = ''
                self.manager.current = "user"
            return ""

        else:
            print("Username and Password not found")
        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/ or Password required[/color]'
        else:
            info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


class UserPage(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


kv_file = Builder.load_file('login.kv')


class LoginApp(App):
    def builder(self):
        return kv_file


if __name__ == '__main__':
    LoginApp().run()