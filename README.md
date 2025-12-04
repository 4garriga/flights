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


