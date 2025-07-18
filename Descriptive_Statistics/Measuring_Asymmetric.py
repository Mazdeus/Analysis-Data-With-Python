import numpy as np
import matplotlib.pyplot as plt

jumlah_game = np.array([4, 7, 1, 0, 3, 1, 2, 2, 5, 4, 8])

# Histogram
plt.hist(jumlah_game, bins= 5)
plt.show()

# Skewness
import pandas as pd
jumlah_game_series = pd.Series(jumlah_game)
print("Skewness:", jumlah_game_series.skew())  # Output: Skewness