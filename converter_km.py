from kivy.app import App
from kivy.lang import Builder


class ConvertToKmApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('converter.kv')
        return self.root


ConvertToKmApp().run()
