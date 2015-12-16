import pygame
import math
import time

class Universe():
    def __init__(self, max_dim, max_axis, z_angle, z_flat):
        self.max_dim = max_dim
        self.max_axis = max_axis
        self.z_angle = z_angle
        self.z_flat = z_flat
        self.screen = pygame.display.set_mode((2 * self.max_dim, 2 * self.max_dim), pygame.DOUBLEBUF)

    def point_2d(self, (x, y)):
        return x + self.max_dim, self.max_dim - y

    def point_3d_to_2d(self, (x, y, z)):
        xz = -z * math.sin(self.z_angle * math.pi / 180)
        yz = -z * self.z_flat * math.cos(self.z_angle * math.pi / 180)
        return x + xz, y + yz

    def point_3d(self, (x, y, z)):
        return self.point_2d(point_3d_to_2d((x, y, z)))
              
    def line_2d(self, p0, p1, color):
        pygame.draw.line(self.screen, color, self.point_2d(p0), self.point_2d(p1))
        
    def line_3d(self, p30, p31, color):
        p20 = self.point_3d_to_2d(p30)
        p21 = self.point_3d_to_2d(p31)
        self.line_2d(p20, p21, color)

    def draw_3d_axes(self, color):
        self.line_3d((-self.max_axis, 0, 0), (self.max_axis, 0, 0), color)
        self.line_3d((0, -self.max_axis, 0), (0, self.max_axis, 0), color)
        self.line_3d((0, 0, -self.max_axis), (0, 0, self.max_axis), color)

    def draw_3d_shape(self, vertices, edges, color):
        for edge in edges:
            real_vert0 = vertices[edge[0]]
            real_vert1 = vertices[edge[1]]
            self.line_3d(vertices[edge[0]], vertices[edge[1]], color)

    def draw_3d_cube(self, size, color):
        vertices = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)]
        vertices = [[size * coord for coord in vertex] for vertex in vertices]
        edges = [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5), (5, 2), (4, 7), (7, 6), (6, 5), (6, 1), (7, 0)]
        self.draw_3d_shape(vertices, edges, color)

def main():
    pygame.init()
    universe = Universe(max_dim=225, max_axis=200, z_angle=-30, z_flat=0.3)
    
    done = False
    while not done:
        universe.screen.fill((0, 0, 0))
        universe.draw_3d_axes((0, 128, 255))
        universe.draw_3d_cube(75, (255, 255, 255))

        universe.z_angle += 1
        time.sleep(0.1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pygame.display.flip()

main()

