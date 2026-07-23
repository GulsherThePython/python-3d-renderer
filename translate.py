from matrix import add_vectors

def translate_point(point, offset):
    return add_vectors(point, offset)

def translate_vertices(vertices, offset):
    translated_vertices = []
    for i in range(len(vertices) // 3):
        point = [
            vertices[i * 3],
            vertices[i * 3 + 1],
            vertices[i * 3 + 2]
        ]
        translated_point = translate_point(point, offset)
        for j in range(3):
            translated_vertices.append(translated_point[j])

    return translated_vertices