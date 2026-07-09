from projection import project_points
import pygame

def draw_points(screen, x_points, y_points, z_points, fov, window_width):
    projected_points = []
    for i in range(len(x_points)):
        projected_points.append((project_points((x_points[i], y_points[i], z_points[i]), fov, window_width)))
        projected_points[i] = (projected_points[i][0] + window_width / 2, projected_points[i][1] + window_width / 2)

    for x, y in projected_points:
        screen_x = int(x)
        screen_y = int(y)
        pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), 2)

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
