#!/usr/bin/env python3
# import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip


# Names of visitors
jackie = Visitor("Jackie")
dylan = Visitor("Dylan")
abby = Visitor("Abby")


# National Parks
rocky_mountian = NationalPark("Rocky Mountain National Park")
bryce = NationalPark("Bryce National Park")
# rocky_mountian.name = "Zion"
obj = NationalPark(rocky_mountian)


# Trips
smith_family = Trip(abby, rocky_mountian, "Aug 3", "Aug 10")
thompson_family = Trip(abby, bryce, "Aug 3", "Aug 10")
rmnp_trip = Trip(jackie, rocky_mountian, "May 12", "May 16")

# print(Trip.all[0].visitor)
# print(obj)

# This is a way to break the hasattr relationship by passing in a location instead of a name
# print(hasattr(obj, "location"))
# This is a way to make hasatt by keeping name 
# print(hasattr(obj, "name"))
# print(jackie.name)
# print(rocky_mountian.name)
# if __name__ == '__main__':
#     print("HELLO! :) let's debug :vibing_potato:")

    # ipdb.set_trace()
