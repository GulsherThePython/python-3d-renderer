def cube(centerx, centery, centerz, side_length):
    half = side_length / 2
    v1 = (centerx - half, centery - half, centerz - half)
    v2 = (centerx - half, centery - half, centerz + half)
    v3 = (centerx - half, centery + half, centerz - half)
    v4 = (centerx - half, centery + half, centerz + half)
    v5 = (centerx + half, centery - half, centerz - half)
    v6 = (centerx + half, centery - half, centerz + half)
    v7 = (centerx + half, centery + half, centerz - half)
    v8 = (centerx + half, centery + half, centerz + half)

    return v1, v2, v3, v4, v5, v6, v7, v8