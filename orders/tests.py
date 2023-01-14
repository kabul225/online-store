# from django.test import TestCase

# Create your tests here.

def binary_search(my_list, num):
    low = 0
    high = len(my_list)+1
    while low<=high:
        mid = (low+high)//2
        guess = my_list[mid]
        if guess==num:
            return mid
        if guess>num:
            high = mid-1
        else:
            high = mid+1
    return None
print(binary_search([1,3,5,7,9,10],3))