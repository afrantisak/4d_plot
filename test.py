import pygame
import math

max_dim = 225
max_line = 200
z_angle = -65

pygame.init()
screen = pygame.display.set_mode((2 * max_dim, 2 * max_dim))
axis_color = (0, 128, 255)
done = False

def d2((x, y)):
    return x + max_dim, max_dim - y

def d3_to_d2((x, y, z)):
    xz = -z * math.sin(z_angle * math.pi / 180)
    yz = -z * math.cos(z_angle * math.pi / 180)
    return x + xz, y + yz

def d3((x, y, z)):
    return d2(d3_to_d2(x, y, z))
              
def line_d2(p0, p1, color):
    pygame.draw.line(screen, color, d2(p0), d2(p1))

def line_d3(p30, p31, color):
    p20 = d3_to_d2(p30)
    p21 = d3_to_d2(p31)
    line_d2(p20, p21, color)

# draw axes
line_d3((-max_line, 0, 0), (max_line, 0, 0), axis_color)
line_d3((0, -max_line, 0), (0, max_line, 0), axis_color)
line_d3((0, 0, -max_line), (0, 0, max_line), axis_color)

# draw 3d cube
cube_size = 100
cube_color = (255, 255, 255)
cube_vertices = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]
cube_vertices = [[cube_size * coord for coord in vertex] for vertex in cube_vertices]

def edge(v0, v1):
    line_d3(cube_vertices[v0], cube_vertices[v1], cube_color)

edge(0, 1)
edge(1, 2)
edge(2, 3)
edge(3, 0)
edge(3, 4)
edge(4, 5)
edge(5, 2)
edge(4, 7)
edge(7, 6)
edge(6, 5)
edge(6, 1)
edge(7, 0)


    
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    pygame.display.flip()

         
