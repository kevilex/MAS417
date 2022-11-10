import numpy as np
from stl import mesh
import math

def circlegen(number_of_points, radius, xoffset, yoffset, zoffset):
    #Creating the centre point such that we can create a mesh as "pizza slices" from the middle of the circle to the edges of the circle:
    vertices = np.array([[0,0,0]])

    #Creating a list of "n" circular points with "radius" radius, and adding the "x,y,z-offests" for the FIRST circle:
    for n in range(0,number_of_points):
        vertices = np.append(vertices, [[round(math.cos(2*(math.pi/number_of_points)*n)*radius) + xoffset, round(math.sin(2*(math.pi/number_of_points)*n)*radius) + yoffset, 0 + zoffset]], axis=0)

    #Creating another centre point, but for the second circle that is offset vertically:
    vertices = np.append(vertices, [[0 + xoffset, 0 + yoffset, 10 + zoffset]], axis=0)

    #Creating a list of "n" circular points with "radius" radius, and adding the "x,y,z-offests" for the SECOND circle:
    for n in range(0,number_of_points):
        vertices = np.append(vertices, [[round(math.cos(2*(math.pi/number_of_points)*n)*radius) + xoffset, round(math.sin(2*(math.pi/number_of_points)*n)*radius) + yoffset, 10 + zoffset]], axis=0)

    #Creating a "faces" array, easier to simply create the first mesh-triangle rather than making an empty array:
    faces = np.array([[0,1,2]])

    #For-loop for connecting the centre point two the two next points in the list for the FIRST CIRCLE:
    for n in range(0,int(len(vertices)/2)-2):
        faces = np.append(faces, [[(0),(1+n),(2+n)]], axis=0)

    #This part ensures that the first point around the edge in the FIRST CIRCLE is connected to the last point in the FIRST CIRCLE, and then to the centre point:
    faces = np.append(faces, [[(0),(1),(int((len(vertices)/2)-1))]], axis=0)

    #For-loop for connecting the centre point two the two next points in the list for the SECOND CIRCLE:
    for n in range(int(len(vertices)/2),len(vertices)-2):
        faces = np.append(faces, [[(int(len(vertices)/2)),(1+n),(2+n)]], axis=0)

    #This part ensures that the first point around the edge in the SECOND CIRCLE is connected to the last point in the SECOND CIRCLE, and then to the centre point:
    faces = np.append(faces, [[int((len(vertices)/2)),int((len(vertices)/2))+1,int((len(vertices)))-1]], axis=0)
        
    #For-loop for "stiching" the two flat circle faces together, this is what connects the two indicidual circles into a circular plate with a thickness:
    for n in range(0,int(len(vertices)/2)-2):
        faces = np.append(faces, [[(int(len(vertices)/2)+1+n),(1+n),(2+n)]], axis=0)
        faces = np.append(faces, [[(2+n),(int(len(vertices)/2)+1+n),(int(len(vertices)/2)+2+n)]], axis=0)

    # Connecting the first points in the circles to the last ones, the foor loop does not connect these points together so this part is neccessary: 
    faces = np.append(faces, [[1,int(len(vertices)/2)-1,int(len(vertices)/2)+1]], axis=0)
    faces = np.append(faces, [[int(len(vertices)/2)-1,int(len(vertices)/2)+1,int(len(vertices))-1]], axis=0)

    #Creating the mesh:
    #The code below is copied from https://github.com/WoLpH/numpy-stl and creates a mesh using the point-array and face-array.
    circle = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            circle.vectors[i][j] = vertices[f[j],:]

    return circle