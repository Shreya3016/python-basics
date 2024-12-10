<<<<<<< HEAD
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
=======
public class StudentRank {
    private String[] students;
    private int[] ranks;

    // Constructor
    public StudentRank(String[] students, int[] ranks) {
        this.students = students;
        this.ranks = ranks;
    }

    // Method to get the highest-ranked student
    public String highestRank() {
        int maxRankIndex = 0;
        for (int i = 1; i < ranks.length; i++) {
            if (ranks[i] > ranks[maxRankIndex]) {
                maxRankIndex = i;
            }
        }
        return students[maxRankIndex];
    }

    // Method to get the lowest-ranked student
    public String lowestRank() {
        int minRankIndex = 0;
        for (int i = 1; i < ranks.length; i++) {
            if (ranks[i] < ranks[minRankIndex]) {
                minRankIndex = i;
            }
        }
        return students[minRankIndex];
    }

    public static void main(String[] args) {
        String[] students = {"Taylor", "Wesley", "Jordan"};
        int[] ranks = {1, 5, 3};
        StudentRank sr = new StudentRank(students, ranks);

        System.out.println(sr.highestRank()); // Output: Wesley
        System.out.println(sr.lowestRank());  // Output: Taylor
    }
}
>>>>>>> 1bfcaa02198f92b3aa0940982549dd2c61f9695e
