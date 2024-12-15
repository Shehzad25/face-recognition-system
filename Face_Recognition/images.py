import os

# Define the base directory
base_dir = 'dataset'

# Define subdirectories for Pooja and Sneha
shehzad_dir = os.path.join(base_dir, 'shehzad')


# Create the directories if they do not exist
os.makedirs(shehzad_dir, exist_ok=True)


# Print confirmation
print("Directories created:")
print(f"Shehzad's images : {shehzad_dir}")

