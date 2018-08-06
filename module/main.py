from kivy.app import App
from kivy.uix.button import Button as Bt


class TestApp(App):
    def build(self):
        return Bt(text='Hello World')


if __name__ == '__main__':
    TestApp().run()