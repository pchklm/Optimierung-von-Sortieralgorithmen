import random
import time

def insertion_sort(unsorted_list):
    sorted_list = [unsorted_list[0]]


    for i in range(1,len(unsorted_list)):
        inserted = False
        for n in range(len(sorted_list)):
            if unsorted_list[i] < sorted_list[n]:
                sorted_list.insert(n, unsorted_list[i])
                inserted = True
                break
        if not inserted:
            sorted_list.append(unsorted_list[i])

    return sorted_list


if __name__ == "__main__":
    l = []
    for n in range(9999):
        l.append(random.randint(0,9999))
    start = time.time()
    print(insertion_sort(l))
    end = time.time()
    print(end-start)
            
