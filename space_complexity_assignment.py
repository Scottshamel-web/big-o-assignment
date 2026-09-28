"""
Space Complexity Assignment

Part 1 - Space Complexity Classifications

Function A: O(n)
Reason: s[::-1] creates a new string containing n characters, so the extra memory grows with the input size.

Function B: O(k), or O(n) in the worst case
Reason: The dictionary stores one entry for each distinct character, so it uses O(k) space where k is the number of unique characters and can grow to O(n).

Function C: O(n^2)
Reason: The function creates an n-by-n matrix containing n^2 values.

Function D: O(1)
Reason: The function only keeps a single running total and loop variable, so it uses constant extra memory.
"""

import csv


# Approach 1: Set approach
# Time complexity: O(n) average
# Space complexity: O(n)
# This is usually faster because set membership checks are O(1) on average,
# but sets use more memory per item than lists.
def find_duplicates_with_set(csv_path, email_column="email"):
    seen = set()
    duplicates = set()

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            email = row[email_column].strip()

            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates


# Approach 2: Sort-and-scan approach
# Time complexity: O(n log n)
# Space complexity: O(n)
# This stores all emails in a list, sorts them, and checks neighboring values.
def find_duplicates_with_sort(csv_path, email_column="email"):
    emails = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            emails.append(row[email_column].strip())

    emails.sort()

    duplicates = []
    last_duplicate = None

    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1] and emails[i] != last_duplicate:
            duplicates.append(emails[i])
            last_duplicate = emails[i]

    return duplicates


# Tradeoff decision:
#
# On a machine with 4GB RAM, I would choose the sort-and-scan approach.
# Both approaches are O(n) space, but a list generally uses less memory per item
# than a set. I would prioritize avoiding running out of memory, even though
# sorting takes more time.
#
# On a machine with 64GB RAM, I would choose the set approach.
# With much more available memory, I would prioritize speed because set lookups
# are O(1) on average, making this approach O(n) average time.


if __name__ == "__main__":
    # Example:
    #
    # csv_file = "emails.csv"
    #
    # duplicates_set = find_duplicates_with_set(csv_file)
    # print("Duplicates using set:", duplicates_set)
    #
    # duplicates_sort = find_duplicates_with_sort(csv_file)
    # print("Duplicates using sort-and-scan:", duplicates_sort)

    pass