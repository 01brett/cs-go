def get_parents(data, target):
    parents = []

    for relations in data:
        parent, child = relations[0], relations[1]

        if child == target:
            parents.append(parent)
        if len(parents) == 2:  # only 2 parents possible, so break!
            break

    if len(parents) > 0:
        parents.sort(reverse=True)  # fixes where we have two earliest
        return parents
    return None


def earliest_ancestor(ancestors, starting_node):
    q = [starting_node]  # q is simple, no need for full-on Queue()
    ans = -1

    while len(q) > 0:
        node = q.pop(0)
        parents = get_parents(ancestors, node)

        if parents:
            for parent in parents:
                q.append(parent)
        else:  # get_parents -> None aka no parents
            if node == starting_node:  # no ancestors! break da loop
                break
            ans = node  # update our answer to the earliest so far
    return ans