# cs577 project

Planned maintenance interval prediction

Given aircraft sensor recordings and unplanned maintenance logs, train a model that estimates the probability a flight requires maintenance. By analyzing part failure frequency and replacement costs, we aim to focus on the highest impact maintenance labels, evaluated on the cost of replacement. Ideally, this model informs decisions on scheduling maintenance that reduces maintenance costs while increasing reliability and safety


### Environment 

- Using uv: `uv sync`

- Using pip: 

    - `python -m venv .venv`
    - `source .venv/bin/activate`
    - `python -m pip install -e .`

- Alternatively, create a venv and install from `requirements.txt`

  - `python -m pip install -r requirements.txt`

### Data

Download NGAFID dataset from [kaggle](https://www.kaggle.com/datasets/hooong/aviation-maintenance-dataset-from-the-ngafid)

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
