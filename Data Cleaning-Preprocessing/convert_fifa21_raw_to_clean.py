"""
FIFA 21 Raw-to-Clean CSV Converter
----------------------------------
Input:
  fifa21_raw_data.csv
  OR fifa21 raw data v2.csv

Output:
  fifa21_cleaned_data.csv

Libraries: pandas, numpy
Install if needed:
  pip install pandas numpy
"""

from pathlib import Path
import re
import numpy as np
import pandas as pd


# ---------- 1. File paths ----------
BASE_DIR = Path(".")
PREFERRED_INPUT = BASE_DIR / "fifa21_raw_data.csv"
ALTERNATE_INPUT = BASE_DIR / "fifa21 raw data v2.csv"
OUTPUT_FILE = BASE_DIR / "fifa21_cleaned_data.csv"

if PREFERRED_INPUT.exists():
    INPUT_FILE = PREFERRED_INPUT
elif ALTERNATE_INPUT.exists():
    INPUT_FILE = ALTERNATE_INPUT
else:
    raise FileNotFoundError(
        "Raw dataset not found. Put either 'fifa21_raw_data.csv' or "
        "'fifa21 raw data v2.csv' in the same folder as this script."
    )


# ---------- 2. Load and back up raw data ----------
df_raw = pd.read_csv(INPUT_FILE, low_memory=False)
df = df_raw.copy()

print(f"Input file: {INPUT_FILE}")
print("Raw shape:", df_raw.shape)

# Standardize column names, e.g. '↓OVA' -> 'OVA'
df.columns = (
    df.columns.astype(str)
    .str.replace("↓", "", regex=False)
    .str.strip()
)


# ---------- 3. Clean whitespace in text columns ----------
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = (
        df[col]
        .astype("string")
        .str.replace(r"[\r\n\t]+", " ", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

# Convert textual placeholders to missing values.
missing_tokens = {"", "-", "--", "N/A", "n/a", "NA", "nan", "None"}
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].replace(list(missing_tokens), pd.NA)


# ---------- 4. Reusable conversion functions ----------
def parse_amount(value):
    """
    Convert values such as €67.5M, €220K, €0 or 220000 to numbers.
    M = million, K = thousand. Unparseable/missing values become NaN.
    """
    if pd.isna(value):
        return np.nan

    if isinstance(value, (int, float, np.integer, np.floating)):
        return float(value)

    text = str(value).strip().replace(",", "").replace("€", "").replace("$", "").replace("£", "")
    text = text.replace(" ", "")

    if text.lower() in {"", "-", "--", "n/a", "na", "nan", "none"}:
        return np.nan

    multiplier = 1.0
    if text[-1:].upper() == "M":
        multiplier = 1_000_000
        text = text[:-1]
    elif text[-1:].upper() == "K":
        multiplier = 1_000
        text = text[:-1]
    elif text[-1:].upper() == "B":
        multiplier = 1_000_000_000
        text = text[:-1]

    try:
        return float(text) * multiplier
    except ValueError:
        return np.nan


def parse_height_cm(value):
    """Convert feet/inches or cm strings to centimetres."""
    if pd.isna(value):
        return np.nan

    if isinstance(value, (int, float, np.integer, np.floating)):
        return float(value)

    text = str(value).strip().lower().replace(" ", "")

    # Examples: 5'11", 5'11, 5′11″
    text = text.replace("′", "'").replace("″", '"')
    feet_inches = re.search(r"(\d+(?:\.\d+)?)'(\d+(?:\.\d+)?)", text)
    if feet_inches:
        feet = float(feet_inches.group(1))
        inches = float(feet_inches.group(2))
        return feet * 30.48 + inches * 2.54

    # Examples: 175cm, 175.0 cm, or a plain numeric string
    number = re.search(r"-?\d+(?:\.\d+)?", text)
    if number:
        return float(number.group())

    return np.nan


def parse_weight_kg(value):
    """Convert pounds or kg strings to kilograms."""
    if pd.isna(value):
        return np.nan

    if isinstance(value, (int, float, np.integer, np.floating)):
        return float(value)

    text = str(value).strip().lower().replace(" ", "")
    number = re.search(r"-?\d+(?:\.\d+)?", text)

    if not number:
        return np.nan

    amount = float(number.group())
    if "lbs" in text or "lb" in text:
        return amount * 0.453592
    # Values labelled kg or plain numeric values are treated as kilograms.
    return amount


def parse_hits(value):
    """Convert hit counts such as 1.6K to numeric counts."""
    return parse_amount(value)


# ---------- 5. Convert money columns ----------
for col in ["Value", "Wage", "Release Clause"]:
    if col in df.columns:
        df[col] = df[col].map(parse_amount)
        print(f"\nConverted {col} to numeric values.")

if "Value" in df.columns:
    print("Value entries equal to 0:", int((df["Value"] == 0).sum()))
if "Wage" in df.columns:
    print("Wage entries equal to 0:", int((df["Wage"] == 0).sum()))


# ---------- 6. Convert height and weight ----------
if "Height" in df.columns:
    df["Height"] = df["Height"].map(parse_height_cm).round(1)
    missing_height = int(df["Height"].isna().sum())
    if missing_height:
        median_height = df["Height"].median()
        if pd.isna(median_height):
            raise ValueError("Height could not be parsed and has no valid values for imputation.")
        df["Height"] = df["Height"].fillna(median_height).round(1)
        print(f"Filled {missing_height} missing/unparsed Height value(s) with the median.")

if "Weight" in df.columns:
    df["Weight"] = df["Weight"].map(parse_weight_kg).round(1)
    missing_weight = int(df["Weight"].isna().sum())
    if missing_weight:
        median_weight = df["Weight"].median()
        if pd.isna(median_weight):
            raise ValueError("Weight could not be parsed and has no valid values for imputation.")
        df["Weight"] = df["Weight"].fillna(median_weight).round(1)
        print(f"Filled {missing_weight} missing/unparsed Weight value(s) with the median.")


# ---------- 7. Convert rating columns ----------
for col in ["W/F", "SM", "IR"]:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col].astype("string").str.extract(r"(\d+(?:\.\d+)?)", expand=False),
            errors="coerce"
        )


# ---------- 8. Convert Hits and fill missing values with median ----------
if "Hits" in df.columns:
    df["Hits"] = df["Hits"].map(parse_hits)
    missing_hits = int(df["Hits"].isna().sum())
    median_hits = df["Hits"].median()

    if pd.isna(median_hits):
        raise ValueError("Hits contains no valid numeric values; median imputation is impossible.")

    df["Hits"] = df["Hits"].fillna(median_hits)
    print(f"Filled {missing_hits} missing/unparsed Hits value(s) with median: {median_hits:g}")


# ---------- 9. Convert Joined date and calculate Years_at_Club ----------
if "Joined" in df.columns:
    df["Joined"] = pd.to_datetime(df["Joined"], format="%b %d, %Y", errors="coerce")

    # Use the assignment's fixed reference date so results are reproducible.
    reference_date = pd.Timestamp("2021-01-01")
    df["Years_at_Club"] = (
        (reference_date - df["Joined"]).dt.days / 365.25
    ).round(2)

    if "Club" in df.columns:
        long_stays = df.loc[
            df["Years_at_Club"] > 10,
            ["Name", "Club", "Joined", "Years_at_Club"]
            if "Name" in df.columns else ["Club", "Joined", "Years_at_Club"]
        ]
        print("\nPlayers with more than 10 years at the club:")
        print(long_stays.to_string(index=False))


# ---------- 10. Flag wage outliers using the IQR rule ----------
if "Wage" in df.columns:
    wage_valid = df["Wage"].dropna()

    if len(wage_valid):
        q1 = wage_valid.quantile(0.25)
        q3 = wage_valid.quantile(0.75)
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr

        # Keep all rows; flag rather than remove outliers.
        df["Wage_Outlier"] = (
            (df["Wage"] < lower_fence) | (df["Wage"] > upper_fence)
        )
        print(f"\nWage lower fence: {lower_fence:,.2f}")
        print(f"Wage upper fence: {upper_fence:,.2f}")
        print("Is lower fence negative?", lower_fence < 0)

        name_col = "Name" if "Name" in df.columns else df.columns[0]
        print("\nTop 10 earners:")
        print(
            df.nlargest(10, "Wage")[[name_col, "Wage"]]
            .to_string(index=False)
        )


# ---------- 11. Optional: split Contract into start, end, status ----------
if "Contract" in df.columns:
    contract = df["Contract"].astype("string").str.strip()

    # Examples commonly include "2018 ~ 2022", "Jun 30, 2021 On Loan",
    # or "Free". Keep the original Contract column as well.
    split_dates = contract.str.extract(
        r"(?P<Contract_Start>\d{4})\s*[~\-]\s*(?P<Contract_End>\d{4})"
    )
    df["Contract_Start"] = split_dates["Contract_Start"]
    df["Contract_End"] = split_dates["Contract_End"]
    df["Contract_Status"] = np.select(
        [
            contract.str.contains("loan", case=False, na=False),
            contract.str.contains("free", case=False, na=False),
        ],
        ["On Loan", "Free Agent"],
        default="Standard/Other"
    )


# ---------- 12. Drop exact duplicate rows, if any ----------
duplicates_before = int(df.duplicated().sum())
if duplicates_before:
    df = df.drop_duplicates().copy()

print(f"\nExact duplicate rows removed: {duplicates_before}")
print("Cleaned shape:", df.shape)


# ---------- 13. Validation ----------
required_numeric = ["Value", "Wage", "Height", "Weight", "Hits"]
for col in required_numeric:
    if col not in df.columns:
        raise KeyError(f"Required column missing from dataset: {col}")
    if not pd.api.types.is_numeric_dtype(df[col]):
        raise TypeError(f"{col} is not numeric after cleaning.")
    if df[col].isna().any():
        raise ValueError(f"{col} still contains missing values after cleaning.")

if not df["Height"].between(150, 220).all():
    bad = df.loc[~df["Height"].between(150, 220), "Height"].head(10).tolist()
    raise ValueError(f"Height range check failed. Example values: {bad}")

if not df["Weight"].between(50, 120).all():
    bad = df.loc[~df["Weight"].between(50, 120), "Weight"].head(10).tolist()
    raise ValueError(f"Weight range check failed. Example values: {bad}")

print("\nAll required numeric and range checks passed.")
if len(df) != len(df_raw):
    print(
        f"Note: row count changed from {len(df_raw)} to {len(df)} "
        f"because {duplicates_before} exact duplicate row(s) were removed."
    )


# ---------- 14. Export and verify ----------
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nSaved cleaned dataset to: {OUTPUT_FILE.resolve()}")

# Reload once to check the CSV was written and numeric types survived.
check = pd.read_csv(OUTPUT_FILE, low_memory=False)
print("Reloaded CSV shape:", check.shape)
print("\nReloaded required column types:")
print(check[required_numeric].dtypes)
print("\nCleaned preview:")
print(check.head())
