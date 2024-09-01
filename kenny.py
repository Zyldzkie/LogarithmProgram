from difflib import SequenceMatcher
import csv

#CSV FILE
# Initialize an empty list to store the rows
arr = []

# Open and read the CSV file
with open('song_name.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over the rows in the CSV file
    for row in csv_reader:
        for element in row:
            arr.append(element)
           


#CSV FILE END
def is_close_match(target, candidate, min_consecutive=4):
    """Check if there are at least `min_consecutive` letters in sequence that match."""
    # Ensure both strings are at least min_consecutive in length
    if len(target) < min_consecutive or len(candidate) < min_consecutive:
        return False
    
    # Convert both strings to lowercase to ignore case sensitivity
    target, candidate = target.lower(), candidate.lower()
    
    # Iterate over target and see if a substring of length min_consecutive exists in the candidate
    for i in range(len(target) - min_consecutive + 1):
        if target[i:i + min_consecutive] in candidate:
            return True
    return False

def binary_search_closest(arr, target):
    left, right = 0, len(arr) - 1
    closest_match = None
    highest_similarity = 0.0
    iteration = 1
    
    # Convert the target to lowercase for case-insensitive comparison
    target_lower = target.lower()
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Print the current half of the array being searched
        print(f"Iteration {iteration}: First half of current search range: {arr[left:mid+1]}")
        iteration += 1
        
        # Convert the current middle element to lowercase for comparison
        mid_element_lower = arr[mid].lower()
        
        # Calculate similarity using SequenceMatcher on lowercase strings
        similarity = SequenceMatcher(None, target_lower, mid_element_lower).ratio()
        
        # If the current word is a close match based on our custom check
        if is_close_match(target_lower, mid_element_lower):
            if similarity > highest_similarity:
                highest_similarity = similarity
                closest_match = arr[mid]  # Store the original case
        
        # Exact match found
        if mid_element_lower == target_lower:
            return arr[mid]  # Return the original case
        
        # Move left or right based on lexicographical order (ignoring case)
        elif mid_element_lower < target_lower:
            left = mid + 1
        else:
            right = mid - 1
    
    return closest_match

# Example usage

target = input("Enter name: ")  # Misspelled target

closest_match = binary_search_closest(arr, target)

if closest_match:
    print(f"Closest match found: {closest_match}")
else:
    print("No close match found in the array")
