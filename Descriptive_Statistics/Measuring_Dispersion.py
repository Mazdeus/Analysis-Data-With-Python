import numpy as np

jumlah_game = np.array([4, 7, 1, 0, 3, 1, 2, 2, 5, 4, 8])

# Range
range = jumlah_game.max() - jumlah_game.min()
print("Range:", range)  # Output: Range: 8

# Interquartile Range (IQR)
iqr = np.percentile(jumlah_game, 75) - np.percentile(jumlah_game, 25)
print("Interquartile Range (IQR):", iqr)  # Output: Interquartile Range (IQR): 3.0

# Variance
import pandas as pd
jumlah_game_series = pd.Series(jumlah_game)
print("Variance : ", jumlah_game_series.var())

# Standard Deviation
print("Standar Deviation : ", jumlah_game_series.std())