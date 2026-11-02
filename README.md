# Student Performance Analytics System — V2

A Python-based student performance analysis and visualization project.

## Attribution

This V2 project is based on the original Student Performance Analyzer project
by **Deepanshu**. The original project provided the base student-data
processing and analysis structure.

This repository should not be presented as an entirely independent rewrite
of the original project.

## My Contributions in V2

The V2 extension adds functionality intended to make the system more useful
for data-analysis workflows:

- Student name search
- Department filtering
- Minimum-percentage filtering
- Grade filtering
- Pass/fail filtering
- Improved user-facing validation for the new filters
- Modular `searchFilter.py` extension
- Internship-oriented documentation

## Technology

- Python
- Pandas
- NumPy
- CSV data processing

## Project Structure

```text
student-performance-analyzer/
├── main.py
├── modules/
│   ├── choicesManager.py
│   ├── dataCleaner.py
│   ├── helperFunctions.py
│   ├── recordsAnalyzer.py
│   └── searchFilter.py
├── students-sample.csv
├── sample-invalid-csv/
├── sample-outputs/
├── .gitignore
└── README.md
```

## V2 Search and Filter Features

The new search/filter menu allows users to:

1. Search students by partial name
2. Filter by department
3. Filter by minimum percentage
4. Filter by grade
5. Filter by Pass/Fail result

The filtering uses Pandas DataFrame operations and case-insensitive matching
where appropriate.

## Running the Project

Install the required packages:

```bash
pip install pandas numpy
```

Run:

```bash
python main.py
```

## Important

Before using this project in an internship application, make sure you
understand the original code, the V2 additions, and the attribution above.
Add only contributions that you can personally explain and demonstrate.
