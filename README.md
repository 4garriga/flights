## CS 577 Project

### Planned maintenance interval prediction
Given aircraft sensor recordings and unplanned maintenance logs, train a model to estimate the probability that a flight requires maintenance. By analyzing part failure frequency and replacement costs, we aim to identify the highest-impact maintenance labels based on replacement cost. Ideally, this model informs decisions on scheduling maintenance that reduces maintenance costs while increasing reliability and safety.

### Contents

- #### data folder
  - Download NGAFID all_flights dataset from [here](https://zenodo.org/records/6624956)

    Unzip to `data/` - rename archive to data if needed

    Structure of `data/`:

    ```
    data/
      all_flights/all_flights/
        flight_header.csv
        one_parq/
          ...
      corr.parquet
      pct_nan.parquet
      prices.csv
    ```
    - Already contains engineered data used for models, so rerun certain cells at your own risk. These cells are marked in comments or markdown cells
    
- #### src folder
  - Notebooks containing data analysis/manipulation and model implementations

- #### Models folder
  - Saved models and respective feature predictions from src folder

### Environment 

- Using uv: `uv sync`

- Using pip: 

    - `python -m venv .venv`
    - `source .venv/bin/activate`
    - `python -m pip install -e .`

- Alternatively, create a venv and install from `requirements.txt`

  - `python -m pip install -r requirements.txt`



### Running Scripts

All scripts can be found in the src folder

Run Scripts in the following order

1) main.py -- Holds common functions used by multiple models.
2) eda.ipynb -- Exploratory Data Analysis.
3) data_engineering.ipynb  -- Generate statistical features out of our sensor data.
4) logistic_regression.ipynb  -- Train a logistic regression model to predict whether a flight is pre or post maintenance.
5) random_forest.ipynb  -- Train a Random Forest model to classify a flight as 1 of 5 part labels needing maintenance.
6) LightGBM.ipynb  -- Train a LightGBM model to classify a flight as 1 of 5 part labels needing maintenance.
7) xgboost.ipynb  -- Train a XGBoost model to classify a flight as 1 of 5 part labels needing maintenance.
8) SQL_Classification_Model.ipynb  -- Set up SQL database and queries and train a logistic regression model to predict whether a flight
   needs maintenance for specific part/label.
