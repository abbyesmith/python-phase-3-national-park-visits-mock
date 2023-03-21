
class Trip:
    all_trips = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all_trips.append(self)


#### Trip

# - `Trip __init__(self, visitor, national_park, start_date, end_date)`
#   - Trips should be initialized with a visitor, national_park, start_date(str), end_date(str)