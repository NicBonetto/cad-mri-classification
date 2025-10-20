import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Kaggle config
DATASET_NAME = 'danialsharifrazi/cad-cardiac-mri-dataset'
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RAW_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')
ZIP_FILE_PATH = os.path.join(RAW_DATA_DIR, 'cad-cardiac-mri-dataset.zip')

# Create raw data directory
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download dataset 
if not os.path.exists(ZIP_FILE_PATH):
    print('Downloading dataset', DATASET_NAME)
    api.dataset_download_files(DATASET_NAME, path=RAW_DATA_DIR, unzip=False)
    print('Download complete.')
else:
    print('Dataset zip file already exists. Skipping download.')

# Unzip dataset 
with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
    zip_ref.extractall(RAW_DATA_DIR)
    print('Dataset extracted to', RAW_DATA_DIR)

print('Dataset ready!')


