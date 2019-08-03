# Pyn3D
### A Python 3D Game Engine and Renderer - *Now With Mesh Tools*
### What Is *Pyn*?
Pyn is a Python 3D game engine and renderer. It is great for creating your own 3D games from scratch with Python, and includes great mesh tools and environmental features. Pyn allows simple physics and easy manipulation to create 3D visualizers, games, and more. Pyn has lighting, materials, and textures, and is completely free and open-source. It is very easy to use and create your own meshes and renders, as well as built-in mesh tools to manipulate your meshes.

###### For more information, see the [documentation](https://github.com/underpig1/Pyn3D/wiki)
###### Install [Pyn](#end)
###### Try a [Project](https://github.com/underpig1/Pyn3D/wiki/Project-Starting-Guide)
***
# Documentation
#### Contents
* [Introduction](#intro)
   * [Getting Started](#start)
* [Windows](#init)
   * [Init](#init)
   * [Mouse](#mouse)
   * [Window](#window)
   * [Camera](#camera)
* [Meshes](#objects)
   * [Objects](#objects)
   * [Meshes](#meshes)
   * [Polygons](#polygons)
   * [Custom Meshes](#customs)
* [Lights](#lights)
* [Materials](#materials)
   * [Materials](#materials)
   * [Texturing](#texturing)
      * [Image Textures](#imagetextures)
      * [Map Textures](#maptextures)
   * [Using Materials](#usingmaterials)
   * [Change Color](#changecolor)
* [UI](#ui)
   * [UI Polygons](#uip)
   * [UI Text](#uit)
   * [Hover](#hover)
* [Physics](#physicsworld)
   * [Physics World](#physicsworld)
   * [Physics](#physics)
   * [Collisions and Colliders](#collisions)
* [Mesh Tools](#meshtools)
   * [Object Tools](#objecttools)
   * [Face Tools](#facetools)
   * [Vertex Tools](#vertextools)
   * [Advanced Tools](#advancedtools)
* [Particle Systems](#particles)
* [Pyn Meshes](#pynmeshes)
   * [Open and Download](#opendownload)
***

<a name = "intro"></a>
## Introduction to Pyn
Pyn is a Python 3D game engine and renderer. It is great for creating your own 3D games from scratch with Python, and includes great mesh tools and environmental features. Pyn allows simple physics and easy manipulation to create 3D visualizers, games, and more. Pyn has lighting, materials, and textures, and is completely free and open-source. It is very easy to use and create your own meshes and renders, as well as built-in mesh tools to manipulate your meshes.

<a name = "start"></a>
## Getting Started
Starting with Pyn is very simple:
```Python
from Pyn3D import *
```
All Pyn programs must begin with the `init()` script.

The `Camera` class creates a camera in your scene.

The `Mouse` class creates a mouse, and allows editing of the cursor and other properties.

The `window()` function creates and updates the window with your specifications.

Simple example program:
```Python
from Pyn3D import *

init()
# initialize window
cam = Camera(pos = (0, 0, -5))
mouse = Mouse()
# creates a camera and mouse object

Light(pos = (0, 3, 0), strength = 10)
Cube(pos = (0, 0, 0))
# creates a light and cube object

while True:
    window(cam)
    # updates the window
```

<a name = "init"></a>
## Init
Starting with Pyn needs the init script to create a window.
```Python
init(width, height)
```
The width and height properties determine the window's width and height. The default width and height is 400 by 400.

<a name = "mouse"></a>
## Mouse
The Mouse object is needed to determine the properties and position of the mouse or cursor.
```Python
Mouse(pos, visible, lock, cursor)
```
###### Position:
 * Vector2 tuple
 * The starting position of the cursor
```Python
Mouse(pos = (0, 0))
```
###### Visible:
 * 0 or 1 integer
 * Visibility of the cursor
```Python
Mouse(visible = 0)
```
###### Lock:
 * 0 or 1 integer
 * Locks cursor to window
```Python
Mouse(lock = 1)
```
###### Cursor:
 * Pygame cursor
 * Cursor display
```Python
Mouse(cursor = pygame.cursors.arrow)
```

<a name = "window"></a>
## Window
The `window()` function updates the window to your specifications.
```Python
window(camera, background, light)
```
###### Camera:
 * Camera object
 * Camera perspective displayed in the window
```Python
window(camera = cam)
```
###### Background:
 * RGB tuple
 * Background color of the window
```Python
window(background = (255, 255, 255))
```
###### Light:
 * Bool
 * Determines whether the background color is affected by Light objects
```Python
window(light = True)
```


<a name = "camera"></a>
## Camera
Cameras are needed in Pyn programs for visualization.
```Python
Camera(pos, rot, fly, fixed, spd)
```
###### Position:
 * Vector3 tuple
 * The position of the camera
```Python
Camera(pos = (0, 0, -5))
```
###### Rotation:
 * Vector2 tuple
 * The rotation of the camera
```Python
Camera(rot = (0, 0))
```
###### Flight:
 * Bool
 * If the camera can fly using Q and E keys
```Python
Camera(fly = False)
```
###### Fixed:
 * Bool
 * If the camera cannot move using W, A, S, and D keys
```Python
Camera(fixed = False)
```
###### Speed:
 * Float
 * Speed of the camera when moving
```Python
Camera(spd = 0.5)
```
###### Bounding Box:
 * List of Vector3 tuples
 * Bounding box vertices for collision detection
```Python
cam.bbox = [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)]
```
###### Check Collisions:
 * Object
 * Checks collisions with other object
```Python
cam.checkCollisions(cube)
```

<a name = "objects"></a>
## Objects
Objects are empty 3D objects which can be used for displaying visuals.
```Python
Object(pos, size, material, parent, physic)
```
###### Position:
 * Vector3 tuple
 * The position of the object
```Python
Object(pos = (0, 0, -5))
```
###### Size:
 * Float
 * The size of the object
```Python
Object(size = 5)
```
###### Material:
 * Material object index
 * The size of the object
```Python
Object(material = 0)
```
###### Parent:
 * Parent object
 * The parent of the object
```Python
Object(parent = cam)
```
###### Physic:
 * Physic list
 * The physics properties of the object
```Python
Object(physics = ["softbody", "gravity", "collider"])
```
###### Check Collisions:
 * Object
 * Checks collisions with other object
```Python
object.checkCollisions(cube)
```
###### Rotate:
 * X, Y, Z floats
 * Rotates object
```Python
object.rotate((10, 10, 10))
```
###### Move:
 * X, Y, Z floats
 * Moves object
```Python
object.move(0, 10, 0)
```
###### Place:
 * X, Y, Z floats
 * Places object
```Python
object.place(0, 0, 10)
```
###### Scale:
 * X, Y, Z floats
 * Scales object
```Python
object.scale(10, 0, 0)
```

<a name = "meshes"></a>
## Meshes
Meshes are pre-built meshes which come with Pyn and already-made coordinates.

Some pre-made meshes:
```Python
Cube()
Plane()
Point()
Line()
Circle()
```

<a name = "polygons"></a>
## Polygons
Polygons are 3D buildable objects based on Vector3D tuple X, Y, Z coordinates.

Example:
```Python
Polygon(args = [(0, 0, 0), (10, 10, 10), (0, 10, 0), (0, 0, 0)])
# creates a polygon mesh face based on X, Y, Z coordinates
```

<a name = "customs"></a>
## Custom Meshes
Custom Meshes are buildable 3D meshes based on vertices, faces, and default face colors.

Example
```Python
class MyMesh(Object):
     vertices = [(-4, -1, -1), (1, -1, -1), (1, 1, -1), (-3, 1, -1), (-4, -1, 1), (1, -1, 1), (1, 1, 1), (-3, 1, 1)]
     faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)]
     colors = [(100, 0, 0), (50, 50, 10), (100, 50, 50), (50, 100, 50), (50, 100, 100), (50, 50, 100), (50, 10, 100), (50, 100, 100), (50, 100, 10), (10, 50, 100)]
```
Custom Meshes must be an instance of the Object class.

<a name = "lights"></a>
## Lights
Lights are needed for lighting effects.
```Python
Light(pos, strength)
```
Lights can cause changes in color and brightness for objects, as well as the window background color.
###### Position:
 * Vector3 tuple
 * The position of the object
```Python
Light(pos = (0, 0, 0))
```
###### Strength:
 * Integer
 * The strength of the light
```Python
Light(strength = 10)
```

<a name = "materials"></a>
## Materials
Materials are objects for materializing meshes.
```Python
Material(color, emmission)
```
Materials can then be assigned to meshes.
###### Color:
 * RBG float
 * The color of the material
```Python
Light(color = (0, 0, 0))
```
###### Emmision:
 * Integer
 * The emission factor of the material
```Python
Light(emmission = 1)
```

<a name = "texturing"></a>
## Texturing
Texturing is a method of assigning an image or pixel map texture to the mesh using materials. Textures are texture objects for texturing meshes.
```Python
Texture()
```
Textures can be created using pixel maps or images, and must be assigned to the object by colors, each pixel being assigned a certain color. Mesh Tools are required for pixelating the mesh to add the pixel map to the mesh.

<a name = "imagetextures"></a>
## Image Textures
Image Textures are texture objects for texturing meshes using images.
```Python
Texture(path)
```
###### Path:
 * String
 * The path of the image
```Python
Texture(path = "myImage.png")
```

<a name = "maptextures"></a>
## Map Textures
Map Textures are texture objects based on a pixel map.
```Python
Texture()
```
Map textures can also be based on image textures.
###### Pixmap:
 * List of RGB tuples
 * The pixel map of the texture
```Python
texture.pixmap = [(0, 0, 0), (10, 10, 10), (0, 0, 0), (10, 10, 10)]
```

<a name = "usingmaterials"></a>
## Using Materials
Materials can be assigned though meshes' material variable.
```Python
myMaterial = Material(color = (0, 10, 0), emmision = 10)
Object(material = myMaterial)
```

<a name = "changecolor"></a>
## Change Color
The `changeColor()` function brightens or darkens a color.
```Python
changeColor(rgb, scale)
```
###### RGB:
 * RBG float
 * The color of the UI object
```Python
changeColor(rgb = (100, 100, 100))
```
###### Scale:
 * Integer
 * Amount to darken or lighten
```Python
changeColor(scale = 10)
```

<a name = "ui"></a>
## UI
UI objects are displayed on top of the graphics for 2D menus, buttons, and more.
```Python
UI(pos)
```
###### Position:
 * Vector2 tuple
 * The position of the UI object
```Python
UI(pos = (0, 0))
```
###### Move:
 * X, Y, Z floats
 * Moves the UI object
```Python
ui.move(10, 10, 10)
```

<a name = "uip"></a>
## UI Polygons
UI Polygons are 2D UI polygons.
```Python
UIPolygon(pos, color, points)
```
###### Position:
 * Vector2 tuple
 * The position of the UI object
```Python
UIPolygon(pos = (0, 0))
```
###### Color:
 * RBG float
 * The color of the UI object
```Python
UIPolygon(color = (0, 0, 0))
```
###### Points:
 * List of Vector3 tuples
 * The points of the UI object
```Python
UIPolygon(points = [(0, 0, 0), (10, 10, 10), (0, 10, 0), (0, 0, 0)])
```

<a name = "uit"></a>
## UI Text
UI Text objects are 2D UI text displays.
```Python
UIText(pos, color, text, font, size)
```
###### Position:
 * Vector2 tuple
 * The position of the UI object
```Python
UIText(pos = (0, 0))
```
###### Color:
 * RBG float
 * The color of the UI object
```Python
UIText(color = (0, 0, 0))
```
###### Text:
 * String
 * The text of the UI object
```Python
UIText(text = "WELCOME")
```
###### Font:
 * String
 * The font name of the UI object
```Python
UIText(font = "Sans Serif")
```
###### Size:
 * Integer
 * The font size of the UI object
```Python
UIText(size = 10)
```

<a name = "hover"></a>
## Hover
UI objects have a hover bool variable, which determines if the mouse is over the UI object, for buttons and menus.
```Python
ui.hover
```
Example:
```Python
ui = UIPolygon(pos = (100, 100), color = (100, 100, 100))
if ui.hover:
     ui.color = changeColor(ui.color, 10)
     # if hovered, the button brightens
```

<a name = "physicsworld"></a>
## Physics World
Physics Worlds are needed for object physics, as they determine the physics of the world.
```Python
PhysicsWorld(gravity, force)
```
###### Gravity:
 * Float
 * The gravity of the world
```Python
PhysicsWorld(gravity = 0.5)
```
###### Force:
 * Vector3 tuple
 * The force direction and power of the world
```Python
PhysicsWorld(force = (0, 10, 0))
```

<a name = "physics"></a>
## Physics
Physics can be applied to objects using the physic variable.
```Python
Object(physic = ["softbody", "gravity"])
object.physic = ["softbody", "gravity"]
```
Some useful physics attributes:
```Python
"softbody" # adds softbody
"gravity" # adds gravity for falling
"collider" # adds a collider for collisions
"bounce" # adds bounce for feathery objects or softbody objects
"force" # adds force for moving objects
"weight" # adds weight for heavy objects
```
Object physics depend on Physics Worlds.

For an object's physics to work, the object's physics must be constantly updated through the use of the `physics()` function:
```Python
while True:
     object.physics()
```

<a name = "collisions"></a>
## Collisions and Colliders
Collisions and Colliders can be used in object physics for colliding objects or other collisions. Colliders are a physics attribute that can be applied to objects. Two objects must have colliders in order for them to collide.
```Python
Object(physic = ["collider"])
```
To create other events when two objects collide, the `checkCollisions()` function checks the object's collisions with other objects, and returns a bool.
```Python
object.checkCollisions(otherObject)
```

<a name = "meshtools"></a>
## Mesh Tools
Mesh Tools are a collection of tools used for modifying meshes inside of Pyn. It can be used to create ocean meshes, animated meshes, mountain meshes, and house meshes. The Pyn Mesh Tools Library maximizes the usefulness of Pyn, and lets you create incredible creations with Pyn.
```Python
Mesh Tools Library
```
<a name = "objecttools"></a>
### Object Tools
#### Rotate
```Python
object.rotate(X, Y, Z)
```
#### Move
```Python
object.move(X, Y, Z)
```
#### Place
```Python
object.place(X, Y, Z)
```
#### Scale
```Python
object.scale(X, Y, Z)
```
<a name = "facetools"></a>
### Face Tools
#### Move Face
```Python
object.moveFace(face, X, Y, Z)
```
###### Face:
 * Face index
 * The face index of the face to move
```Python
object.moveFace(face = 0)
```
#### Rotate Face
```Python
object.rotateFace(face, X, Y, Z)
```
###### Face:
 * Face index
 * The face index of the face to rotate
```Python
object.rotateFace(face = 0)
```
#### Scale Face
```Python
object.scaleFace(face, X, Y, Z)
```
###### Face:
 * Face index
 * The face index of the face to scale
```Python
object.scaleFace(face = 0)
```
#### Extrude
```Python
object.extrude(face, X, Y, Z)
```
###### Face:
 * Face index
 * The face index of the face to extrude
```Python
object.extrude(face = 0)
```
#### Delete Face
```Python
object.deleteFace(face, X, Y, Z)
```
###### Face:
 * Face index
 * The face index of the face to delete
```Python
object.deleteFace(face = 0)
```
<a name = "vertextools"></a>
### Vertex Tools
#### Move Vertex
```Python
object.moveVertex(vert, X, Y, Z)
```
###### Vert:
 * Vertex index
 * The vertex index of the vertex to move
```Python
object.moveVertex(vert = 0)
```
<a name = "advancedtools"></a>
### Advanced Tools
#### Subdivide
* Subdivides the face
```Python
object.subdivide(face)
```
###### Face:
 * Face index
 * The face index of the face to subdivide
```Python
object.subdivide(face = 0)
```
#### Pixelate
* Pixelates the face
```Python
object.pixelate(face)
```
###### Face:
 * Face index
 * The face index of the face to pixelate
```Python
object.pixelate(face = 0)
```
#### Displace
* Displaces the face
```Python
object.displace(face, amount, damping)
```
###### Face:
 * Face index
 * The face index of the face to displace
```Python
object.displace(face = 0)
```
###### Amount:
 * Integer
 * The amount to displace
```Python
object.displace(amount = 10)
```
###### Damping:
 * Integer
 * The amount to damp from the displacement
```Python
object.displace(damping = 100)
```

<a name = "particles"></a>
## Particle Systems
Particle Systems create particles for smoke effects, explosions, and more.
```Python
ParticleSystem(obj, pos, spread, interval, movement)
```
###### Object:
 * Object
 * The object to clone for particles
```Python
ParticleSystem(obj = cube)
```
###### Position:
 * Vector3 tuple
 * The position of the Particle System
```Python
ParticleSystem(pos = (0, 0, 0))
```
###### Spread:
 * Integer
 * The spread of the particles in the Particle System
```Python
ParticleSystem(spread = 10)
```
###### Interval:
 * Integer
 * Wait between summoning of particles
```Python
ParticleSystem(interval = 10)
```
###### Movement:
 * Integer
 * Speed of particle movement
```Python
ParticleSystem(movement = 10)
```
###### Step:
 * Updates the Particle System
```Python
particles.step()
```
###### Clear:
 * Clears the particles in the Particle System
```Python
particles.clear()
```

<a name = "pynmeshes"></a>
## Pyn Meshes
Pyn Meshes are a specific file type, which can store mesh data and other properties of a mesh.
```
myMesh.pyn
```
<a name = "opendownload"></a>
### Open and Download
To open and download Pyn Meshes, use the `open()` and `download()` functions.
```Python
open(file)
# open a Pyn Mesh through a .pyn file
```
```Python
download(name, obj)
# download a Pyn Mesh as the name and object
```

<a name = "end"></a>
## Congratulations!
#### You made it to the end of the documentation!
###### [Now go try it yourself](https://github.com/underpig1/Pyn3D) or try a [project!](https://github.com/underpig1/Pyn3D/wiki/Project-Starting-Guide)
***
###### Download the [source](https://raw.githubusercontent.com/underpig1/Pyn3D/master/Pyn3D.py)
###### Install through pip:
```
pip install git+https://github.com/underpig1/Pyn3D#egg=Pyn3D
```
