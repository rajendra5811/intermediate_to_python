class House:
    PRICE_PER_SQUARE_FOOT =2.5
    def __init__(self,size,num_bedrooms,num_bathrooms):
        self.size=size
        self.beds=num_bedrooms
        self.baths=num_bathrooms
    @property    
    def price(self):
        return self.size  * self.PRICE_PER_SQUARE_FOOT
home=House(1000,2,2)
print(home.price)
print(home.size)
class Distance:
    _KILOMETERS_PER_MILE = 1.60934
    
    def __init__(self, km):
        self.km = km
        
    @property
    def miles(self):
        return self.km / self._KILOMETERS_PER_MILE
    
    @miles.setter
    def miles(self, value):
        self.km = value * self._KILOMETERS_PER_MILE

# 1. Instantiate the class with an initial KM value
dist = Distance(10)
print(f"Initial distance: {dist.miles:.2f} miles")

# 2. Update the distance using the miles setter
dist.miles = 8  # This triggers the @miles.setter
print(f"Updated distance in km: {dist.km:.2f} km")