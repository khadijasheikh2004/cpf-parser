# CPF Parser

A Python program for reading **ILRS Consolidated Prediction Format (CPF)** files, extracting satellite state vectors, and visualizing predicted orbits in 3D.

The project parses CPF ephemeris files into a Pandas DataFrame, converts Modified Julian Date (MJD) timestamps into Python `datetime` objects, and plots the satellite trajectory around Earth.

---

## Features

- Read ILRS CPF files
- Parse satellite position records (`10` records)
- Convert **Modified Julian Date (MJD)** and **Seconds of Day (SOD)** into UTC timestamps
- Convert positions from **meters to kilometers**
- Store ephemeris data in a Pandas DataFrame
- Generate 3D orbit visualizations using Matplotlib
- Automatically process multiple CPF files in a directory

---

## Project Structure

```
cpf-parser/
│
├── cpf/                  # Input CPF files
├── output/               # Generated orbit plots
├── src/                  # Python source files
│   ├── read_cpf.py
│   ├── plot_orbit.py
│   └── test_cpf.py
│
└── README.md
```

---

## Example CPF File

The parser reads **position records** beginning with `10`.

```
10 0 61232      0.00000  0   1875497.685  -6054808.380   4654367.848
10 0 61232    240.00000  0   3194666.344  -6147400.078   3719624.561
10 0 61232    480.00000  0   4365565.048  -5996307.734   2609586.323
```

Each position record contains

- Modified Julian Date (MJD)
- Seconds of Day (SOD)
- Earth-centered Cartesian coordinates (X, Y, Z)

---

## Installation

Clone the repository

```bash
git clone https://github.com/khadijasheikh2004/cpf-parser.git
cd cpf-parser
```

Install the required packages

```bash
pip install pandas matplotlib numpy
```

---

## Usage

Run

```bash
cd src
python test_cpf.py
```

The program will

1. Search the `cpf/` directory for CPF files.
2. Parse each file into a DataFrame.
3. Print a preview of the extracted state vectors.
4. Generate a 3D orbit plot.
5. Save the figure to the `output/` directory.

---

## Output

Each parsed CPF file produces

- A Pandas DataFrame containing timestamps and Cartesian coordinates.
- A high-resolution PNG orbit plot.

## Data Format

The DataFrame returned by `read_cpf()` contains

| Column | Description |
|---------|-------------|
| `timestamp` | UTC timestamp |
| `x` | X position (km) |
| `y` | Y position (km) |
| `z` | Z position (km) |

---

## Modules

### `read_cpf.py`

Responsible for

- Reading CPF files
- Parsing position (`10`) records
- Converting MJD + SOD into Python `datetime`
- Returning a Pandas DataFrame

---

### `plot_orbit.py`

Creates a 3D visualization of the orbit.

Features include

- Equal axis scaling
- Earth plotted at the origin
- Satellite trajectory
- Optional image export

---

### `test_cpf.py`

Driver script that

- Finds all CPF files
- Processes each file
- Displays parsed data
- Saves orbit plots

---

## Dependencies

- Python 3.9+
- pandas
- numpy
- matplotlib

Install with

```bash
pip install pandas numpy matplotlib
```
