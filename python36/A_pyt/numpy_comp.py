#
# Loop Version --- Iterations in Python
#
# Array Initialization for Inner Values
iv = np.zeros((M + 1, M + 1), dtype=np.float)
for z, j in enumerate(range(M + 1)):
    for i in range(z + 1):
        iv[i, j] = max(S[i, j] - K, 0)
#
# Vectorized Version --- Iterations on NumPy Level
#
# Array Initialization for Inner Values
pv = maximum(S - K, 0)
