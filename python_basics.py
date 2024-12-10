from collections import Counter

def sort_by_frequency(s):
    # Count the frequency of each character
    freq = Counter(s)
    
    # Sort characters by frequency and then alphabetically
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Build the sorted string
    sorted_string = ''.join(char * count for char, count in sorted_chars)
    
    return sorted_string

# Example usage:
s = "tree"
sorted_s = sort_by_frequency(s)
print(sorted_s)  # Output: "eert"