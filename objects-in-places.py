# Write your code here :-)
import random
from pprint import pprint

objects = ["car", "hat", "towel", "banana"]
places = {
    (0, 0) : "kitchen",
    (1, 1) : "dining room",
    (1, 0) : "hall",
    (0, 1) : "nowhere"
}
place_objects = {}

for place in places:
    place_objects[place] = []
pprint(place_objects)

for obj in objects:
    x = random.randint(0, 1)
    y = random.randint(0, 1)
    place_objects[x, y].append(obj)
pprint(place_objects)
