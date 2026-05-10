from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
class MyApp (App):
    def build(self):
        screenmanager = ScreenManager()
        screenmanager.add_widget(NewScreen(name = 'screen'))
        return screenmanager

class NewScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

app = MyApp()
app.run()