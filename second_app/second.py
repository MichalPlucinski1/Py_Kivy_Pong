import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


#Builder.load_file('test.kv')

#Builder.load_string('''     cssik kivi ''')

class TestGrid(Widget):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def btn(self):
        print(f'User email:{self.email.text}, User password: {self.password.text}')
        self.email.text = ''
        self.password.text = ''
    


class TestApp(App):
    def build(self):
        return TestGrid()
    
if __name__ == '__main__':
    TestApp().run()