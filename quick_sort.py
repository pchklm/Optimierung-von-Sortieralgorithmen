import time
import random


def quick_sort(unsorted_list, l=0, r=None):
    #print(unsorted_list[l:r])
    if r == None:
        r = len(unsorted_list)-1
    #print(len(unsorted_list[l:r]))
    if len(unsorted_list[l:r])+1 == 1:
       # print("1")
        pass
    elif len(unsorted_list[l:r])+1 == 2:
       # print("2")
        if unsorted_list[l] > unsorted_list[r]:
            unsorted_list[l], unsorted_list[r] = unsorted_list[r], unsorted_list[l]
    else:
        #print("3")
        pivot = unsorted_list[r]
        pivot_index = r
        left_index = l
        r-=1
        first_loop = True
        while r >= l:
            if not first_loop:
                l+=1
                r-=1
            else:
                first_loop = False

            while unsorted_list[r] > pivot:
                if r < l:
                    break
                else:
                    r-=1
            while unsorted_list[l] < pivot:
                if r < l:
                    break
                else:
                    l+=1
            if r >=l:
                unsorted_list[l], unsorted_list[r] = unsorted_list[r], unsorted_list[l]

        split = l
        unsorted_list[split], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[split]
        if split == left_index:
            split = pivot_index
        #print(pivot_index - left_index)
        if pivot_index-left_index > 1:
            
            quick_sort(unsorted_list, left_index, split-1)
            quick_sort(unsorted_list, split, pivot_index)


if __name__ == "__main__":

    l = []
    for _ in range(9999):
        l.append(random.randint(0,9999))
    start = time.time()
    quick_sort(l)
    end = time.time()
    for i in range(len(l)-1):
        assert l[i] <= l[i+1]
    print(end-start)
    
    print(l)

