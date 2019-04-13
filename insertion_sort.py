import random
 
 
def make_array():
	return [random.randint(0, 100) for _ in range(10)]


def insertion_sort(input_array):
	for j in range(1, len(input_array)):
		key = input_array[j]
		i = j - 1
		while i > -1 and input_array[i] > key:
			input_array[i + 1] = input_array[i]
			i -= 1
		input_array[i+1] = key
	return input_array

if __name__ == "__main__":
	array = make_array()
	print(array)
	sorted_array = insertion_sort(array)
	print(sorted_array)
