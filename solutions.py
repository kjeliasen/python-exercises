def make_model(cars):    
    '''
    Write a function named make_model. It will accept a list of dictionaries 
    where each dictionary represents a car, and return a list of strings where 
    each string is the make and model of the car concatenated together.

    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    ['Toyota Camry', 'Honda Accord', 'Ford Fiesta', 'Ford F-150']
    '''
    car_list = []
    for car in cars:
        car_list.append(car['make'] + ' ' + car['model'])
    
    return car_list


def extract_time_components(time24):
    '''
    Write a function named extract_time_components. It should take in a string 
    that is a 24-hour time with the hour, minutes, and seconds seperated by 
    :s, and return a dictionary with keys hour, minutes, and seconds with 
    corresponding integer values.

    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''
    hours = int(time24[:-6])
    minutes = int(time24[-5:-3])
    seconds = int(time24[-2:])
    time_components = dict(
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )
    return(time_components)
