import numpy as np

jumlah_game = np.array([4,7,1,0,3,1,2,2,5,4,8])

# Mean
mean_jumlah_game = jumlah_game.mean()
print("Mean : ", mean_jumlah_game) # Output: 3.3636363636363638

# Median
median_jumlah_game = np.median(jumlah_game)
print("Median : ", median_jumlah_game) # Output: 3.0

# Mode
from scipy import stats

mode_jumlah_game = stats.mode(jumlah_game)[0]
print("Mode : ", mode_jumlah_game) # Output: 1