from draw import draw_wireframe
from rotate import rotate_points_along_axes
from translate import translate_vertices

def render_scene(scene, screen, camera):
    for obj in scene:
        # Rotate the cube vertices
        vertices = rotate_points_along_axes(obj["vertices"], obj["angle"], 0, 0)

        # Translate the cube to its position
        vertices = translate_vertices(vertices, obj["position"])

        # Apply camera transformations
        vertices = translate_vertices(vertices, camera["position"])

        # Apply camera rotations
        vertices = rotate_points_along_axes(vertices, 
            camera["rotation"][0],
            camera["rotation"][1],
            camera["rotation"][2]
        )

        # Draw the cube wireframe
        draw_wireframe(screen, vertices, fov=90, window_width=400, edges=obj["edges"])