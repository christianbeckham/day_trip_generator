from random import randrange

destinations = ['Green Bay', 'Madison', 'Milwaukee']
restaurants = ['Burger King', 'Culvers', 'Kopps', 'McDonalds', 'Shake Shack']
types_of_transportation = ['Car', 'Taxi', 'Bus', 'Airplane', 'Train']
types_of_entertainment = ['Amusement park', 'Concert',
                          'Fair', 'Movie', 'Museum', 'Sporting event']


def make_random_selection(list):
    random_index = randrange(0, len(list))
    random_item = list[random_index]
    return random_item


random_destination = make_random_selection(destinations)
print(random_destination)
