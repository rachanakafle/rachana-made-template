KAGGLE_JSON_PATH="./project/kaggle.json"
KAGGLE_CONFIG_DIR=$(dirname "$KAGGLE_JSON_PATH")
export KAGGLE_CONFIG_DIR

# Install required packages
pip install --upgrade pip
pip install -r ./project/requirements.txt

python3 ./project/pipeline.py

echo "Pipeline completed"