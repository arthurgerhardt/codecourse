import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define os vértices do cubo
vertices = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]

# Define as faces do cubo usando os vértices
faces = [[vertices[j] for j in [0, 1, 2, 3]],
         [vertices[j] for j in [4, 5, 6, 7]], 
         [vertices[j] for j in [0, 1, 5, 4]], 
         [vertices[j] for j in [2, 3, 7, 6]],
         [vertices[j] for j in [1, 2, 6, 5]],
         [vertices[j] for j in [4, 7, 3, 0]]]

# Adiciona as faces ao gráfico
ax.add_collection3d(Poly3DCollection(faces, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Define os limites dos eixos
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

plt.show()