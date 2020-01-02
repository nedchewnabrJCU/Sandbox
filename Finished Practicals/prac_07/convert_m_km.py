from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKilometreApp(App):
    def build(self):
        """
        Setup GUI environment.
        """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_addition(self, value_change):
        """
        Increase or decrease the inputted value by 1 depending on what the user selects (Up or Down)
        """
        value = self.valid_value_check() + value_change
        self.root.ids.miles_input.text = str(value)

    def handle_calculate(self):
        """
        Convert the inputted miles into kilometres.
        """
        value = self.valid_value_check()
        converted_result = value * MILES_TO_KM
        self.root.ids.converted_kilometres.text = str(converted_result)

    def valid_value_check(self):
        """
        Check if the inputted text is a valid number.
        """
        try:
            value = float(self.root.ids.miles_input.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKilometreApp().run()
