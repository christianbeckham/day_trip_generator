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


def generate_day_trip(destinations, restaurants, transportation, entertainment):
    day_trip = []

    random_destination = make_random_selection(destinations)
    random_restaurant = make_random_selection(restaurants)
    random_transport = make_random_selection(transportation)
    random_entertainment = make_random_selection(entertainment)

    day_trip.append(random_destination)
    day_trip.append(random_restaurant)
    day_trip.append(random_transport)
    day_trip.append(random_entertainment)

    return day_trip


def print_trip_details(trip):
    print('\nHere is your current day trip:')
    print('\tLocation:', trip[0])
    print('\tRestaurant:', trip[1])
    print('\tTansportation:', trip[2])
    print('\tEntertainment:', trip[3])


def prompt_user_input_boolean(message):
    user_input = input(message)

    if user_input.lower() == 'yes':
        return True
    else:
        return False


def prompt_user_input_number(message):
    user_input = int(input(message))
    return user_input


print('Welcome to the Day Trip Generator!')
trip = generate_day_trip(destinations, restaurants,
                         types_of_transportation, types_of_entertainment)

print_trip_details(trip)
