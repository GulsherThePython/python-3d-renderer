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

def cube_edges():
    edges = [
        # Back
        0, 1, 
        1, 3, 
        3, 2, 
        2, 0,

        # Front
        4, 5, 
        5, 7, 
        7, 6, 
        6, 4,
        
        # Connecting edges
        0, 4, 
        1, 5, 
        2, 6, 
        3, 7   
    ]
    return edges