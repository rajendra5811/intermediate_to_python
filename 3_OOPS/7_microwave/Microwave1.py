class Microwave:
    def __init__(self, company: str, power_rating: str) -> None:
        self.company = company
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.company}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.company}) is now turned on.")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.company}) is turned off.")
        else:
            print(f"Microwave ({self.company}) is already turned off.")

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Running ({self.company}) for {seconds} seconds.")
        else:
            print('A Mystical force whispers: "Turn on your microwave first...."')


smeg = Microwave(company="Smeg", power_rating="B")

smeg.turn_on()
smeg.run(30)
smeg.turn_off()