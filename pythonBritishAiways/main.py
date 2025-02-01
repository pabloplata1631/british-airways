import requests

# URL of the GitHub repository's ZIP file
repo_url = "https://github.com/mochen862/tableau-end-to-end-portfolio-project/archive/refs/heads/main.zip"

# Define where to save the downloaded ZIP file
save_path = r"C:\Users\karla\Documents\Projects\british-airways\datasets\raw\tableau-end-to-end-portfolio-project.zip"

# Send a GET request to download the file
response = requests.get(repo_url)

# Check if the request was successful
if response.status_code == 200:
    # Write the content of the response to the ZIP file
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Repository downloaded successfully and saved to {save_path}")
else:
    print(f"Failed to download the repository. Status code: {response.status_code}")
