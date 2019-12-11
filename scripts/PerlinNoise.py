import mathutils
import numpy as np
import bpy

# initializing coordinates 
# z is randomly selected between 0 and 1 to create different images at execution
# SMOOTHNESS: greater number = smaller steps = more details
x = 0
y = 0
z = mathutils.noise.random()
SMOOTHNESS = 150

# function is used to normalize noise values to values between 0 and 1
def normalizeMatrix(matrix):
    # search for smalles value and subtract from all values (e.g. -0.2 -> 0; 0.3 -> 0.5)
    min_value = np.amin(matrix)
    for x in range(len(matrix)):
        for y in range(np.size(matrix[x])):
            matrix[y][x] = (matrix[y][x] - min_value)

    # search for biggest value and divide all values by that (e.g. 1.3 -> 1; 0 -> 0)
    max_value = np.amax(matrix)
    for x in range(len(matrix)):
        for y in range(np.size(matrix[x])):
            matrix[y][x] = matrix[y][x] / max_value
                
    return matrix

# function to get perlin noise values
def MainPerlinNoise(height, width):
    # size of the image in pixels 
    heightMapX = height
    heightMapY = width
    size = heightMapX, heightMapY


    # blank image
    image = bpy.data.images.new("MyImage", width=size[0], height=size[1])

    # create pixels array with size of height map
    pixels = [None] * size[0] * size[1]

    imageArr = [[0 for x in range(heightMapX)] for y in range(heightMapY)]

    for x in range(size[0]):
        for y in range(size[1]):
            # assigning RGBA, normalizing noise values to [0, 1]
            # higher SMOOTHNESS for smaller steps results in noise values more similar to the previous one
            r =  mathutils.noise.noise(mathutils.Vector((x/SMOOTHNESS,y/SMOOTHNESS, z)))
            imageArr[x][y] = r


    # normalize values
    normalizedMoisture = normalizeMatrix(imageArr)

    #save values as pixels 
    for x in range(heightMapX):
        for y in range(heightMapY):
            # red value set to noise value
            r = normalizedMoisture[x][y]
            # green and blue also set to noise value
            g = r
            b = r
            # opacity set to 1
            a = 1.0
            pixels[(y * heightMapX) + x] = [r, g, b, a]

    # flatten list
    pixels = [chan for px in pixels for chan in px]

    # write pixels to image 
    image.pixels = pixels 

    # save moisture image
    image.filepath_raw = bpy.path.abspath("//") + "/textures/moisture.png"
    image.file_format = 'PNG'
    image.save()