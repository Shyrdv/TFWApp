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


class NavDemoWindow(NavigationDrawer):
    pass


class LoginPage(Screen):
    def verify_credentials(self):

        user = self.ids.login
        pwd = self.ids.passw
        info = self.ids.info
        r_user = self.ids.rem_user
        r_pass = self.ids.rem_pass

        username = user.text
        password = pwd.text

        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/ or Password required[/color]'
        else:
            if username == 'admin' and password == 'admin':
                info.text = ''
                if r_user.active:
                    r_pass.disabled=False
                if not r_user.active:
                    user.text = ''
                if not r_pass.active:
                    pwd.text = ''
                self.manager.current = "user"

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
    Config.set('graphics', 'resizable', 0)
    Window.size = (500, 1000)
    LoginApp().run()