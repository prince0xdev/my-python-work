""" Binary Search """
def binary_search(search_list, low, high, key):
    
    #low=0 and hight=13
    
    # Check base case
    if high > low:
        #Yes 13 > 0
        mid = (high + low) // 2
        # mid = (13 + 0)//2 = 6
        
        # If element is present at the middle itself (base case)
        if search_list[mid] == key:
            #searchlist[6]==48 ---> True
            return mid
        
        # Recursive case: check which subarray must be checked
        # Right subarray
        elif key > search_list[mid]:
             #'48 > 27 ---> False
            return binary_search(search_list, mid + 1, high, key)
        # Left subarray
        else:
            return binary_search(search_list, low, mid - 1, key)
    else:
    # Key not found (other base case)
        return "Not found"
    
    
# Test list
in_list = [1, 3, 13, 16, 19, 22, 27, 32, 48, 66, 78, 99, 111, 122]
# Call binary search function
print(binary_search(in_list, 0, len(in_list)-1, 48)) # Key exists at index 8


print(binary_search(in_list, 0, len(in_list)-1, 86)) # Key does not exist