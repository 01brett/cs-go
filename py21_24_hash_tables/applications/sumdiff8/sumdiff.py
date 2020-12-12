"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q1 = (1, 3, 4, 7, 12)
q2 = set(range(1, 10))
# q3 = set(range(1, 200))


def f(x):
    return x * 4 + 6


# ITERATIVE
# def sumdiff(q):
#     seen = {}
#     refs = {n: f(n) for n in q}

#     # keep track of where we're at
#     count = [0 for _ in q]
#     # arr to mess with -> start at first el
#     arr = [q[0] for _ in range(4)]

#     while count[-1] < len(q):


# RECURSIVE
def sumdiff(q):
    seen = {}
    refs = {n: f(n) for n in q}

    def fn(src, arr):
        combo = tuple(arr)
        if combo in seen:  # return if we've seen combo
            return

        if len(arr) == 4:
            seen[combo] = True  # mark this combo in cache
            a, b, c, d = combo  # pull out refs from combo
            ra, rb, rc, rd = refs[a], refs[b], refs[c], refs[d]  # grab computed refs
            if ra + rb == rc - rd:  # see if results hit our criteria
                print(f"f({a}) + f({b}) = f({c}) - f({d})\t{ra} + {rb} = {rc} - {rd}")
            return  # exit out of this call to prevent further loop

        for n in src:
            arr.append(n)
            fn(src, arr)
            arr.pop()

    fn(q, [])


print(f"\ntuple: {q1}\n")
sumdiff(q1)
# print(f"\nset: {q2}\n")
# sumdiff(q2)
