import numpy as np
from stl import mesh

def smilegen(happiness, width, xoffset, yoffset, zoffset):
    #Creating an array with coordinates and offsets for the smiley, the only two points that change are the edges of the smile itself:
    vertices = np.array([\
        [0 + xoffset, 0 + yoffset, 0 + zoffset],
        [0 + xoffset, width/3 + yoffset, 0 + zoffset],
        [width + xoffset, (width/6) + 2*happiness + yoffset, 0 + zoffset],
        [-width + xoffset, (width/6) + 2*happiness + yoffset, 0 + zoffset],
        [0 + xoffset, 0 + yoffset, 3 + zoffset],
        [0 + xoffset, width/3 + yoffset, 3 + zoffset],
        [width + xoffset, (width/6) + 2*happiness + yoffset, 3 + zoffset],
        [-width + xoffset, (width/6) + 2*happiness + yoffset, 3 + zoffset]])

    #Connecting all the points together to create a mesh:
    faces = np.array([\
        [0, 1, 2],
        [0, 1, 3],
        [0, 1, 2],
        [4, 5, 6],
        [4, 5, 7],
        [2, 6, 0],
        [3, 7, 0],
        [6, 0, 4],
        [7, 0, 4],
        [6, 1, 5],
        [7, 1, 5],
        [2, 6, 1],
        [3, 7, 1]])

    #Creating the mesh:
    #The code below is copied from https://github.com/WoLpH/numpy-stl and creates a mesh using the point-array and face-array.
    smile = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            smile.vectors[i][j] = vertices[f[j],:]       

    return smile