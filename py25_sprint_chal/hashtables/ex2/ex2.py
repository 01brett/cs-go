#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    for t in tickets:
        if t.source not in cache:
            cache[t.source] = t.destination

    temp = cache["NONE"]
    route = []

    for _ in range(length):
        route.append(temp)
        temp = cache[temp]

    return route
