import random
import time
import math


def merge_sort(unsorted_list):  
    unsorted_list = [[unsorted_list[i]] for i in range(len(unsorted_list))]
    for _ in range(math.ceil(math.log(2, len(unsorted_list)))):
        



        return unsorted_list


if __name__ == "__main__":

    l = []
    for i in range(9999):
        l.append(random.randint(0,9999))
    start = time.time()
    print(merge_sort(l))
    end = time.time()
    print(end-start)