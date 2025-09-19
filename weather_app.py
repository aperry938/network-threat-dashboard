# weather_app.py
# Translated by Anthony Perry
# WGU D793, Task 2

import math

class Weather:
    """
    A class to represent and calculate weather data for a 7-day forecast.
    """
    def __init__(self, high_temps, low_temps, wind_speed, weather_code):
        """Initializes the Weather object with forecast data."""
        self.f_high_array = high_temps
        self.f_low_array = low_temps
        self.ws_mph = wind_speed
        self.w_code = weather_code
        self.number_temperatures = len(high_temps)
        self.description = self._determine_description()

    def _determine_description(self):
        """A private method to determine the weather description from a code."""
        if self.w_code == 'S':
            return "SUNNY"
        elif self.w_code == 'P':
            return "PARTLY CLOUDY"
        elif self.w_code == 'C':
            return "CLOUDY"
        elif self.w_code == 'N':
            return "CLEAR"
        else:
            return "UNDEFINED"

    def calculate_average_high(self):
        """Calculates the average high temperature for the week."""
        return sum(self.f_high_array) / self.number_temperatures

    def calculate_average_low(self):
        """Calculates the average low temperature for the week."""
        return sum(self.f_low_array) / self.number_temperatures

    def find_weekly_high(self):
        """Finds the highest temperature for the week."""
        return max(self.f_high_array)

    def find_weekly_low(self):
        """Finds the lowest temperature for the week."""
        return min(self.f_low_array)

    def display_today_weather(self):
        """Prints the forecast for the first day (Sunday)."""
        print("SUNDAY FORECAST")
        print(f"High:  {self.f_high_array[0]}  (F)  Low:  {self.f_low_array[0]}  (F)")
        print() # For spacing

    def display_weekly_weather(self):
        """Prints the full weekly forecast summary."""
        days = [
            "Sunday   ", "Monday   ", "Tuesday  ", "Wednesday",
            "Thursday ", "Friday   ", "Saturday "
        ]
        
        print("THE WEEKLY FORECAST")
        # Use formatting to match Fortran's default float output style
        print(f"Average Hi:   {self.calculate_average_high():.7f}")
        print(f"Average Low:  {self.calculate_average_low():.7f}")
        print()
        print(f"Highest Weekly Temperature:  {self.find_weekly_high()}  (F) ")
        print(f"Lowest Weekly Temperature:   {self.find_weekly_low()}  (F) ")
        print()

        for i in range(self.number_temperatures):
            print(days[i])
            print(f"High:  {self.f_high_array[i]}  (F)  Low:  {self.f_low_array[i]}  (F)")
            print()

def main():
    """Main function to run the weather program."""
    # Initial data from main.f90
    fh = [78, 76, 80, 82, 85, 79, 75]
    fl = [75, 70, 75, 76, 75, 70, 69]
    ws = 9
    wc = 'P'

    # Initialize the Weather object
    w = Weather(high_temps=fh, low_temps=fl, wind_speed=ws, weather_code=wc)

    # Call methods to display weather information
    w.display_today_weather()
    w.display_weekly_weather()

if __name__ == "__main__":
    main()
