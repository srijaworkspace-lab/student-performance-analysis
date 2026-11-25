"""
Student Academic Performance Analysis
Run: python analysis.py
Input: student_performance.csv
Outputs: outputs/student_results.csv, outputs/subject_summary.csv, charts/*.png
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "student_performance.csv"
OUTPUT_DIR = ROOT / "outputs"
CHART_DIR = ROOT / "charts"
SUBJECTS = ["Maths", "Science", "English", "Computer"]

def assign_grade(score):
    if pd.isna(score):
        return "N/A"
    if score >= 90:
        return "A+"
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    CHART_DIR.mkdir(exist_ok=True)

    # 1. Load and inspect CSV data
    df = pd.read_csv(DATA_FILE)
    print("\\n--- First five records ---")
    print(df.head())
    print("\\n--- Dataset information ---")
    print(df.info())
    print("\\n--- Missing values before cleaning ---")
    print(df.isnull().sum())

    # 2. Validate and clean marks
    for subject in SUBJECTS:
        df[subject] = pd.to_numeric(df[subject], errors="coerce")
        invalid = (df[subject] < 0) | (df[subject] > 100)
        df.loc[invalid, subject] = np.nan

    df = df.drop_duplicates(subset=["Student_ID"]).copy()

    # Keep missing marks as missing; pandas mean skips NaN by default.
    df["Average"] = df[SUBJECTS].mean(axis=1)
    df["Percentage"] = df["Average"]  # all subjects are out of 100
    df["Grade"] = df["Percentage"].apply(assign_grade)

    # 3. Summary statistics using NumPy and Pandas
    subject_averages = df[SUBJECTS].mean()
    class_average = float(np.nanmean(df[SUBJECTS].to_numpy()))
    print("\\n--- Student results ---")
    print(df[["Student_ID", "Name", "Average", "Grade"]].round(2).to_string(index=False))
    print("\\nClass average:", round(class_average, 2))
    print("Highest subject average:", subject_averages.idxmax(), round(subject_averages.max(), 2))
    print("Lowest subject average:", subject_averages.idxmin(), round(subject_averages.min(), 2))

    # 4. Save analyzed data and subject summary
    df.to_csv(OUTPUT_DIR / "student_results.csv", index=False)
    subject_summary = subject_averages.rename("Average_Marks").reset_index()
    subject_summary.columns = ["Subject", "Average_Marks"]
    subject_summary.to_csv(OUTPUT_DIR / "subject_summary.csv", index=False)

    # 5. Visualizations
    plt.figure(figsize=(8, 5))
    subject_averages.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "subject_averages.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    df.set_index("Name")[SUBJECTS].plot(kind="bar", figsize=(10, 5))
    plt.title("Student-wise Subject Performance")
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "student_performance.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 5))
    df["Grade"].value_counts().sort_index().plot(kind="bar")
    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "grade_distribution.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 5))
    df["Average"].dropna().plot(kind="hist", bins=6, edgecolor="black")
    plt.title("Distribution of Student Averages")
    plt.xlabel("Average marks")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "average_distribution.png", dpi=150)
    plt.close()

    # 6. Evidence-based findings
    print("\\n--- Findings ---")
    print(f"Number of student records: {len(df)}")
    print(f"Overall class average: {class_average:.2f}/100")
    print(f"Strongest subject: {subject_averages.idxmax()} ({subject_averages.max():.2f})")
    print(f"Subject needing most attention: {subject_averages.idxmin()} ({subject_averages.min():.2f})")
    print("\\nGrade counts:")
    print(df["Grade"].value_counts().sort_index())
    print("\\nMissing marks after loading (before any imputation):")
    print(pd.read_csv(DATA_FILE)[SUBJECTS].isnull().sum())
    print("\\nAnalysis complete. Check the outputs/ and charts/ folders.")

if __name__ == "__main__":
    main()
