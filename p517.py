#!/usr/bin/env python

import random

Max = 2 ** 31 - 1

array = [ ]
arrayrand = [ ]

for i in range(100):
	array.append(random.randint(0, Max))

for i in range(10):
	arrayrand.append(random.choice(array))

arrayrand.sort()

print arrayrand
