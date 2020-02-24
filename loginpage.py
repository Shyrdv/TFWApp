from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder


class LoginPage(Screen):
    def verify_credentials(self):
        user = self.ids.login
        pwd = self.ids.passw
        info = self.ids.info

        username = user.text
        password = pwd.text

        if username == '' or password == '':
            info.text = '[color=#FF0000]Username and/ or Password required[/color]'
        else:
            if username == 'admin' and password == 'admin':
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
    LoginApp().run()