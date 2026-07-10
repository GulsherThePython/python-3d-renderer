from math import tan, radians

def project_points(point, fov, window_width):
    x, y, z = point
    if z <= 0:
        return (None, None)

    near = window_width / tan(radians(fov) / 2)

    x_proj = (near * x) / z
    y_proj = -(near * y) / z

    return (x_proj, y_proj)