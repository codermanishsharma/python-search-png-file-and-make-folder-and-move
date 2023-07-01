import os
import re
import shutil

# Path to the folder containing your images
folder_path = r"C:\Users\Sharm\Downloads\new"

# List of search terms
search_terms = [ "earth", "moon","smoke"]

# Recursive function to search for images in subfolders
def search_images(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path) and any(filename.lower().endswith(extension) for extension in [".png", ".jpg", ".jpeg"]):
                # Search for each search term in the file name using regular expressions
                for term in search_terms:
                    regex_pattern = fr"\b{re.escape(term)}\b"
                    if re.search(regex_pattern, filename, re.IGNORECASE):
                        # Create the folder if it doesn't exist
                        folder_name = term.replace(" ", "_")
                        new_folder_path = os.path.join(folder_path, folder_name)
                        os.makedirs(new_folder_path, exist_ok=True)
                
                        # Move the file to the corresponding folder
                        new_file_path = os.path.join(new_folder_path, filename)
                        shutil.move(file_path, new_file_path)
                        break

# Call the search_images function with the initial folder_path
search_images(folder_path)