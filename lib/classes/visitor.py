from .trip import Trip

class Visitor:

    # all_visitors = []

    def __init__(self, name):
        self.trips = []
        self.name = name
        # self.all_visitors.append(self)
    
    def get_name(self):
        return self._name 
    
    def set_name(self, new_name):
        if (type(new_name) == str and 1<=len(new_name)<= 15):
            self._name = new_name
    
    name = property(get_name, set_name)

    # def trips(self):
    #      return [trip for trip in Trip.all_trips if trip.visitor == self]



    # def get_trip(self):
    #     return self._trips
    
    # def set_trip(self, trip):
    #     for trip in Trip.all:
    #         if trip == self.name:
    #             self.trips.append(self)
    #     # return self.trips
    
    # trip = property(get_trip, set_trip)





    #### Visitor

# - `Visitor __init__(self, name)`
#   - Visitor should be initialized with a name
# - `Visitor property name`
#   - Return name
#   - Names must be of type `str`
#   - Names must be between 1 and 15 characters, inclusive