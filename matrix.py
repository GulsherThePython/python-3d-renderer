def multiply_matrix_to_vector(m, v):
    a = m[0]
    b = m[1]
    c = m[2]
    d = m[3]

    x = v[0]
    y = v[1]

    return [a*x + b*y, c*x + d*y]