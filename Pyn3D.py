import pygame, sys, math
try:
    from PIL import Image
except:
    pass
import random

objects = []
lights = []
materials = []
interfaces = []

def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

class Camera:
    def __init__(self, pos = (0, 0, 0), rot = (0, 0), fly = True, fixed = (False, False), spd = 0):
        x, y, z = pos
        self.bbox = [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)]
        self.bbox = [(float(x) + float(X)/2, float(y) + float(Y)/2, float(z) + float(Z)/2) for X, Y, Z in self.bbox]
        self.pos = list(pos)
        self.rot = list(rot)
        self.fly = fly
        self.fixed = fixed
        self.spd = spd

    def events(self, event):
        if self.fixed[1] == False:
            if event.type == pygame.MOUSEMOTION:
                x, y = event.rel
                x, y = float(x), float(y)
                x /= 200
                y /= 200
                self.rot[0] += y
                self.rot[1] += x

    def update(self, dt, key):
        s = dt * 10 + self.spd

        if self.fixed[0] == False:
            if self.fly == True:
                if key[pygame.K_q]: self.pos[1] += s
                if key[pygame.K_e]: self.pos[1] -= s

            x, y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
            if key[pygame.K_w]: self.pos[0] += x; self.pos[2] += y;
            if key[pygame.K_s]: self.pos[0] -= x; self.pos[2] -= y
            if key[pygame.K_a]: self.pos[0] -= y; self.pos[2] += x
            if key[pygame.K_d]: self.pos[0] += y; self.pos[2] -= x

        self.collision = False
        for obj in objects:
            if self.checkCollisions(obj):
                self.collision = True

    def checkCollisions(self, obj):
        xMax = max([i[0] for i in self.bbox])
        xMin = min([i[0] for i in self.bbox])
        yMax = max([i[1] for i in self.bbox])
        yMin = min([i[1] for i in self.bbox])
        zMax = max([i[2] for i in self.bbox])
        zMin = min([i[2] for i in self.bbox])
        xMax2 = max([i[0] for i in obj.verts])
        xMin2 = min([i[0] for i in obj.verts])
        yMax2 = max([i[1] for i in obj.verts])
        yMin2 = min([i[1] for i in obj.verts])
        zMax2 = max([i[2] for i in obj.verts])
        zMin2 = min([i[2] for i in obj.verts])
        collision = ((xMax >= xMin2 and xMax <= xMax2) or (xMin <= xMax2 and xMin >= xMin2)) and ((yMax >= yMin2 and yMax <= yMax2) or (yMin <= yMax2 and yMin >= yMin2)) and ((zMax >= zMin2 and zMax <= zMax2) or (zMin <= zMax2 and zMin >= zMin2))
        return collision

class Object:
    vertices = [()]
    faces = [()]
    colors = [()]

    def __init__(self, pos = (0, 0, 0), size = 1, material = 0, parent = None, physic = []):
        x, y, z = pos
        self.pos = pos
        self.size = size
        self.parent = parent
        self.physic = physic
        self.g = 0
        try:
            if material <= len(materials):
                self.materials = materials[material]
            else:
                self.materials = materials[0]
            colors = []
            for i in range(len(self.faces)):
                self.colors += material.color
        except:
            for i in range(len(self.faces)):
                self.colors += (100, 100, 100)
        self.verts = [(float(x) + float(X)/2, float(y) + float(Y)/2, float(z) + float(Z)/2) for X, Y, Z in self.vertices]
        self.verts = [(float(X)*size, float(Y)*size, float(Z)*size) for X, Y, Z in self.verts]

        self.collision = False
        try:
            for obj in objects:
                if self.checkCollisions(obj):
                    self.collision = True
        except:
            pass

        objects.append(self)

    def rotate(self, X = 0, Y = 0, Z = 0):
        verticesList = []
        for x, y, z in self.verts:
            rad = X*math.pi/180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            y = y*cosa - z*sina
            z = y*sina + z*cosa
            rad = Y*math.pi/180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            z = z*cosa - x*sina
            x = z*sina + x*cosa
            rad = Z*math.pi/180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            x = x*cosa - y*sina
            y = x*sina + y*cosa
            verticesList.append((x, y, z))
        self.verts = verticesList

    def move(self, X = 0, Y = 0, Z = 0):
        self.verts = [(float(x) + X, float(y) + Y, float(z) + Z) for x, y, z in self.verts]

    def place(self, x = 0, y = 0, z = 0):
        self.verts = [(float(x) + float(X)/2, float(y) + float(Y)/2, float(z) + float(Z)/2) for X, Y, Z in self.vertices]

    def subdivide(self, face = 0):
        verticesLength = len(self.vertices)
        face = self.faces[face]
        p1 = self.vertices[face[0]]
        p2 = self.vertices[face[1]]
        p3 = self.vertices[face[2]]
        p4 = self.vertices[face[3]]
        center = (((p1[0] * 0.25) + (p2[0] * 0.25) + (p3[0] * 0.25)), ((p1[1] * 0.25) + (p2[1] * 0.25) + (p3[1] * 0.25)), ((p1[2] * 0.25) + (p2[2] * 0.25) + (p3[2] * 0.25)))
        p12 = (((p1[0] * 0.5) + (p2[0] * 0.5)), ((p1[1] * 0.5) + (p2[1] * 0.5)), ((p1[2] * 0.5) + (p2[2] * 0.5)))
        p23 = (((p2[0] * 0.5) + (p3[0] * 0.5)), ((p2[1] * 0.5) + (p3[1] * 0.5)), ((p2[2] * 0.5) + (p3[2] * 0.5)))
        p34 = (((p3[0] * 0.5) + (p4[0] * 0.5)), ((p3[1] * 0.5) + (p4[1] * 0.5)), ((p3[2] * 0.5) + (p4[2] * 0.5)))
        p41 = (((p4[0] * 0.5) + (p1[0] * 0.5)), ((p4[1] * 0.5) + (p1[1] * 0.5)), ((p4[2] * 0.5) + (p1[2] * 0.5)))
        self.vertices += center, p12, p23, p34, p41
        f1 = (self.vertices.index(p1[-verticesLength:]), self.vertices.index(p12[-verticesLength:]), self.vertices.index(center[-verticesLength:]), self.vertices.index(p41[-verticesLength:]))
        f2 = (self.vertices.index(p12[-verticesLength:]), self.vertices.index(p2[-verticesLength:]), self.vertices.index(p23[-verticesLength:]), self.vertices.index(center[-verticesLength:]))
        f3 = (self.vertices.index(center[-verticesLength:]), self.vertices.index(p23[-verticesLength:]), self.vertices.index(p3[-verticesLength:]), self.vertices.index(p34[-verticesLength:]))
        f4 = (self.vertices.index(p41[-verticesLength:]), self.vertices.index(center[-verticesLength:]), self.vertices.index(p34[-verticesLength:]), self.vertices.index(p4[-verticesLength:]))
        self.faces.remove(face)
        self.faces += f1, f2, f3, f4
        x, y, z = self.pos
        self.verts = [(float(x) + float(X)/2, float(y) + float(Y)/2, float(z) + float(Z)/2) for X, Y, Z in self.vertices]
        self.verts = [(X*self.size, Y*self.size, Z*self.size) for X, Y, Z in self.verts]

    def pixelate(self, face = 0):
        face = self.faces[face]
        facesLength = len(self.faces)
        factor = 4
        self.subdivide(face)
        for i in range(50):
            for i in range(4):
                try:
                    self.subdivide(factor + i)
                except:
                    break
            factor *= 4

    def moveFace(self, face = 0, x = 0, y = 0, z = 0):
        face = self.faces[face]
        for i in face:
            self.verts[i] = (self.verts[i][0] + x, self.verts[i][1] + y, self.verts[i][2] + z)

    def _rotateFace(self, face = 0, X = 0, Y = 0, Z = 0):
        face = self.faces[face]
        vertsList = []
        for i in face:
            vertsList += ((self.verts[i]),)
        verticesList = []
        for x, y, z in vertsList:
            rad = X*math.pi/180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            y = y*cosa - z*sina
            z = y*sina + z*cosa
            rad = Y*math.pi/180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            z = z*cosa - x*sina
            x = z*sina + x*cosa
            rad = Z*math.pi/180
            cosa = math.cos(rad)
            sina = math.sin(rad)
            x = x*cosa - y*sina
            y = x*sina + y*cosa
            verticesList.append((x, y, z))
        for i in face:
            self.verts.remove(self.verts[i])
        self.verts += verticesList
        self.faces.remove(face)
        facesNew = []
        for i in range(self.verts.index(verticesList[0]), self.verts.index(verticesList[len(verticesList) - 1])):
            facesNew.append(i)

    def scaleFace(self, face = 0, x = 0, y = 0, z = 0):
            face = self.faces[face]
            for i in face:
                self.verts[i] = [float(self.verts[i][0])*x, float(self.verts[i][1])*y, float(self.verts[i][2])*z]

    def _extrude(self, face = 0, x = 0, y = 0, z = 0):
            face = self.faces[face]
            self.faces.remove(face)
            verticesIndexes = []
            for i in face:
                self.vertices += (self.vertices[i][0] + x, self.vertices[i][1] + y, self.vertices[i][2] + z)
                verticesIndexes.append(len(self.vertices))
            for i in range(0, len(verticesIndexes), len(face)):
                facesNew = []
                for j in range(len(face)):
                    facesNew.append(self.vertices.index(self.vertices[verticesIndexes[i]]))
                self.faces += facesNew

    def deleteFace(self, face = 0):
        self.faces.remove(face)

    def moveVertex(self, vert = 0, x = 0, y = 0, z = 0):
        self.verts[vert] = (self.verts[vert][0] + x, self.verts[vert][1] + y, self.verts[vert][2] + z)

    def displace(self, face = 0, amount = 1, damping = 1):
        face = self.faces[face]
        for i in face:
            self.verts[i] = (self.verts[i][0] + float(random.randint(-amount, amount))/damping, self.verts[i][1] + float(random.randint(-amount, amount))/damping, self.verts[i][2] + float(random.randint(-amount, amount))/damping)

    def scale(self, x = 1, y = 1, z = 1):
        self.verts = [(float(X)*x, float(Y)*y, float(Z)*z) for X, Y, Z in self.verts]

    def physics(self):
        if "softbody" in self.physic:
            self.displace(0, 1, 100)
        if "gravity" in self.physic:
            self.g -= world.gravity
            self.move(0, self.g, 0)
        if "collider" in self.physic:
            for obj in objects:
                if self.checkCollisions(obj):
                    if "collider" in obj.physic:
                        if "bounce" in obj.physic:
                            self.g = -self.g/2
                        else:
                            self.g = 0
        if "bounce" in self.physic:
            if "gravity" in self.physic:
                self.g += world.gravity/2
        if "force" in self.physic:
            self.move(world.force)

    def checkCollisions(self, obj):
        xMax = max([i[0] for i in self.verts])
        xMin = min([i[0] for i in self.verts])
        yMax = max([i[1] for i in self.verts])
        yMin = min([i[1] for i in self.verts])
        zMax = max([i[2] for i in self.verts])
        zMin = min([i[2] for i in self.verts])
        xMax2 = max([i[0] for i in obj.verts])
        xMin2 = min([i[0] for i in obj.verts])
        yMax2 = max([i[1] for i in obj.verts])
        yMin2 = min([i[1] for i in obj.verts])
        zMax2 = max([i[2] for i in obj.verts])
        zMin2 = min([i[2] for i in obj.verts])
        collision = ((xMax >= xMin2 and xMax <= xMax2) or (xMin <= xMax2 and xMin >= xMin2)) and ((yMax >= yMin2 and yMax <= yMax2) or (yMin <= yMax2 and yMin >= yMin2)) and ((zMax >= zMin2 and zMax <= zMax2) or (zMin <= zMax2 and zMin >= zMin2))
        return collision

    def texture(self, material):
        for pixel in material.pixmap:
            r, g, b, a = pixel[0], pixel[1], pixel[2], pixel[3]
            if material.pixmap.index(pixel) < len(self.color):
                self.color[material.pixmap.index(pixel)] = (r, g, b, a)
            else:
                self.color += (r, g, b, a)

class UI:
    def __init__(self, pos = (0, 0)):
        self.pos = pos
        self.hover = False
        interfaces.append(self)

    def move(self, x = 0, y = 0):
        self.pos = (self.pos[0] + x, self.pos[1] + y)

class UIPolygon(UI):
    def __init__(self, pos = (0, 0), color = (0, 0, 0), *points):
        self.pos = pos
        self.color = color
        self.points = points

class UIText(UI):
    def __init__(self, pos = (0, 0), color = (0, 0, 0), text = "", font = "Sans-Serif", size = 10):
        self.pos = pos
        self.color = color
        self.text = text
        self.font = font
        self.size = size

class Cube(Object):
    vertices = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
    faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)]
    colors = [(100, 0, 0), (50, 50, 10), (100, 50, 50), (50, 100, 50), (50, 100, 100), (50, 50, 100), (50, 10, 100), (50, 100, 100), (50, 100, 10), (10, 50, 100)]

class Plane(Object):
    vertices = [(-1, 0, 1), (1, 0, 1), (1, 0, -1), (-1, 0, -1)]
    faces = [(0, 1, 2, 3)]
    colors = [(100, 0, 0)]

class Point(Object):
    vertices = [(0, 0, 0)]
    faces = [(0)]
    colors = [(100, 0, 0)]

class Line(Object):
    def __init__(self, *args):
        vertices = [args]
        facesArgs = []
        for i in len(args):
            facesArgs += i
        faces = [(facesArgs)]

class Circle(Object):
    vertices = []
    theta = 0
    while theta <= 360:
        x = math.cos(theta)
        y = math.sin(theta)
        vertices += ((x, 0, y),)
        theta += 5
    facesNew = []
    for i in range(len(vertices)):
        facesNew.append(i)
    faces = [tuple(facesNew)]
    colors = [(100, 0, 0)]

class Sphere(Object):
    A = 9
    B = 18
    points = [(0, -1, 0)]
    for zRot in range(A, 100, A):
        X, y = rotate2d((0, -1), zRot/180*math.pi)
        for yRot in range(0, 360, B):
            z, x = rotate2d((0, X), yRot/180*math.pi)
            points += [(x, y, z)]
    points += [(0, 1, 0)]
    a = len(range(A, 180, A))
    b = len(range(0, 360, B))
    n = len(points) - 1
    n2 = b*(a - 1)
    po = []
    for i in range(1, b + 1):
        if i == b:
            po += [(0, i, 1)]
        else:
            po += [(0, i, i + 1)]
    for j in range(0, (a-1) * b, b):
        for i in range(1, b + 1):
            if i == b:
                po += [(i + j, i + b + j, i + 1 + j, 1 + j)]
            else:
                po += [(i + j, i + b + j, i + b + 1 + j, i + 1 + j)]
    for i in range(1, b + 1):
        if i == b:
            po += [(n, i + n2, 1 + n2)]
        else:
            po += [(n, i + n2, i + 1 + n2)]

    vertices = points
    faces = po
    colors = (0, 0, 0), (0, 0, 0), (0, 0, 0)

class Polygon(Object, object):
    def __init__(self, pos = (0, 0, 0), size = 1, parent = None, *args):
        x, y, z = pos
        self.pos = pos
        self.parent = parent
        try:
            if material in materials:
                self.materials = material
            else:
                self.materials = materials[0]
            colors = []
            for color in material.color:
                self.colors += color
        except:
            pass
        self.vertices = [args]
        facesArgs = []
        for i in range(len(args)):
            facesArgs.append(i)
        self.faces = [tuple(facesArgs)]
        self.colors = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        self.verts = [(float(x) + float(X)/2, float(y) + float(Y)/2, float(z) + float(Z)/2) for X, Y, Z in self.vertices[0]]
        self.verts = [(X*size, Y*size, Z*size) for X, Y, Z in self.verts]

class Prism(Object, object):
    def __init__(self, pos = (0, 0, 0), size = 1, length = 0, *args):
        x, y, z = pos
        self.pos = pos
        try:
            if material in materials:
                self.materials = material
            else:
                self.materials = materials[0]
            colors = []
            for color in material.color:
                self.colors += color
        except:
            pass
        self.vertices = [args]
        for i in range(len(args)):
            self.vertices += ((args[i][2], args[i][1] + length, args[i][2]),)
        facesArgs = []
        for i in range(len(args)):
            facesArgs.append(i)
        self.faces = [(facesArgs)]
        facesArgs = ()
        for i in range(len(args), len(args)):
            facesArgs.append(i)
        self.faces += (facesArgs)
        facesArgs = []
        for i in range(0, len(args), 2):
            try:
                p1 = self.vertices[0][i]
                p2 = self.vertices[0][i + len(args)]
                p3 = self.vertices[0][i + 1]
                p4 = self.vertices[0][i + 1 + len(args)]
                facesArgs = (p1, p2, p3, p4)
                self.faces += (facesArgs)
            except:
                pass
        self.colors = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        self.verts = [(float(x) + float(X)/2, float(y) + float(Y)/2, float(z) + float(Z)/2) for X, Y, Z in self.vertices[0]]
        self.verts = [(X*size, Y*size, Z*size) for X, Y, Z in self.verts]

class Light:
    def __init__(self, pos = (0, 0, 0), strength = 10):
        self.pos = pos
        self.strength = strength

        lights.append(self)

class Material:
    def __init__(self, color = (0, 0, 0), emmision = 1):
        self.emmision = emmision
        try:
            self.color = colorChange(color, self.emmision)
        except:
            self.color = color

        materials.append(self)

class Texture(Material):
    def __init__(self, path):
        self.image = Image.open(str(path), "r")
        self.pixmap = list(self.image.getdata())

        materials.append(self)

class ParticleSystem:
    def __init__(self, obj, pos = (0, 0, 0), spread = 0, interval = 10, movement = 10):
        global objects
        self.obj = obj
        self.tick = 0
        self.objectsLength = len(objects)
        self.spread = spread
        self.interval = interval
        self.movement = movement
        self.objects = []
        objects.append(obj)
        for i in self.objects:
            self.objects.remove(i)
        for i in range(len(objects) - self.objectsLength):
            self.objects.append(objects[i])

    def step(self):
        global objects
        self.tick += 1
        if random.randint(-1, 1) == 1:
            self.rand = 1
        else:
            self.rand = -1
        if self.tick % int(self.interval) == 0:
            objects.append(self.obj)
            for i in self.objects:
                self.objects.remove(i)
            for i in range(len(objects) - self.objectsLength):
                self.objects.append(objects[i])
        for i in range(len(objects) - self.objectsLength):
            objectCurrent = objects[self.objectsLength + i]
            objectCurrent.verts = [(float(x), float(y) + self.movement, float(z)) for x, y, z in objectCurrent.verts]

    def clear(self):
        global objects
        for i in range(len(objects) - self.objectsLength):
            objects.delete(objects[self.objectsLength + i])

class PhysicsWorld:
    def __init__(self, gravity = 0, force = (0, 0, 0)):
        global world
        world = self
        self.gravity = gravity
        self.force = force

class Mouse:
    def __init__(self, pos = (0, 0), visible = 0, lock = 1, cursor = pygame.cursors.arrow):
        self.visible = visible
        self.lock = lock
        self.cursor = cursor
        pygame.mouse.set_cursor(*self.cursor)
        pygame.mouse.set_visible(int(visible))
        pygame.event.set_grab(int(lock))
        pygame.mouse.set_pos(pos)
        self.pos = pygame.mouse.get_pos()

def init(width = 400, height = 400):
    global screen, cx, cy, clock, w, h
    pygame.init()
    w, h = width, height
    cx, cy = w//2, h//2
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    pygame.event.get()
    pygame.mouse.get_rel()

#cube = Cube((1, 1, 1), 1, 0, None, ["gravity", "softbody"])

#objects = [cube, Plane((0, 1, 0), 1), Polygon((0, 0, 0), 3, None, (0, 0, 0), (1, 1, 1), (1, 0, 1), (0, 1, 1)), Circle((0, 5, 0))]
#lights = [Light((0, 3, 0), 10)]
#materials = [Material((255, 100, 255))]
#interfaces = [UIPolygon((0, 0), (100, 100, 100), (0, 10), (5, 10), (10, 0), (0, 0), (0, 5)), UIText((0, 0), (0, 100, 0), "Hi", "Serif", 100)]

def colorChange(rgb, scale = 1):
    r = rgb[0]/scale
    g = rgb[1]/scale
    b = rgb[2]/scale
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255
    return (r, g, b)

def open(file):
    file = open(str(file), "r+")
    file.write("pyn")
    info = file.readlines()
    lines = []
    for line in info:
        lines.append(line)
    objectNew = Object()
    objectNew.pos = tuple(lines[0])
    objectNew.vertices = list(lines[1])
    objectNew.verts = list(lines[2])
    objectNew.faces = list(lines[3])
    objectNew.colors = list(lines[4])
    objectNew.size = float(lines[5])
    objectNew.parent = eval(lines[6])
    objectNew.physic = list(lines[7])
    objectNew.g = float(lines[8])
    objects.append(objectNew)

def download(name, obj):
    file = open(str(name) + ".pyn", "w+")
    file.write(str(obj.pos) + "\n")
    file.write(str(obj.vertices) + "\n")
    file.write(str(obj.verts) + "\n")
    file.write(str(obj.faces) + "\n")
    file.write(str(obj.colors) + "\n")
    file.write(str(obj.size) + "\n")
    file.write(str(obj.parent) + "\n")
    file.write(str(obj.physic) + "\n")
    file.write(str(obj.g) + "\n")
    return file

def window(camera, background = (255, 255, 255), light = True):

    dt = 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        camera.events(event)

    if light == True:
        screen.fill(colorChange(background, 10/lights[0].strength*10))
    else:
        screen.fill(background)

    for obj in objects:
        faceList = []
        faceColor = []
        depth = []
        vertList = []
        screenCoords = []
        for x, y, z in obj.verts:
            x -= camera.pos[0]
            y -= camera.pos[1]
            z -= camera.pos[2]
            x, z = rotate2d((x, z), camera.rot[1])
            y, z = rotate2d((y, z), camera.rot[0])
            vertList += [(x, y, z)]
            f = 200/z
            x, y = x*f, y*f
            screenCoords += [(cx + int(x), cy + int(y))]

        for f in range(len(obj.faces)):
            face = obj.faces[f]
            onScreen = False
            for i in face:
                x, y = screenCoords[i]
                if vertList[i][2] > 0 and x > 0 and x < w and y > 0 and y < h:
                    onScreen = True
                    break
            if onScreen:
                for light in lights:
                    lightDistance = pow((pow((light.pos[0] - obj.pos[0]), 2) + pow((light.pos[1] - obj.pos[1]), 2) + pow((light.pos[2] - obj.pos[2]), 2)), 0.5)
                    lightColor = colorChange(obj.colors[f], lightDistance/light.strength*10)
                faceColor += [lightColor]
                coords = [screenCoords[i] for i in face]
                faceList += [coords]
                depth += [sum(sum(vertList[j][i] for j in face)**2 for i in range(3))]
        order = sorted(range(len(faceList)), key = lambda i: depth[i], reverse = 1)
        for i in order:
            pygame.draw.polygon(screen, faceColor[i], faceList[i])

        if not obj.parent == None:
            obj.place(obj.pos[0] + obj.parent.pos[0], obj.pos[1] + obj.parent.pos[1], obj.pos[2] + obj.parent.pos[2])

    for ui in interfaces:
        if ui.__class__.__name__ == "UIPolygon":
            uiCurrent = pygame.draw.polygon(screen, ui.color, ui.points)
            ui.move(ui.pos[0], ui.pos[1])
        elif ui.__class__.__name__ == "UIText":
            pygame.font.init()
            font = pygame.font.SysFont(str(ui.font), int(ui.size))
            text = font.render(str(ui.text), False, ui.color)
            screen.blit(text, ui.pos)
        if uiCurrent.collidepoint(pygame.mouse.get_pos()):
            ui.hover = True
        else:
            ui.hover = False

    pygame.display.flip()
    key = pygame.key.get_pressed()
    camera.update(dt, key)
