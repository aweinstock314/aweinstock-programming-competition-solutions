#!/usr/bin/env python

foods = []
try:
    while True:
        tmp = raw_input().rstrip().split(':')
        categories = tmp[1].split(',')
        name, price = tmp[0].split(',')
        price = float(price)
        foods.append([name, price, set(categories)])
except EOFError:
    pass

#print foods
all_flavors = set(['salty', 'sweet', 'bitter', 'sour', 'spicy', 'umami'])


def greedy_main():
    by_price = list(sorted(foods, key=lambda x:x[1]))
    #print by_price

    cost = 0.0
    foods = []
    flavors_so_far = set()

    for food in by_price:
        if all_flavors.issubset(flavors_so_far):
            #print foods
            print('%.2f' % (cost,))
            break
        cost += food[1]
        foods.append(food[0])
        flavors_so_far.update(food[2])

def dynprog(cost, flavors_so_far, foods):
    if all_flavors.issubset(flavors_so_far):
        return cost
    subcosts = set()
    for food in foods:
        subfoods = set(foods)
        subfoods.remove(food)
        subcosts.add(dynprog(cost+food[1], flavors_so_far.union(set(food[2])), subfoods))
    return min(subcosts)

print('%.2f' % (dynprog(0.0, set(), set([((), food[1], tuple(food[2])) for food in foods])),))
