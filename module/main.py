from kivy.app import App
from kivy.uix.button import Label as kivy_lable
from kivy.config import Config as general_config
general_config.set('graphics', 'width', '810')  # set window's width
general_config.set('graphics', 'height', '500')  # set window's height

## A sub-class of "kivy.app.App"
class TestApp(App):
    ## This method is kivy.app.App.build(). <br>
    #  Implementing its build() method,
    #  so it returns a Widget instance (the root of your widget tree)
    def build(self):
        return kivy_lable(text='Hello World')


if __name__ == '__main__':
    TestApp().run()