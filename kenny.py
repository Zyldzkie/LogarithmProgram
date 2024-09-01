from difflib import SequenceMatcher

def is_close_match(target, candidate, min_consecutive=4):
    """Check if there are at least `min_consecutive` letters in sequence that match."""
    # Ensure both strings are at least min_consecutive in length
    if len(target) < min_consecutive or len(candidate) < min_consecutive:
        return False
    
    # Iterate over target and see if a substring of length min_consecutive exists in the candidate
    for i in range(len(target) - min_consecutive + 1):
        if target[i:i + min_consecutive] in candidate:
            return True
    return False

def binary_search_closest(arr, target):
    left, right = 0, len(arr) - 1
    closest_match = None
    highest_similarity = 0.0
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Print the current half of the array being searched
        print("Current search range:", arr[left:right + 1])
        
        # Calculate similarity using SequenceMatcher
        similarity = SequenceMatcher(None, target, arr[mid]).ratio()
        
        # If the current word is a close match based on our custom check
        if is_close_match(target, arr[mid]):
            if similarity > highest_similarity:
                highest_similarity = similarity
                closest_match = arr[mid]
        
        # Exact match found
        if arr[mid] == target:
            return arr[mid]
        
        # Move left or right based on lexicographical order
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return closest_match

# Example usage
arr = sorted(["Angel", "Lexine", "Maria", "Joanna", "Anna", "Alex", "Janna", "Mia", "Jennefer", "Chelsea", "Mariel", "Jinjher", "Licelle", "Dion"])
target = input("Enter name: ")  # Misspelled target

closest_match = binary_search_closest(arr, target)

if closest_match:
    print(f"Closest match found: {closest_match}")
else:
    print("No close match found in the array")
