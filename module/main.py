# The requirement for version is necessary since it is hard to maintain the program with updating version.
import kivy

# The App module is the main part of kivy
from kivy.app import App as kivy_app

# The uix module is the section that holds the user interface elements like layouts and widgets.
from kivy.uix.button import Label as kivy_label

# Set up window's width and height
from kivy.config import Config as general_config

kivy.require('1.10.1')
general_config.set('graphics', 'width', '810')
general_config.set('graphics', 'height', '500')


## Inherit from App
class HelloWorld(kivy_app):
    ## This method is App.build(). <br>
    #  Implementing its build() method, so it returns a Widget instance (the root of your widget tree)
    def build(self):
        return kivy_label(text='Hello World')


if __name__ == '__main__':
    HelloWorld().run()