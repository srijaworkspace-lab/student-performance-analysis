# Student Academic Performance Analysis

A beginner-friendly Python project that analyzes student marks stored in a CSV file using **NumPy, Pandas and Matplotlib**.

## Features
- Loads student records from `student_performance.csv`.
- Checks missing values and duplicate student IDs.
- Converts invalid/out-of-range marks to missing values.
- Calculates each student's average and grade.
- Calculates subject-wise and overall class averages.
- Creates four charts.
- Exports analyzed student results and subject summaries.

## Project structure
```text
student-performance-analysis/
├── student_performance.csv
├── analysis.py
├── requirements.txt
├── README.md
├── charts/
└── outputs/
```

## Setup and run
1. Install Python 3.10 or later.
2. Open this folder in VS Code or a terminal.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python analysis.py
   ```
5. Open the `charts/` and `outputs/` folders to view generated results.

## Dataset format
The sample CSV contains `Student_ID`, `Name`, `Maths`, `Science`, `English`, and `Computer`. Replace it with your own non-sensitive dataset while keeping the subject column names or updating `SUBJECTS` in `analysis.py`.

## Grading scale used in this demo
- A+: 90–100
- A: 80–89.99
- B: 70–79.99
- C: 60–69.99
- D: 50–59.99
- F: below 50

This is only a demonstration scale. Replace it with the official grading policy required by your institution.

## Missing data
Missing marks are not silently changed to zero. Student averages are calculated from the available subject marks, and Pandas skips missing values when calculating means. Review the missing-value report before interpreting results.

## Important
The included dataset is synthetic sample data for learning. Do not upload real student personal information or confidential academic records to a public repository.
