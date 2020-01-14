from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Flagfall rate for SilverServiceTaxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string of SilverServiceTaxi"""
        return "{}, plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get SilverServiceTaxi fare"""
        return round(self.flagfall + super().get_fare(), 1)
