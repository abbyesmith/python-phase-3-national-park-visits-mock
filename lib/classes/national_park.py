from .trip import Trip
from .visitor import Visitor

class NationalPark:

    all_national_park=[]

    def __init__(self, name):
        # self.trips = []
        # print(self.trips)
        self.all_national_park.append(self)

        if (type(name) != str):
            print("Name must be a string")
        else:
            self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
            print("Cannot change park name")
    
    name = property(get_name, set_name)

    def trips(self):
         return [trip for trip in Trip.all_trips if trip.national_park == self]
    
    # def vistors(self):
    #     # visitors = []
    #     # return [visitor for visitor in Trip.all_trips if visitor.visitor == self]
    #     return list(set([trip.visitor for trip in self.trips()]))

    def visitors(self):
        visitors = []
        for trip in self.trips():
            if trip.visitor not in visitors:
                visitors.append(trip.visitor)
        return visitors
    
    def total_visits(self):
         return len(self.trips())


# Failed attempts:

    # def get_trip(self):
    #      return self._trips
    
    # def set_trip(self, trip):
    #     print("something")
    #     for trip in Trip.all:
    #          if trip == self.name:
    #             self.trips.append(self)
    #     trip = self.trip
    
    # trip = property(get_trip, set_trip)
    # @property
    # def trip(self):
    
    # @classmethod
    # def all_trips(cls):
    #      return [national_park.all_trips for national_park in cls.all_national_park]

    # @property
    # def trips(self):
    #      return self._trips

    

#### NationalPark

# - `NationalPark __init__(self, name)`
#   - NationalParks should be initialized with a name, as a string
# - `NationalPark property name`
#   - Returns the NationalPark's name
#   - Should not be able to change after the NationalPark is created
#   - hint: hasattr()
