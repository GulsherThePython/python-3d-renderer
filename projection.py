def project_points(point, focal_length, center_x, center_y):
    x, y, z = point

    x_proj = (focal_length * x) / (focal_length + z) + center_x
    y_proj = -(focal_length * y) / (focal_length + z) + center_y

    return (x_proj, y_proj)