from heapq import heappop, heappush

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruir_camino(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def a_estrella(mundo, start, goal, items):
    def a_estrella_simple(start, goal):
        open_set = []
        heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristica(start, goal)}

        while open_set:
            _, current = heappop(open_set)

            if current == goal:
                return reconstruir_camino(came_from, current)

            for neighbor in mundo.obtener_vecinos(current):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristica(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))

        return []

    # Encuentra el camino a cada ítem y luego al objetivo final
    path = []
    current_position = start

    for item in items:
        partial_path = a_estrella_simple(current_position, item)
        if not partial_path:
            return []  # Si no se puede llegar a un ítem, retorna un camino vacío
        path.extend(partial_path[1:])  # Evita duplicar el nodo de inicio
        current_position = item

    # Finalmente, encuentra el camino al objetivo final
    final_path = a_estrella_simple(current_position, goal)
    if not final_path:
        return []  # Si no se puede llegar al objetivo final, retorna un camino vacío

    path.extend(final_path[1:])  # Evita duplicar el nodo de inicio

    return path
