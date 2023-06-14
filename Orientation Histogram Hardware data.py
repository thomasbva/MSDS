# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:15:02 2023

@author: treyb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "2023-06-13-survey.csv"

data = pd.read_csv(path)

counts, bins, patches = plt.hist(
    data.iloc[:, 5], bins=10, color='green', edgecolor='black', width=300)

# Set labels and title
plt.xlabel('Hard drive size (in GB)')
plt.ylabel('Frequency')
plt.title('Histogram of Hard drive sizes (in GB) for 2024 Cohort')

for count, patch in zip(counts, patches):
    x = patch.get_x() + patch.get_width() / 2
    y = patch.get_height()
    plt.text(x, y, int(count), ha='center', va='bottom')

# Display the histogram
    plt.show()
