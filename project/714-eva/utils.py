import csv


def read_csv(filename):
    roads = []
    s_cities = []
    x_cities = []
    v_cities = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            roads.append(row)

    clean_roads = []
    for road in roads:
        cities = []
        for city in road:
            result = city.split('X:')
            if len(result) > 1:
                city_name = result[1]
                x_cities.append(city_name)
            else:
                result = city.split('S:')
                if len(result) > 1:
                    city_name = result[1]
                    s_cities.append(city_name)
                else:
                    city_name = city.split('V:')[1]
                    v_cities.append(city_name)
            cities.append(city_name)
        edge = {
            'from': cities[0],
            'to': cities[1],
        }
        clean_roads.append(edge)

    x_cities = set(x_cities)
    s_cities = set(s_cities)
    v_cities = set(v_cities)

    return [x_cities, s_cities, v_cities, clean_roads]
