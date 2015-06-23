import csv


def get_city_info(city):
    if 'X:' in city:
        return 'X', city.split('X:')[1]
    if 'S:' in city:
        return 'S', city.split('S:')[1]
    if 'V:' in city:
        return 'V', city.split('V:')[1]


def read_csv(filename):
    roads = []
    s_cities = []
    x_cities = []
    v_cities = []

    # Lemos o arquivo que possui o seguinte formato:
    # "<grupo>:<cidade>","<grupo>:<cidade>"
    # onde a primeira cidade se conecta a segunda
    # Existem 3 grupos:
    # - X, cidade populada
    # - S, cidade segura
    # - V, cidade comum
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            roads.append(row)

    # Devemos formatar as arestas e limpar o nome das cidades
    clean_roads = []
    for road in roads:
        cities = []
        for city in road:
            group, city_name = get_city_info(city)
            if group == 'X':
                x_cities.append(city_name)
            if group == 'S':
                s_cities.append(city_name)
            if group == 'V':
                v_cities.append(city_name)
            cities.append(city_name)
        edge = {
            'from': cities[0],
            'to': cities[1],
        }
        clean_roads.append(edge)

    # Remove as cidades repetidas
    x_cities = set(x_cities)
    s_cities = set(s_cities)
    v_cities = set(v_cities)

    return [x_cities, s_cities, v_cities, clean_roads]


def get_all_cities(s_cities, x_cities, v_cities):
    all_cities = []

    all_cities.extend(s_cities)
    all_cities.extend(x_cities)
    all_cities.extend(v_cities)

    return all_cities
