# construa uma classe chamada ordenador
# com um método chamado bubble_sort 
# que faça a ordenação de um vetor com o algoritmo bubble_sort.

class Ordenador:
    
    def bubble_sort(self, array):
        for i in range(0, len(array)):
            for j in range(0, len(array)-1):
                if array[j] > array[j+1]:               
                    aux = array[j]
                    array[j] = array[j+1]
                    array[j+1] = aux
        return array


a = Ordenador().bubble_sort([3,5,9,4,1,2])
print(a)
