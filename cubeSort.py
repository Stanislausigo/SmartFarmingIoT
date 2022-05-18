# Alg. 2: CubeSort
# --------------------------------------------------------
# 
# Koding disini
import functools
import math
from multiprocessing.dummy import Array
import timeit

start = timeit.default_timer() #waktu mulai
class cubeSort :
    
    def sortArray( arr,  n) :
        ar = [None] * (n)
        i = 0
        while (i < n) :
            ar[i] = arr[i]
            i += 1
        def compare(a,  b) :
            x = int(math.pow(a,3))
            y = int(math.pow(b,3))
            return -1 if (x < y) else 1
        sorted_ar = sorted(ar, key=functools.cmp_to_key(compare))
        print("Nilai Array awal", end="\n")
        printList(ar)
        print("Nilai Array setelah disorting: ", end="\n")
        printList(sorted_ar)
    def main( args) :
        arr = [4, -2, 0, 5, -9, 3]
        n = len(arr)
        cubeSort.sortArray(arr, n)
if __name__=="__main__":
    cubeSort.main([])
    stop = timeit.default_timer() #waktu selesai
    lama_eksekusi = stop - start #lama eksekusi dalam detik
    print("Lama eksekusi: ",lama_eksekusi,"detik")