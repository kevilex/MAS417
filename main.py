import subprocess
import circle 
import smile

import numpy as np
from stl import mesh

def run_cpp_thing():

    proc = subprocess.Popen('./io',
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        stdin=subprocess.PIPE)

    so, se = proc.communicate()

    return [int(x) for x in so.split()]

hapiness = int(run_cpp_thing()[0])

face = circle.circlegen(32,50, 0, 0, 0)

eyeR = circle.circlegen(24, 10, 20, 20, 5)

eyeL = circle.circlegen(24, 10, -20, 20, 5)

eyeRpup = circle.circlegen(12, 3, 20, 20, 6)

eyeLpup = circle.circlegen(12, 3, -20, 20, 6)

face_smile = smile.smilegen(hapiness, 30, 0, (-18 - hapiness),10)

combined = mesh.Mesh(np.concatenate([face.data, eyeR.data, eyeL.data, eyeRpup.data, eyeLpup.data]))
combined = mesh.Mesh(np.concatenate([combined.data, face_smile.data]))

combined.save('test.stl')


