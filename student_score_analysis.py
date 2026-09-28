import pandas as pd


# ---------------------------------------
# Create the DataFrame
# ---------------------------------------

data = {
    "student": [
        "Alice", "Bob", "Charlie", "Diana", "Eve",
        "Frank", "Grace", "Henry", "Iris", "Jack"
    ],
    "course": [
        "Python", "Python", "SQL", "SQL", "Python",
        "SQL", "Python", "SQL", "Python", "SQL"
    ],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)


# ---------------------------------------
# 1. How many students are in each course?
# ---------------------------------------

students_per_course = df["course"].value_counts()

print("1. Students per course:")
print(students_per_course)


# ---------------------------------------
# 2. Average score per course
# ---------------------------------------

average_score = df.groupby("course")["score"].mean()

print("\n2. Average score per course:")
print(average_score)


# ---------------------------------------
# 3. Top 3 students by score
# ---------------------------------------

top_three = df.nlargest(3, "score")[["student", "score"]]

print("\n3. Top 3 students:")
print(top_three)


# ---------------------------------------
# 4. Average hours studied:
#    passed vs. did not pass
# ---------------------------------------

average_hours = df.groupby("passed")["hours_studied"].mean()

print("\n4. Average hours studied by pass status:")
print(average_hours)


# ---------------------------------------
# 5. Create grade column
#
# 90+     = A
# 80-89   = B
# 70-79   = C
# Below 70 = F
# ---------------------------------------

df["grade"] = pd.cut(
    df["score"],
    bins=[float("-inf"), 70, 80, 90, float("inf")],
    labels=["F", "C", "B", "A"],
    right=False
)

print("\n5. Students with grades:")
print(df[["student", "course", "score", "grade"]])


# ---------------------------------------
# 6. Grade distribution per course
# ---------------------------------------

grade_distribution = pd.crosstab(
    df["course"],
    df["grade"],
    dropna=False
)

print("\n6. Grade distribution per course:")
print(grade_distribution)