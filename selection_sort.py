import random
import time

def selection_sort(unsorted_list):
    sorted_list = unsorted_list
    smallest_number_index = 1
    for i in range(len(sorted_list)):
        smallest_number = sorted_list[i]
        for n in range(i+1,len(sorted_list)):
            if sorted_list[n] < smallest_number:
                smallest_number_index = int(n)
                smallest_number = sorted_list[n]
        #print(n)
        #print(smallest_number_index)
        #print()
        #print(sorted_list[smallest_number_index])
        #print(sorted_list[i])
        if smallest_number != sorted_list[i]:
            sorted_list[i], sorted_list[smallest_number_index] = sorted_list[smallest_number_index], sorted_list[i]

    return sorted_list


if __name__ == "__main__":
    l = []
    for n in range(9999):
        l.append(random.randint(0,999))
    start = time.time()
    print(selection_sort(l))
    end = time.time()
    print(end-start)
