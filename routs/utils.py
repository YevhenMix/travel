from trains.models import Train


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(_qs):
    qs = _qs.values()
    graph = {}
    for q in qs:
        graph.setdefault(q['from_city_id'], set())
        graph[q['from_city_id']].add(q['to_city_id'])

    return graph


def get_routes(request, form):
    qs = Train.objects.all().order_by('travel_time')
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    traveling_time = data['traveling_time']
    graph = get_graph(_qs=qs)
    all_ways = list(dfs_path(graph, from_city.id, to_city.id))

    if len(all_ways) == 0:
        raise ValueError('Маршрута, удовлетворяющего условиям не существует!')

    if cities:
        across_cities = [city.id for city in cities]
        right_ways = []
        for way in all_ways:
            if all(point in way for point in across_cities):
                right_ways.append(way)
        if not right_ways:
            raise ValueError('Маршрут, через эти города невозможен!')
    else:
        right_ways = all_ways

    trains = []
    all_trains = {}
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)

    for route in right_ways:
        tmp = {'trains': []}
        total_time = 0
        for index in range(len(route) - 1):
            qs = all_trains[(route[index], route[index + 1])]
            qs = qs[0]
            total_time += qs.travel_time
            tmp['trains'].append(qs)
            tmp['total_time'] = total_time
        if total_time <= traveling_time:
            trains.append(tmp)

    if not trains:
        raise ValueError('Время в пути, больше заданого!')

    routes = []
    cities = {'from_city': from_city.name, 'to_city': to_city.name}

    for tr in trains:
        routes.append({'trains': tr['trains'],
                       'total_time': tr['total_time'],
                       'from_city': from_city.name,
                       'to_city': to_city.name})

    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(x['total_time'] for x in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)

    context = {'form': form,
               'routes': sorted_routes,
               'cities': cities}

    return context
