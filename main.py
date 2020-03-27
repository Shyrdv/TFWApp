from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
from kivy.metrics import dp, sp
import mysql.connector
import hashlib

db = mysql.connector.connect(
    host="172.104.148.212",
    user="daviid",
    passwd="Ubuntob0I!",
    database="Tfw",
    auth_plugin="mysql_native_password"
)
mycursor = db.cursor()




class LoginPage(Screen):
    def if_active(self, state):
        r_user = self.ids.rem_user
        r_pass = self.ids.rem_pass

        if state:

            r_pass.disabled = False

        else:
            r_pass.disabled = True
            r_pass.active = False

    def verify_credentials(self):

        user = self.ids.login
        pwd = self.ids.passw
        info = self.ids.info
        r_user = self.ids.rem_user
        r_pass = self.ids.rem_pass
        username = user.text
        password = pwd.text

        hash_object = hashlib.sha256(password.encode('utf-8'))
        hashedpw = hash_object.hexdigest()

        mycursor.execute("SELECT * FROM Users WHERE username = '"+username+"' AND password = '"+hashedpw+"'")
        results = mycursor.fetchall()

        if results and results[0][2] == 1:
            for i in results:
                print("Welcome "+i[0])
                info.text = ''
                if not r_user.active:
                    self.ids.login.text = ""
                if not r_pass.active:
                    self.ids.passw.text = ""

                self.manager.current = "admin"

            return ""
        elif results:
            for i in results:
                print("Welcome "+i[0])
                info.text = ''
                if not r_user.active:
                    self.ids.login.text = ""
                if not r_pass.active:
                    self.ids.passw.text = ""
                self.manager.current = "user"

            return ""

        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/ or Password required[/color]'
        else:
            info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


class UserPage(Screen):
    pass


class AdminPage(Screen):
    def dostuff(self):
        print("IT WORKS YES")

    def get_count(self):
        mycursor.execute("SELECT Count(*) FROM Users")
        results = mycursor.fetchone()[0]
        return "Current user count= " + str(results)


class CreateUserPage(Screen):

    def create_user(self):
        user = self.ids.createuser_username
        pwd = self.ids.createuser_password
        verifypwd = self.ids.createuser_verifypassword
        info = self.ids.info_create_user
        username = user.text
        password = pwd.text
        verifypassword = verifypwd.text

        mycursor.execute("SELECT * FROM Users WHERE username = '" +username+"'")
        results = mycursor.fetchall()

        if results:
            info.text = '[color=#FF0000]Username already exists![/color]'
        if not results:
            if verifypassword == password:
                mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", (username, hashlib.sha256(password.encode('utf-8')).hexdigest(), True))
                db.commit()
                info.text = '[color=#00FF00]User Created![/color]'
            else:
                info.text = '[color=#FF0000]Passwords discrepancy![/color]'

#ass


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)

    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if self.current_screen.name == "login_page":
                return False  # exit the app from this page
            elif self.current_screen.name == "admin":
                self.current = "login_page"
                return True  # do not exit the app
            elif self.current_screen.name == "user":
                self.current = "login_page"
                return True  # do not exit the app
            elif self.current_screen.name == "create_user_page":
                self.current = "admin"
                return True  # do not exit the app


kv_file = Builder.load_file('tfw.kv')


class TFWApp(App):
    def builder(self):
        return kv_file


if __name__ == '__main__':
    TFWApp().run()









#mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Users (username VARCHAR(20) NOT NULL, password VARCHAR(100) NOT NULL, admin_rights boolean NOT NULL, userID int PRIMARY KEY AUTO_INCREMENT)")


#mycursor.execute("INSERT INTO Users (username, password, admin_rights) VALUES (%s,%s,%s)", ("Daviid9400", hashedpw2, True))
#db.commit()


#engine = create_engine('mysql+mysqlconnector://daviid:Ubuntob0I!@172.104.148.212/Tfw')

#connection = engine.raw_connection()

#mycursor = connection.cursor()





  # hash_object = hashlib.sha256(password.encode('utf-8'))
      #  hashedpw = hash_object.hexdigest()