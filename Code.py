# Python Data Analyst Interview Practice
# Author: Nishanth Sake
# Topics: Python, Pandas, NumPy

import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. List, Tuple and Set
# --------------------------------------------------

def list_tuple_set_demo():
    my_list = [10, 20, 20, 30]
    my_tuple = (10, 20, 20, 30)
    my_set = {10, 20, 20, 30}

    print("List :", my_list)
    print("Tuple:", my_tuple)
    print("Set  :", my_set)


# --------------------------------------------------
# 2. Handling Missing Values
# --------------------------------------------------

def handle_missing_values():
    df = pd.DataFrame({
        "Name": ["A", "B", "C", "D"],
        "Age": [20, np.nan, 22, 21],
        "Salary": [30000, 40000, np.nan, 50000]
    })

    print("\nOriginal Data:")
    print(df)

    print("\nMissing Values:")
    print(df.isna().sum())

    # Fill missing values with mean
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

    print("\nAfter Handling Missing Values:")
    print(df)


# --------------------------------------------------
# 3. Remove Duplicates from List
# --------------------------------------------------

def remove_duplicates(numbers):
    result = []
    seen = set()

    for number in numbers:
        if number not in seen:
            result.append(number)
            seen.add(number)

    return result


# --------------------------------------------------
# 4. Merge Two DataFrames
# --------------------------------------------------

def merge_dataframes():
    employees = pd.DataFrame({
        "ID": [1, 2, 3],
        "Name": ["Rahul", "Priya", "Arun"]
    })

    salary = pd.DataFrame({
        "ID": [1, 2, 3],
        "Salary": [40000, 50000, 60000]
    })

    result = pd.merge(employees, salary, on="ID")

    print("\nMerged DataFrame:")
    print(result)


# --------------------------------------------------
# 5. Filter Values Greater Than 100
# --------------------------------------------------

def filter_data():
    df = pd.DataFrame({
        "Name": ["A", "B", "C", "D"],
        "Marks": [80, 150, 120, 90]
    })

    result = df[df["Marks"] > 100]

    print("\nValues Greater Than 100:")
    print(result)


# --------------------------------------------------
# 6. GroupBy Example
# --------------------------------------------------

def groupby_example():
    df = pd.DataFrame({
        "Department": ["IT", "IT", "HR", "HR"],
        "Salary": [50000, 60000, 40000, 45000]
    })

    result = df.groupby("Department")["Salary"].mean()

    print("\nAverage Salary by Department:")
    print(result)


# --------------------------------------------------
# 7. Second Highest Salary
# --------------------------------------------------

def second_highest_salary(salaries):
    unique_salaries = sorted(set(salaries), reverse=True)

    if len(unique_salaries) < 2:
        return None

    return unique_salaries[1]


# --------------------------------------------------
# 8. Create New Column Based on Condition
# --------------------------------------------------

def create_conditional_column():
    df = pd.DataFrame({
        "Name": ["A", "B", "C", "D"],
        "Marks": [85, 65, 35, 90]
    })

    df["Result"] = np.where(
        df["Marks"] >= 40,
        "Pass",
        "Fail"
    )

    print("\nConditional Column:")
    print(df)


# --------------------------------------------------
# 9. loc and iloc
# --------------------------------------------------

def loc_iloc_example():
    df = pd.DataFrame({
        "Name": ["A", "B", "C"],
        "Age": [20, 21, 22],
        "Marks": [85, 90, 75]
    })

    print("\nUsing loc:")
    print(df.loc[1, "Name"])

    print("\nUsing iloc:")
    print(df.iloc[1, 0])


# --------------------------------------------------
# 10. Mean, Median and Standard Deviation
# --------------------------------------------------

def statistics_example():
    df = pd.DataFrame({
        "Salary": [30000, 40000, 50000, 60000, 70000]
    })

    print("\nStatistics:")

    print("Mean:", df["Salary"].mean())
    print("Median:", df["Salary"].median())
    print("Standard Deviation:", df["Salary"].std())


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("PYTHON DATA ANALYST INTERVIEW PRACTICE")
    print("=" * 50)

    print("\n1. LIST, TUPLE AND SET")
    list_tuple_set_demo()

    print("\n2. MISSING VALUES")
    handle_missing_values()

    print("\n3. REMOVE DUPLICATES")
    numbers = [1, 2, 2, 3, 1, 4, 3]
    print("Original:", numbers)
    print("Without Duplicates:", remove_duplicates(numbers))

    print("\n4. MERGE DATAFRAMES")
    merge_dataframes()

    print("\n5. FILTER DATA")
    filter_data()

    print("\n6. GROUPBY")
    groupby_example()

    print("\n7. SECOND HIGHEST SALARY")
    salaries = [30000, 50000, 70000, 50000, 60000]
    print("Salaries:", salaries)
    print("Second Highest:", second_highest_salary(salaries))

    print("\n8. CONDITIONAL COLUMN")
    create_conditional_column()

    print("\n9. LOC VS ILOC")
    loc_iloc_example()

    print("\n10. STATISTICS")
    statistics_example()

    print("\n" + "=" * 50)
    print("PROGRAM COMPLETED")
    print("=" * 50)
