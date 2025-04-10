import os
import requests
from datetime import datetime

# Replace with your name
first_name = "Derrick"
last_name = "Darku"

# 1. Create a custom directory in the user's home folder
home_dir = os.path.expanduser("~")
dir_name = os.path.join(home_dir, f"{first_name}_{last_name}")
if not os.path.exists(dir_name):
    os.makedirs(dir_name)  # This will create the directory if it doesn't exist

# 2. Download a file from GitHub (or any URL)
url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"  # You can replace this URL with your own
response = requests.get(url)

# 3. Save it with your name, ensuring the directory exists
file_path = os.path.join(dir_name, f"{first_name}_{last_name}.txt")
with open(file_path, "wb") as f:
    f.write(response.content)  # Write the file content

# 4. Modify file content with user input and current datetime
user_input = input("Describe what you have learned so far in a sentence: ")
with open(file_path, "w") as f:
    f.write(user_input + "\n")
    f.write("Timestamp: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 5. Verify the final content
with open(file_path, "r") as f:
    print("\n✅ Final content of the file:")
    print(f.read())

