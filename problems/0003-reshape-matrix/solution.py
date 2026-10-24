import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a = np.array(a)
	s1, s2 = a.shape
	ns1, ns2 = new_shape

	reshaped_matrix = []
	if s1*s2 == ns1*ns2:
		reshaped_matrix = (a.reshape(new_shape)).tolist()
		return reshaped_matrix
	else:
		return reshaped_matrix