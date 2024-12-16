#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

distances = {}
def dist(a,b):
    x1, y1 = sites[a]
    x2, y2 = sites[b]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


names = sites.keys()
for a in names:
    distances[a] = dict((b, dist(a,b)) for b in names)
print(distances)




