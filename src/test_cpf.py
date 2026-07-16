import os

from read_cpf import read_cpf
from plot_orbit import plot_orbit

CPF_FOLDER = "../cpf"
OUTPUT_FOLDER = "../output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

cpf_files = sorted(
    f for f in os.listdir(CPF_FOLDER)
    if f.lower().endswith(".cpf")
)

print("=" * 60)
print(f"Found {len(cpf_files)} CPF files")
print("=" * 60)

for cpf_file in cpf_files:

    filepath = os.path.join(CPF_FOLDER, cpf_file)

    print(f"\nProcessing {cpf_file}")

    df = read_cpf(filepath) # reads one CPF file. produces rows(state vectors)

    print(df.head())

    print(f"Number of state vectors: {len(df)}")

    satellite_name = os.path.splitext(cpf_file)[0]

    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"{satellite_name}_orbit.png",
    )

    plot_orbit(
        df,
        satellite_name.upper(),
        save_path=output_path,
    )

print("\nFinished testing all CPF files.")