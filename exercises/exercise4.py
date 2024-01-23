import urllib.request
import zipfile


# Download and unzip data
download_link = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
path = "mowesta-dataset-20221107.zip"
urllib.request.urlretrieve(download_link, path)
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('mowesta-dataset-20221107')
