class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        answer = self.seconds / 31557600
        return round(answer, 2)

    def on_mercury(self):
        answer = self.seconds / (86400 * 87.969257175)
        return round(answer, 2)

    def on_venus(self):
        answer = self.seconds / ((0.61519726 * 365.25) * 86400)
        return round(answer, 2)

    def on_mars(self):
        answer = self.seconds / ((1.8808158 * 365.25) * 86400)
        return round(answer, 2)

    def on_jupiter(self):
        answer = self.seconds / ((11.862615 * 365.25) * 86400)
        return round(answer, 2)

    def on_saturn(self):
        answer = self.seconds / ((29.447498 * 365.25) * 86400)
        return round(answer, 2)

    def on_uranus(self):
        answer = self.seconds / ((84.016846 * 365.25) * 86400)
        return round(answer, 2)

    def on_neptune(self):
        answer = self.seconds / ((164.79132 * 365.25) * 86400)
        return round(answer, 2)
