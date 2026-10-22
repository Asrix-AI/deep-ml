def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    transpose = zip(*a)
    transpose_list = [list(a) for a in transpose]
    return transpose_list