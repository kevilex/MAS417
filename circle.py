import numpy as np
from stl import mesh
import math

def circlegen(number_of_points, radius, xoffset, yoffset, zoffset):
    vertices = np.array([[0,0,0]])

    for n in range(0,number_of_points):
        vertices = np.append(vertices, [[round(math.cos(2*(math.pi/number_of_points)*n)*radius) + xoffset, round(math.sin(2*(math.pi/number_of_points)*n)*radius) + yoffset, 0 + zoffset]], axis=0)

    vertices = np.append(vertices, [[0 + xoffset, 0 + yoffset, 10 + zoffset]], axis=0)

    for n in range(0,number_of_points):
        vertices = np.append(vertices, [[round(math.cos(2*(math.pi/number_of_points)*n)*radius) + xoffset, round(math.sin(2*(math.pi/number_of_points)*n)*radius) + yoffset, 10 + zoffset]], axis=0)

    faces = np.array([[0,1,2]])

    for n in range(0,int(len(vertices)/2)-2):
        faces = np.append(faces, [[(0),(1+n),(2+n)]], axis=0)

    faces = np.append(faces, [[(0),(1),(int((len(vertices)/2)-1))]], axis=0)

    for n in range(int(len(vertices)/2),len(vertices)-2):
        faces = np.append(faces, [[(int(len(vertices)/2)),(1+n),(2+n)]], axis=0)

    faces = np.append(faces, [[int((len(vertices)/2)),int((len(vertices)/2))+1,int((len(vertices)))-1]], axis=0)
        
    for n in range(0,int(len(vertices)/2)-2):
        faces = np.append(faces, [[(int(len(vertices)/2)+1+n),(1+n),(2+n)]], axis=0)
        faces = np.append(faces, [[(2+n),(int(len(vertices)/2)+1+n),(int(len(vertices)/2)+2+n)]], axis=0)

    faces = np.append(faces, [[1,int(len(vertices)/2)-1,int(len(vertices)/2)+1]], axis=0)
    faces = np.append(faces, [[int(len(vertices)/2)-1,int(len(vertices)/2)+1,int(len(vertices))-1]], axis=0)

    #Creating the mesh:
    #THI PART IS COPIED FROM https://pythonhosted.org/numpy-stl/usage.html:
    circle = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            circle.vectors[i][j] = vertices[f[j],:]

    return circle