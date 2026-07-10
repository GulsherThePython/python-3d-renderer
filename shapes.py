def cube(centerx, centery, centerz, side_length):
    half = side_length / 2
    vertices = [centerx - half, centery - half, centerz - half,
                centerx - half, centery - half, centerz + half,
                centerx - half, centery + half, centerz - half,
                centerx - half, centery + half, centerz + half,
                centerx + half, centery - half, centerz - half,
                centerx + half, centery - half, centerz + half,
                centerx + half, centery + half, centerz - half,
                centerx + half, centery + half, centerz + half
                ]

    return vertices
