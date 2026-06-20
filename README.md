<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Python][python-shield]][python-url]
[![Pandas][pandas-shield]][pandas-url]
[![License: Unlicense][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">ETL Data Cleaning Tool</h3>

  <p align="center">
    A Python-based ETL tool that automatically detects column types, validates data, and generates detailed quality reports for CSV, Excel, and JSON files.
    <br />
    <a href="https://github.com/keziah-bejoy/etl-tool"><strong>Explore the repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/keziah-bejoy/etl-tool/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/keziah-bejoy/etl-tool/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#configuration">Configuration</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#validation-rules">Validation Rules</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The **ETL Data Cleaning Tool** is a Python script that Extracts, Transforms, and Loads tabular data while automatically detecting column types, validating values against format and range rules, standardizing dates, handling missing values, and removing duplicates. It finishes by printing a detailed quality report that lists exactly which rows had missing or invalid data.

This project was built during my internship to solve a common data engineering problem: messy, inconsistent input files (CSV, Excel, or JSON) that need to be cleaned and validated before they can be trusted for analysis.

Here's what makes it useful:
* It doesn't rely on hardcoded column names alone — a **hybrid detection** approach (column name *and* data pattern, with a 70% match threshold) is used to correctly identify column types even when headers are inconsistent.
* It supports **three file formats** (CSV, XLSX, JSON) through a single, unified pipeline.
* All thresholds, regex patterns, and file paths are kept in a `.env` file, so the tool can be reconfigured without touching the code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][python-shield]][python-url]
* [![Pandas][pandas-shield]][pandas-url]
* python-dateutil
* python-dotenv
* openpyxl

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- KEY FEATURES -->
## Key Features

| Feature | Description |
|---|---|
| Multi-format Support | Reads CSV, Excel (`.xlsx`), and JSON files |
| Hybrid Column Detection | Identifies column types using column names **and** data patterns (70% match threshold) |
| Regex Validation | Validates emails, phone numbers, dates, URLs, and zipcodes |
| Date Standardization | Converts any recognized date format to ISO (`YYYY-MM-DD`) |
| Missing Value Handling | Fills missing text with `"Unknown"`, missing numbers with `0` |
| Duplicate Removal | Automatically removes duplicate rows |
| Detailed Quality Report | Lists exact row numbers for missing and invalid data |
| Environment Configuration | All file paths, patterns, and thresholds live in `.env` |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to get a local copy of the ETL tool up and running.

### Prerequisites

You'll need Python 3 and `pip` installed on your machine.
* pip
```sh
  python -m pip install --upgrade pip
```

### Installation

1. Clone the repo
```sh
   git clone https://github.com/keziah-bejoy/etl-tool.git
```
2. Move into the project directory
```sh
   cd etl-tool
```
3. Install the required Python packages
```sh
   pip install pandas python-dateutil python-dotenv openpyxl
```
   or, if a `requirements.txt` is present:
```sh
   pip install -r requirements.txt
```

### Configuration

All settings are controlled through a `.env` file in the project root. Create one (or edit the existing one) with values like:

```env
INPUT_FILE=employeejs.json
OUTPUT_FILE=clean.json
REPORT_FILE=report.txt

EMAIL_PATTERN=^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
PHONE_PATTERN=^[0-9]{10}$
DATE_PATTERN=^\d{4}-\d{2}-\d{2}$|^\d{2}/\d{2}/\d{4}$

AGE_MIN=0
AGE_MAX=120
SALARY_MIN=1000
SALARY_MAX=10000000
QUANTITY_MIN=1
QUANTITY_MAX=1000
PRICE_MIN=1
PRICE_MAX=1000000
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Place your input file (CSV, XLSX, or JSON) in the project directory, point `INPUT_FILE` to it in `.env`, then run:

```sh
python etl.py
```

The tool will clean the data, write the cleaned output to `OUTPUT_FILE`, and generate a quality report saved to `REPORT_FILE`. A sample report looks like this:

```text
------------------------------------------------------------
                    ETL QUALITY REPORT
------------------------------------------------------------

SUMMARISED REPORT:
  Original rows:                 1500
  Duplicate rows removed:        5
  Rows after cleaning:           1495
  Rows with issues:              320
  Clean rows:                    1175

MISSING DATA FOUND
------------------------------------------------------------
  Email (15 rows)
    Row numbers: [1, 3, 44, 33, 56, ...]

INVALID DATA FOUND
------------------------------------------------------------
  Invalid email (45 rows)
    Row numbers: [5, 12, 23, 45, 67, ...]
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- VALIDATION RULES -->
## Validation Rules

| Data Type | Validation Rule |
|---|---|
| Email | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` |
| Phone | `^[0-9]{10}$` |
| Age | 0 – 120 |
| Salary | 1,000 – 10,000,000 |
| Date | Multiple formats (`YYYY-MM-DD`, `DD/MM/YYYY`, `DD-MM-YYYY`) |
| URL | Must start with `http://`, `https://`, or `www.` |
| Zipcode | 5–6 digits |
| Gender | Male, Female, M, F, Other, Non-binary |
| Status | Active, Inactive, Pending, Completed, Cancelled, Approved, Rejected |
| Quantity | 1 – 1,000 |
| Price | 1 – 1,000,000 |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PROJECT STRUCTURE -->
## Project Structure

| File | Purpose |
|---|---|
| `etl.py` | Main ETL script |
| `.env` | Configuration file |
| `.gitignore` | Git ignore rules |
| `README.md` | Project documentation |
| `requirements.txt` | Python dependencies |

**Code sections inside `etl.py`:**

| Section | Purpose |
|---|---|
| Load `.env` | Loads environment variables |
| File I/O | Reads/writes CSV, XLSX, JSON |
| Detection Functions | Identifies column types |
| Column Detection | Hybrid (name + data) matching |
| Validation | Checks data quality against rules |
| Missing Data Collection | Tracks missing values by row |
| Reporting | Generates the final quality report |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Multi-format support (CSV, XLSX, JSON)
- [x] Hybrid column detection
- [x] Regex-based validation
- [x] Environment-based configuration
- [x] Detailed quality report with row numbers
- [ ] Command-line arguments (override `.env` values at runtime)
- [ ] Configurable detection threshold (currently fixed at 70%)
- [ ] Export report as HTML/PDF in addition to plain text
- [ ] Unit test coverage

See the [open issues](https://github.com/keziah-bejoy/etl-tool/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Keziah Bejoy - [keziahbejoy16@gmail.com](mailto:keziahbejoy16@gmail.com)

Project Link: [https://github.com/keziah-bejoy/etl-tool](https://github.com/keziah-bejoy/etl-tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[pandas-shield]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[pandas-url]: https://pandas.pydata.org/
[license-shield]: https://img.shields.io/badge/license-Unlicense-orange?style=for-the-badge
[license-url]: https://github.com/keziah-bejoy/etl-tool/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/keziahh
