import pygame
import math
import time

def d2((x, y), universe):
    return x + universe['max_dim'], universe['max_dim'] - y

def d3_to_d2((x, y, z), universe):
    xz = -z * math.sin(universe['z_angle'] * math.pi / 180)
    yz = -z * math.cos(universe['z_angle'] * math.pi / 180)
    return x + xz, y + yz

def d3((x, y, z)):
    return d2(d3_to_d2((x, y, z), universe), universe)
              
def line_d2(p0, p1, color, universe):
    pygame.draw.line(universe['screen'], color, d2(p0, universe), d2(p1, universe))

def line_d3(p30, p31, color, universe):
    p20 = d3_to_d2(p30, universe)
    p21 = d3_to_d2(p31, universe)
    line_d2(p20, p21, color, universe)

def draw_axes(universe):
    axis_color = (0, 128, 255)
    line_d3((-universe['max_axis'], 0, 0), (universe['max_axis'], 0, 0), axis_color, universe)
    line_d3((0, -universe['max_axis'], 0), (0, universe['max_axis'], 0), axis_color, universe)
    line_d3((0, 0, -universe['max_axis']), (0, 0, universe['max_axis']), axis_color, universe)

def draw_3d_cube(universe, size):
    color = (255, 255, 255)
    vertices = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 2), (4, 7), (7, 6), (6, 5), (6, 1), (7, 0)]
    for edge in edges:
        real_vert0 = [size * coord for coord in vertices[edge[0]]]
        real_vert1 = [size * coord for coord in vertices[edge[1]]]
        line_d3(real_vert0, real_vert1, color, universe)

def main():
    pygame.init()
    universe = {'max_dim': 225, 'max_axis': 200, 'z_angle': -70}
    universe['screen'] = pygame.display.set_mode((2 * universe['max_dim'], 2 * universe['max_dim']), pygame.DOUBLEBUF)
    
    done = False
    while not done:
        draw_axes(universe)
        draw_3d_cube(universe, 50)

        universe['z_angle'] += 0
        time.sleep(0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pygame.display.flip()

main()

         
