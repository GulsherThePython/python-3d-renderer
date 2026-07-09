from math import tan, radians

def project_points(point, fov, window_width):
    x, y, z = point

    near = window_width / tan(radians(fov) / 2)

    x_proj = (near * x) / (near + z)
    y_proj = -(near * y) / (near + z)

    return (x_proj, y_proj)