class Beach:

    def __init__(self, location, water_color, temperature):
        self.location = location #instance variable
        self.water_color = water_color
        self.heat_rating = 'hot' if temperature > 80 else 'cool'
        self.parts = ['water','sand']
        self.ocean_name = ['pacific', 'arctic', 'Indian' , 'Atlantic']

    def add_part(self, part):
        self.parts.append(part)

def main():
        cape_cod_beach = Beach("Cape Cod", "dark blue" , 70)
        cancun_beach = Beach("Cancun", 'crystal blue', 90)
        cape_cod_beach.add_part('rock')
        la_beach = Beach('LA', 'turquoise', 85)
        italy_beach = Beach('Italy', 'blue', 82)
        italy_beach.add_part('rock')
        hot_not_rocky = []
        for beach in [cape_cod_beach, cancun_beach, la_beach, italy_beach]:
            if beach.heat_rating == 'hot'and 'rock' not in beach.parts:
                hot_not_rocky.append(beach)

        return hot_not_rocky
    
if __name__ == '__main__':
    beaches = main()
    print([beach.location for beach in beaches])