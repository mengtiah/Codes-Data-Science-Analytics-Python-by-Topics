## 3. Vector Operations ##

# This code draws the x and y axis as lines.
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-4,4)
plt.ylim(-1,4)

# Add your code here.
plt.quiver(0, 0, 3, 0, angles='xy', scale_units='xy', scale=1)
plt.quiver(3, 0, 0, 3, angles='xy', scale_units='xy', scale=1)
plt.quiver(0, 0, 3, 3, angles='xy', scale_units='xy', scale=1, color='green')

## 4. Scaling Vectors ##

# This code draws the x and y axis as lines.
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(0,10)
plt.ylim(0,5)

# Add your code here.
plt.quiver(0, 0, 3, 1, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, 6, 2, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(0, 0, 9, 3, angles='xy', scale_units='xy', scale=1, color='orange')

## 5. Vectors In NumPy ##

import numpy as np

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

vector_linear_combination=vector_one*2+vector_two*5

## 6. Dot Product ##

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

dot_product = np.dot(vector_one[:,0], vector_two)
print(dot_product)

## 7. Linear Combination ##

w=np.asarray([[1],[2]])
v=np.asarray([[3],[1]])
end_point=2*v-2*w