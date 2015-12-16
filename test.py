import pygame
import math
import time

def point_2d((x, y), universe):
    return x + universe['max_dim'], universe['max_dim'] - y

def point_3d_to_2d((x, y, z), universe):
    xz = -z * math.sin(universe['z_angle'] * math.pi / 180)
    yz = -z * universe['z_flat'] * math.cos(universe['z_angle'] * math.pi / 180)
    return x + xz, y + yz

def point_3d((x, y, z)):
    return point_2d(point_3d_to_2d((x, y, z), universe), universe)
              
def line_d2(p0, p1, color, universe):
    pygame.draw.line(universe['screen'], color, point_2d(p0, universe), point_2d(p1, universe))

def line_d3(p30, p31, color, universe):
    p20 = point_3d_to_2d(p30, universe)
    p21 = point_3d_to_2d(p31, universe)
    line_d2(p20, p21, color, universe)

def draw_axes(universe):
    axis_color = (0, 128, 255)
    line_d3((-universe['max_axis'], 0, 0), (universe['max_axis'], 0, 0), axis_color, universe)
    line_d3((0, -universe['max_axis'], 0), (0, universe['max_axis'], 0), axis_color, universe)
    line_d3((0, 0, -universe['max_axis']), (0, 0, universe['max_axis']), axis_color, universe)

def draw_3d_shape(universe, vertices, edges, color):
    for edge in edges:
        real_vert0 = vertices[edge[0]]
        real_vert1 = vertices[edge[1]]
        line_d3(vertices[edge[0]], vertices[edge[1]], color, universe)

def draw_3d_cube(universe, size, color):
    vertices = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]
    vertices = [[size * coord for coord in vertex] for vertex in vertices]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 2), (4, 7), (7, 6), (6, 5), (6, 1), (7, 0)]
    draw_3d_shape(universe, vertices, edges, color)

def main():
    pygame.init()
    universe = {'max_dim': 225, 'max_axis': 200, 'z_angle': -30, 'z_flat': 0.3}
    universe['screen'] = pygame.display.set_mode((2 * universe['max_dim'], 2 * universe['max_dim']), pygame.DOUBLEBUF)
    
    done = False
    while not done:
        draw_axes(universe)
        draw_3d_cube(universe, 75, (255, 255, 255))

        universe['z_angle'] += 0
        time.sleep(0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pygame.display.flip()

main()

