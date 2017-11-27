#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

a = np.array([[1,2],[3,4]])
sum0 = np.sum(a, axis=0)
sum1 = np.sum(a, axis=1)

print('hello')

print(sum0)
print(sum1)