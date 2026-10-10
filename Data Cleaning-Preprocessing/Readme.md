# FIFA 21 Data Cleaning-Preprocessing  & Visualization

A personal learning project to practice a complete data workflow with Python: starting from raw FIFA 21 player data, converting inconsistent fields into a cleaner dataset, and comparing the raw and cleaned data through visualizations.

This is a self-learning project, not an assignment submission.

## Project Workflow

```text
Raw FIFA 21 CSV
      
Inspect and understand the data
      
Run the raw-to-clean conversion script
      
fifa21_cleaned_data.csv
      
Visualize and compare raw vs. cleaned data
      
Review data quality and patterns
```

## Goals

- Practice inspecting a real-world, messy dataset.
- Convert text-formatted numeric values into usable numeric columns.
- Standardize height and weight units.
- Clean rating fields and convert hit counts.
- Parse player join dates and derive `Years_at_Club`.
- Flag potential wage outliers without automatically deleting those rows.
- Validate important columns and compare the raw and cleaned versions.
- Create visualizations that make data-quality issues and distributions easier to understand.

## Tools

- Python 3
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Dataset

The project uses the FIFA 21 player dataset originally published on Kaggle:

[FIFA 21 Messy, Raw Dataset for Cleaning / Exploring — Kaggle](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring)

Download the dataset separately and place the raw CSV in the project folder. The conversion script supports either of these filenames:

- `fifa21_raw_data.csv`
- `fifa21 raw data v2.csv`


### Cleaning steps

The conversion script is designed to:

- Remove extra whitespace and line breaks from text columns.
- Convert `Value`, `Wage`, and `Release Clause` values such as `€67.5M` and `€220K` into numeric amounts.
- Convert height measurements into centimetres.
- Convert weight measurements into kilograms.
- Extract numeric values from `W/F`, `SM`, and `IR`.
- Convert `Hits` values such as `1.6K` into numbers and fill missing values with the median.
- Parse the `Joined` date and create `Years_at_Club`, using 1 January 2021 as the reference date.
- Create a `Wage_Outlier` flag using the IQR rule while keeping flagged players in the dataset.
- Run validation checks and reload the exported CSV to inspect its shape and important data types.


## 3. Visualize and Compare Raw vs. Cleaned Data

After the cleaned CSV has been generated, open `FIFA21_EDA_Solved.ipynb` in Jupyter Notebook or JupyterLab.

Make sure the notebook loads both the raw and cleaned files. Run the notebook from top to bottom:

1. Compare dataset shapes, data types, and missing values.
2. Inspect raw versus cleaned fields.
3. Visualize player attributes and their distributions.
4. Explore relationships between attributes such as Value, Wage, Age, and ratings.
5. Review outliers and category-level patterns.
6. Summarize what changed after cleaning and what the visualizations reveal.

Run **Kernel → Restart Kernel and Run All Cells** to reproduce the notebook outputs. If your CSV filenames differ, update the `pd.read_csv(...)` paths in the notebook.

## Examples of Transformations

| Raw value | Cleaned value | Purpose |
| `€67.5M` | `67500000` | Convert market value to a numeric amount |
| `€220K` | `220000` | Convert wage to a numeric amount |
| `5'11"` | `180.3` | Standardize height in centimetres |
| `159lbs` | `72.1` | Standardize weight in kilograms |
| `4 ★` | `4` | Extract a numeric rating |
| `1.6K` | `1600` | Convert hit counts to numbers |

Actual results depend on the input file and the values it contains.

## What I Am Practicing

- Data inspection and data quality checks
- Text cleaning and numeric parsing
- Unit conversion
- Missing-value handling
- Date parsing and feature creation
- IQR-based outlier flagging
- Data validation
- Exploratory Data Analysis (EDA)
- Histograms, boxplots, scatter plots, and correlation analysis
- Comparing data before and after preprocessing

## Acknowledgment

Dataset source: [yagunnersya — FIFA 21 Messy, Raw Dataset for Cleaning / Exploring](https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring).

