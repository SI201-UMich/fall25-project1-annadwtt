import csv

def load_penguin(csv_file):
  penguins = []
  with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      penguins.append(row)
  return penguins

def get_length(penguins, species):
  return [penguin['bill_length_mm'] for penguin in penguins if penguin['species'] == species.lower()]

def avg_bill_length(penguins):
  species_list = ['adelie', 'chinstrap', 'gentoo']
  averages = {}
  for species in species_list:
    lengths = get_length(penguins, species)
    averages[species] = sum(map(float, lengths)) / len(lengths)
  return averages

def avg_flipper_length(penguins):
  species_list = ['adelie', 'chinstrap', 'gentoo']
  averages = {}
  for species in species_list:
    lengths = get_length(penguins, species)
    averages[species] = sum(map(float, lengths)) / len(lengths)
  return averages

def max_bill_length(penguins, averages):
  max_species = max(averages, key=averages.get)
  return [max_species, averages[max_species]]

def max_flipper_length(penguins, averages):
  max_species = max(averages, key=averages.get)
  return [max_species, averages[max_species]]
#testing changes 
print("My local edits here")
