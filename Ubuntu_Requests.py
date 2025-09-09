# Import the necessary libraries
import os
import requests
from urllib.parse import urlparse

def download_image(url):
    """
    Downloads an image from a given URL and saves it to a local directory.
    """
    # 1. Create the directory if it doesn't exist
    directory = 'Fetched_Images'
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' is ready.")
    except OSError as e:
        print(f"Error: Could not create directory '{directory}'. {e}")
        return

    # 2. Extract a filename from the URL
    try:
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            # Fallback for URLs without a filename
            print("No clear filename in URL. Using a default name.")
            filename = "downloaded_image.jpg"
    except Exception as e:
        print(f"Error parsing URL to get filename: {e}")
        filename = "downloaded_image.jpg"

    filepath = os.path.join(directory, filename)

    # 3. Download the image and handle errors gracefully
    try:
        print(f"Attempting to download from: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

        # 4. Save the image to the file
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Success! Image saved to '{filepath}'")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except OSError as e:
        print(f"Error: Could not write file to '{filepath}'. {e}")

if __name__ == "__main__":
    image_url = input("Enter the URL of the image you want to download: ")
    download_image(image_url)