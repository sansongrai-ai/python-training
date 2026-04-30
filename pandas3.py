
import pandas as pd
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Math Score": [85, 78, 92, 75, 88],
    "Science Score": [90, 82, 88, 80, 92]
}


df = pd.DataFrame(data)


print("Dataset:")
print(df)


avg_math = df["Math Score"].mean()
avg_science = df["Science Score"].mean()


top_math_student = df.loc[df["Math Score"].idxmax()]
top_science_student = df.loc[df["Science Score"].idxmax()]


print("\nResults:")
print(f"Average Math Score: {avg_math}")
print(f"Average Science Score: {avg_science}")

print("\nStudent with Highest Math Score:")
print(top_math_student["Student"], "-", top_math_student["Math Score"])

print("\nStudent with Highest Science Score:")
print(top_science_student["Student"], "-", top_science_student["Science Score"])