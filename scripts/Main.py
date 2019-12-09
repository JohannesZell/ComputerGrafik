import bpy

DiamondSquare = bpy.data.texts['SquareDiamond.py'].as_module()
PerlinNoise = bpy.data.texts['PerlinNoise.py'].as_module()

Width = 1024
Height = 1024

DiamondSquare.MainSquareDiamond(Height,Width)
PerlinNoise.MainPerlinNoise(Height,Width)
