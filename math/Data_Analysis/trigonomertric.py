# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:20:45 2022

@author: Lete
"""

import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.linspace(-2*np.pi, 2*np.pi), 
         np.sin(np.linspace(-2*np.pi, 2*np.pi)))
plt.plot(np.linspace(-2*np.pi, 2*np.pi),
         np.cos(np.linspace(-2*np.pi, 2*np.pi)))
plt.show()