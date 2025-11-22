# cs577 project

Planned maintenance interval prediction

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
  2days/2days/
    flight_data.pkl
    flight_header.csv
    stats.csv
  all_flights/all_flights/
    flight_header.csv
    one_parq/
      ...
    corr.parquet
    pct_nan.parquet
    prices.csv
```
