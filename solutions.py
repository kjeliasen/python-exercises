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
    for car in cars
        car_list.append(car['make'] + ' ' + car['model'])
    
    return car_list
