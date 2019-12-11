import bpy

DiamondSquare = bpy.data.texts['SquareDiamond.py'].as_module()
PerlinNoise = bpy.data.texts['PerlinNoise.py'].as_module()

#Width and height of the image
Width = 1024
Height = 1024

#Create height map
DiamondSquare.MainSquareDiamond(Height,Width)

#Create Noise Map
PerlinNoise.MainPerlinNoise(Height,Width)
