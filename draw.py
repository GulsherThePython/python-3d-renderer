from projection import project_points
import pygame

def draw_cube(
        screen, vertex1, vertex2, vertex3, 
        vertex4, vertex5, vertex6, vertex7,
        vertex8, fov, window_width
        ):
    
    projected_points = []
    for vertex in [
        vertex1, vertex2, vertex3, vertex4,
        vertex5, vertex6, vertex7, vertex8
    ]:
        x_proj, y_proj = project_points(vertex, fov, window_width)
        if x_proj is not None and y_proj is not None:
            projected_points.append((x_proj + window_width / 2, y_proj + window_width / 2))
        else:
            projected_points.append(None)

    pygame.draw.line(screen, (255, 255, 255), projected_points[0], projected_points[1])
    pygame.draw.line(screen, (255, 255, 255), projected_points[1], projected_points[2])
    pygame.draw.line(screen, (255, 255, 255), projected_points[2], projected_points[3])
    pygame.draw.line(screen, (255, 255, 255), projected_points[3], projected_points[0])
    pygame.draw.line(screen, (255, 255, 255), projected_points[4], projected_points[5])
    pygame.draw.line(screen, (255, 255, 255), projected_points[5], projected_points[6])
    pygame.draw.line(screen, (255, 255, 255), projected_points[6], projected_points[7])
    pygame.draw.line(screen, (255, 255, 255), projected_points[7], projected_points[4])
    pygame.draw.line(screen, (255, 255, 255), projected_points[0], projected_points[4])
    pygame.draw.line(screen, (255, 255, 255), projected_points[1], projected_points[5])
    pygame.draw.line(screen, (255, 255, 255), projected_points[2], projected_points[6])
    pygame.draw.line(screen, (255, 255, 255), projected_points[3], projected_points[7])
