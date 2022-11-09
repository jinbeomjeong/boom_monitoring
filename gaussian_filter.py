import sys
from scipy.ndimage import gaussian_filter1d


num_1 = sys.argv[1]
num_2 = sys.argv[2]
num_3 = sys.argv[3]

out_1 = gaussian_filter1d([1, 2, 3], 3)

print(out_1)
