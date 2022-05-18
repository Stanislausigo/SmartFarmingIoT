# Alg. 1: MergeSort
# --------------------------------------------------------
# Koding disini
# Python program for implementation of MergeSort
import timeit

start = timeit.default_timer() #waktu mulai
def mergeSort(arr):
	if len(arr) > 1:

		# Mencari nilai tengah pada array
		mid = len(arr)//2
		# Memisah array element dan beri penanda sisi kiri
		L = arr[:mid]
		# Memisah array element dan beri penanda sisi kanan
		R = arr[mid:]
		# Melakukan sorting di sisi kiri
		mergeSort(L)
		# Melakukan sorting di sisi kanan
		mergeSort(R)
		i = j = k = 0
		# Lakukan komparasi dari kedua sisi array
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		# Check apakah masih ada element array yang tersisa
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

if __name__ == '__main__':
	arr = [4, -2, 0, 5, -9, 3]
	print("Nilai Array awal", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Nilai Array setelah disorting: ", end="\n")
	printList(arr)
	stop = timeit.default_timer() #waktu selesai
	lama_eksekusi = stop - start #lama eksekusi dalam detik
	print("Lama eksekusi: ",lama_eksekusi,"detik")