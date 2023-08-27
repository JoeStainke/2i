def remove_duplicates(nums):
    """
    Removes any duplicate numbers from the array
    by creating a dictionary using the array items as keys
    (as dictionaries cannot have duplicate keys),
    then turning it back into an array.
    """
    array_as_list = list(dict.fromkeys(nums))
    array_without_duplicates = list(dict.fromkeys(array_as_list)) 
    return array_without_duplicates



def sum_pairs(nums, x):
    """
    A function that looks for pairs of numbers in an array that add up to X.
    Returns the count of how many such unique pairs it finds.
    """

    nums = remove_duplicates(nums) # runs the function to remove any duplicates

    count = 0 # initialise the counter
    
    n = len(nums)

    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == x:
                count += 1

    return count