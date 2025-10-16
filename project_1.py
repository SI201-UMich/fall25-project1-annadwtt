# -------------------------------------------------------------
# Name: Anna D.
# Student ID: [Your ID]
# Email: [Your Email]
# Collaborators: [Names or "None"]
# AI Tools Used: ChatGPT (for debugging and cleanup)
# Dataset: Palmer Penguins (Kaggle)
# -------------------------------------------------------------

import csv

# -------------------------------------------------------------
# 1. LOAD CSV
# -------------------------------------------------------------
def load_penguin(csv_file):
    '''
    Params:
        csv_file (str): name or path to a CSV file

    Returns:
        list of dictionaries with penguin data
    '''
    penguins = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            penguins.append(row)
    return penguins


# -------------------------------------------------------------
# 2. SAFE FLOAT HELPER
# -------------------------------------------------------------
def safe_float(value):
    """Converts a value to float, returns None if invalid, empty, or 'NA'."""
    try:
        if value is None or value == "" or str(value).upper() == "NA":
            return None
        return float(value)
    except ValueError:
        return None


# -------------------------------------------------------------
# 3. CALCULATION FUNCTIONS (6 total)
# -------------------------------------------------------------

# --- Function 1 ---
def avg_bill_length_by_sex(penguins):
    '''
    Returns: average bill length (mm) for each species and sex
    Uses columns: species, bill_length_mm, sex
    '''
    species_list = ['Adelie', 'Chinstrap', 'Gentoo']
    sexes = ['male', 'female']
    averages = {}
    for species in species_list:
        for sex in sexes:
            values = []
            for p in penguins:
                if p['species'] == species and p['sex'].lower() == sex:
                    val = safe_float(p['bill_length_mm'])
                    if val is not None:
                        values.append(val)
            if values:
                averages[f'{species}_{sex}'] = round(sum(values) / len(values), 2)
    return averages


# --- Function 2 ---
def avg_flipper_length_by_island(penguins):
    '''
    Returns: average flipper length (mm) for each species on each island
    Uses columns: species, flipper_length_mm, island
    '''
    species_list = ['Adelie', 'Chinstrap', 'Gentoo']
    islands = set(p['island'] for p in penguins if p.get('island'))
    averages = {}
    for species in species_list:
        for island in islands:
            values = []
            for p in penguins:
                if p['species'] == species and p['island'] == island:
                    val = safe_float(p['flipper_length_mm'])
                    if val is not None:
                        values.append(val)
            if values:
                averages[f'{species}_{island}'] = round(sum(values) / len(values), 2)
    return averages


# --- Function 3 ---
def avg_body_mass_by_island_and_sex(penguins):
    '''
    Returns: average body mass (g) by island and sex
    Uses columns: island, sex, body_mass_g
    '''
    islands = set(p['island'] for p in penguins if p.get('island'))
    sexes = ['male', 'female']
    averages = {}
    for island in islands:
        for sex in sexes:
            masses = []
            for p in penguins:
                if p.get('island') == island and p.get('sex') == sex:
                    val = safe_float(p['body_mass_g'])
                    if val is not None:
                        masses.append(val)
            if masses:
                averages[f'{island}_{sex}'] = round(sum(masses) / len(masses), 2)
    return averages


# --- Function 4 ---
def percent_heavy_penguins_by_species(penguins, threshold=5000):
    '''
    Returns: percentage of penguins heavier than threshold (default 5000g) per species
    Uses columns: species, body_mass_g
    '''
    species_list = set(p['species'] for p in penguins)
    percentages = {}
    for species in species_list:
        weights = []
        for p in penguins:
            if p['species'] == species:
                val = safe_float(p['body_mass_g'])
                if val is not None:
                    weights.append(val)
        if weights:
            heavy = [w for w in weights if w > threshold]
            percentages[species] = round(len(heavy) / len(weights) * 100, 1)
    return percentages


# --- Function 5 ---
def avg_bill_depth_by_island_and_species(penguins):
    '''
    Returns: average bill depth (mm) by island and species
    Uses columns: bill_depth_mm, island, species
    '''
    species_list = set(p['species'] for p in penguins)
    islands = set(p['island'] for p in penguins if p.get('island'))
    averages = {}
    for species in species_list:
        for island in islands:
            depths = []
            for p in penguins:
                if p['species'] == species and p['island'] == island:
                    val = safe_float(p['bill_depth_mm'])
                    if val is not None:
                        depths.append(val)
            if depths:
                averages[f'{species}_{island}'] = round(sum(depths) / len(depths), 2)
    return averages


# --- Function 6 ---
def sex_ratio_by_species(penguins):
    '''
    Returns: male-to-female ratio for each species
    Uses columns: species, sex
    '''
    species_list = set(p['species'] for p in penguins)
    ratios = {}
    for species in species_list:
        males = len([p for p in penguins if p['species'] == species and p['sex'].lower() == 'male'])
        females = len([p for p in penguins if p['species'] == species and p['sex'].lower() == 'female'])
        if females > 0:
            ratios[species] = round(males / females, 2)
    return ratios


# -------------------------------------------------------------
# 4. HELPER FUNCTION
# -------------------------------------------------------------
def max_average(averages):
    '''
    Returns: (key, value) pair for the highest average in a dictionary
    '''
    if not averages:
        return ("None", 0)
    max_key = max(averages, key=averages.get)
    return (max_key, averages[max_key])


# -------------------------------------------------------------
# 5. OUTPUT FILE FUNCTION
# -------------------------------------------------------------
def generate_report(results):
    '''
    Writes all calculated results to penguin_report.txt
    '''
    with open("penguin_report.txt", "w") as f:
        f.write("🐧 Penguin Data Analysis Report\n")
        f.write("==================================\n\n")

        for title, data in results.items():
            f.write(f"{title}:\n")
            for k, v in data.items():
                f.write(f"  {k}: {v}\n")
            f.write("\n")

        # Include top averages for two examples
        if "Average Bill Length by Sex" in results:
            bill_max = max_average(results["Average Bill Length by Sex"])
            f.write(f"Highest Average Bill Length: {bill_max[0]} ({bill_max[1]} mm)\n")

        if "Average Flipper Length by Island" in results:
            flip_max = max_average(results["Average Flipper Length by Island"])
            f.write(f"Highest Average Flipper Length: {flip_max[0]} ({flip_max[1]} mm)\n")

    print('Report generated: "penguin_report.txt"!')


# -------------------------------------------------------------
# 6. MAIN FUNCTION
# -------------------------------------------------------------
def main():
    penguins = load_penguin('penguins.csv')

    # Run all six calculations
    bill_avg = avg_bill_length_by_sex(penguins)
    flipper_avg = avg_flipper_length_by_island(penguins)
    body_mass_avg = avg_body_mass_by_island_and_sex(penguins)
    heavy_pct = percent_heavy_penguins_by_species(penguins)
    bill_depth_avg = avg_bill_depth_by_island_and_species(penguins)
    sex_ratio = sex_ratio_by_species(penguins)

    # Store all results in one dict for output
    results = {
        "Average Bill Length by Sex": bill_avg,
        "Average Flipper Length by Island": flipper_avg,
        "Average Body Mass by Island and Sex": body_mass_avg,
        "Percent Heavy Penguins by Species": heavy_pct,
        "Average Bill Depth by Island and Species": bill_depth_avg,
        "Sex Ratio by Species": sex_ratio
    }

    generate_report(results)


# -------------------------------------------------------------
# 7. TEST FUNCTIONS
# -------------------------------------------------------------
import unittest

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"species": "Adelie", "bill_length_mm": "40.1", "bill_depth_mm": "18.7",
             "flipper_length_mm": "181", "body_mass_g": "3750", "sex": "male", "island": "Torgersen"},
            {"species": "Adelie", "bill_length_mm": "37.8", "bill_depth_mm": "18.4",
             "flipper_length_mm": "180", "body_mass_g": "3700", "sex": "female", "island": "Torgersen"},
            {"species": "Gentoo", "bill_length_mm": "47.3", "bill_depth_mm": "15.3",
             "flipper_length_mm": "217", "body_mass_g": "5050", "sex": "male", "island": "Biscoe"},
            {"species": "Adelie", "bill_length_mm": "NA", "bill_depth_mm": "NA",
             "flipper_length_mm": "NA", "body_mass_g": "NA", "sex": "male", "island": "Torgersen"}
        ]

    def test_avg_bill_length_by_sex(self):
        result = avg_bill_length_by_sex(self.data)
        self.assertAlmostEqual(result['Adelie_male'], 40.1)
        self.assertAlmostEqual(result['Adelie_female'], 37.8)

    def test_percent_heavy_penguins_by_species(self):
        result = percent_heavy_penguins_by_species(self.data, threshold=4000)
        self.assertIn('Gentoo', result)
        self.assertTrue(result['Gentoo'] > 0)

    def test_sex_ratio_by_species(self):
        result = sex_ratio_by_species(self.data)
        self.assertIn('Adelie', result)
        self.assertAlmostEqual(result['Adelie'], 2.0)

    def test_avg_body_mass_by_island_and_sex(self):
        result = avg_body_mass_by_island_and_sex(self.data)
        self.assertIn('Torgersen_male', result)
        self.assertAlmostEqual(result['Torgersen_male'], 3750)


if __name__ == "__main__":
    main()
    unittest.main(exit=False)

