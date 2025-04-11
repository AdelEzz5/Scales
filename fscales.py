#Utility Functions for the Scales Dataset Project

import os
import tarfile          
import urllib.request   
import magic
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.error 
import seaborn as sns

#Download and extract a dataset
def fetch_scales_data(scales_url, scales_path, filename="scales.tgz"):
    try:
        # Creating the Directory If It Doesn't Exist
        if not os.path.isdir(scales_path):
            os.makedirs(scales_path)

        tgz_path = os.path.join(scales_path, filename)

        # Skip download if already exists
        if os.path.exists(os.path.join(scales_path, "scales.csv")):
            print("✅ Dataset already downloaded and extracted.")
            return

        # Download the file
        print("📥 Downloading dataset...")
        urllib.request.urlretrieve(scales_url, tgz_path)
        file_size = os.path.getsize(tgz_path)
        print(f"✅ Downloaded file size: {file_size} bytes")

        if file_size < 1000:
            raise ValueError("❌ File too small, possible incomplete download.")

        # Validate and extract
        if tarfile.is_tarfile(tgz_path):
            print("📦 Valid .tgz archive detected.")
            with tarfile.open(tgz_path) as scales_tgz:
                scales_tgz.extractall(path=scales_path)
            print("✅ Extraction complete.")
        else:
            raise tarfile.TarError("❌ Not a valid .tgz file.")

    except urllib.error.URLError as e:
        print(f"❌ URL error: {e}")
    except tarfile.TarError as e:
        print(f"❌ Tar error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


#load file
def load_scales_data(scales_path):
    csv_path = os.path.join(scales_path, "scales.csv")
    return pd.read_csv(csv_path)

#Save a Matplotlib plot as an image file
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    PROJECT_ROOT_DIR = "."
    CHAPTER_ID = "end_to_end_project"
    IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
    os.makedirs(IMAGES_PATH, exist_ok=True)
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Display cross-validation score
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())

