import os

# Define the base directory
base_dir = 'dataset'

# Define subdirectories for Pooja and Sneha
pooja_dir = os.path.join(base_dir, 'pooja')
sneha_dir = os.path.join(base_dir, 'sneha')
shehzad_dir = os.path.join(base_dir, 'shehzad')


# Create the directories if they do not exist
os.makedirs(pooja_dir, exist_ok=True)
os.makedirs(sneha_dir, exist_ok=True)
os.makedirs(shehzad_dir, exist_ok=True)


# Print confirmation
print("Directories created:")
print(f"Pooja's images : {pooja_dir}")
print(f"Sneha's images : {sneha_dir}")
print(f"Shehzad's images : {shehzad_dir}")

