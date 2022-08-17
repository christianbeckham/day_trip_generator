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
    print('\nDay Trip Information:')
    print('\tDestination:', trip[0])
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


def display_update_options(current_trip):
    counter = 1

    print('\nWhat do you want to update?')
    for option in current_trip:
        print(f'\tSelect [{counter}] to update {option}.')
        counter += 1
    print('\tSelect [0] to cancel.')


def update_trip_selection(current_trip, item):
    current_item = current_trip[item - 1]
    new_trip = current_trip.copy()

    if item == 1:
        new_item = make_random_selection(destinations)
    elif item == 2:
        new_item = make_random_selection(restaurants)
    elif item == 3:
        new_item = make_random_selection(types_of_transportation)
    elif item == 4:
        new_item = make_random_selection(types_of_entertainment)
    else:
        return

    while current_item == new_item:
        return update_trip_selection(new_trip, item)

    new_trip[item - 1] = new_item
    print(f'The {current_item} option has been updated to {new_item}.')
    return new_trip


def update_trip(current_trip):
    update_cycle = True
    update_cycle_count = 1
    updated_trip = current_trip.copy()

    while update_cycle == True:
        if update_cycle_count == 1:
            update_message = '\nDo you want to update this trip? Enter [Yes] or [No]: '
            update_cycle_count += 1
        else:
            update_message = '\nDo you want to make other updates? Enter [Yes] or [No]: '

        update_trip_prompt = prompt_user_input_boolean(update_message)

        if update_trip_prompt:
            display_update_options(updated_trip)
            item_to_update = prompt_user_input_number(
                '\nEnter update option (use number): ')

            if item_to_update != 0:
                updated_trip = update_trip_selection(
                    updated_trip, item_to_update)
        else:
            update_cycle = False

    return updated_trip


print('\nWelcome to the Day Trip Generator!')
trip = generate_day_trip(destinations, restaurants,
                         types_of_transportation, types_of_entertainment)
print_trip_details(trip)

is_trip_completed = False
while is_trip_completed == False:
    trip_confirmation_input = prompt_user_input_boolean(
        '\nDo you want to complete this trip? \nEnter [Yes] to CONFIRM or [No] to UPDATE: ')

    if trip_confirmation_input == False:
        trip = update_trip(trip)
    else:
        is_trip_completed = True
        print('\nYour day trip is completed!')
        print_trip_details(trip)
