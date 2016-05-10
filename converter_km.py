from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class ConvertToKmApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('converter.kv')
        return self.root

    def handle_calculate(self):
        """convert miles to km"""
        number = self.validate_number()
        conversion = number * MILES_TO_KM
        self.root.ids.output_label.text = str(conversion)

    def handle_increment(self, increment):
        """ add or subtract in increments of 1 to the number
        :param increment
        """
        number = self.validate_number() + increment
        self.root.ids.input_number.text = str(number)
        self.handle_calculate()

    def validate_number(self):
        """ handle invalid inputs. if the input is text, display 0.0 as output"""
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0


ConvertToKmApp().run()

