import random
import time

def bubble_sort(unsorted_list):
    for n in range(len(unsorted_list), 0, -1):
        for i in range(len(unsorted_list[:n])-1):

            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]


    return unsorted_list


if __name__ == "__main__":


    l = []
    for n in range(9999):
        l.append(random.randint(0,9999))
    start = time.time()
    print(bubble_sort(l))
    end = time.time()
    print(end-start)
    for i in range(len(l)-1):
        assert l[i] <= l[i+1]
   
