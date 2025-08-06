import datetime

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

        if minute > 59:
            hour += minute // 60
            minute = minute % 60

        if hour > 23:
            hour = hour % 24

        while minute < 0:
            hour -= 1
            minute = 60 + minute

        while hour < 0:
            hour += 24

        self.current_time = datetime.time(hour=hour, minute=minute).strftime('%H:%M')


    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"


    def __str__(self):
        return self.current_time


    def __eq__(self, other):
        return self.current_time == other.current_time


    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)


    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
