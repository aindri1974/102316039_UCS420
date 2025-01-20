##Question 1
"""
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
print("After adding 200 and 300:", L)
L.remove(10)
L.remove(30)
print("After removing 10 and 30:", L)
L.sort()
print("Sorted in ascending order:", L)
L.sort(reverse=True)
print("Sorted in descending order:", L)
"""

##Question 2
"""
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
highest_score = max(scores)
highest_index = scores.index(highest_score)
print("Highest score:", highest_score, "at index:", highest_index)
lowest_score = min(scores)
lowest_count = scores.count(lowest_score)
print("Lowest score:", lowest_score, "occurs", lowest_count, "times")
reversed_list = list(scores[::-1])
print("Reversed tuple as a list:", reversed_list)
score_to_check = 76  
if score_to_check in scores:
    print(f"Score {score_to_check} is present at index {scores.index(score_to_check)}")
else:
    print(f"Score {score_to_check} is not present")
"""
## Question 3
"""
import random
random_numbers = [random.randint(100, 900) for _ in range(100)]
odd_numbers = [num for num in random_numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)
even_numbers = [num for num in random_numbers if num % 2 == 0]
print("Even numbers:", even_numbers)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [num for num in random_numbers if is_prime(num)]
print("Prime numbers:", prime_numbers)

"""
## Question 4
"""
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. Unique scores (union of sets)
unique_scores = A.union(B)
print("Unique scores:", unique_scores)

# ii. Common scores (intersection of sets)
common_scores = A.intersection(B)
print("Common scores:", common_scores)

# iii. Scores exclusive to each team (symmetric difference)
exclusive_scores = A.symmetric_difference(B)
print("Exclusive scores:", exclusive_scores)

# iv. Check subset relationship
is_A_subset_of_B = A.issubset(B)
is_B_subset_of_A = B.issubset(A)
print("Is A a subset of B?", is_A_subset_of_B)
print("Is B a subset of A?", is_B_subset_of_A)

# v. Remove a specific score X from A
score_to_remove = 78  # Change this to user input if needed
if score_to_remove in A:
    A.remove(score_to_remove)
    print(f"Score {score_to_remove} removed from A:", A)
else:
    print(f"Score {score_to_remove} is not present in A")

"""

## Question 5
"""
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Rename key 'city' to 'location'
sample_dict["location"] = sample_dict.pop("city")

# Printing the updated dictionary
print(sample_dict)

"""

