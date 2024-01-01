import random

feet_in_mile = 5280
beatles = ["John Lennon", "Paul MaCartney", "George Harison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
