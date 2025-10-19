# cs577 project

Planned maintenance interval prediction

### Environment 

- Using uv: `uv sync`

- Using pip: 
    - `python -m venv .venv`
    - `source .venv/bin/activate`
    - `python -m pip install -e .`

### Data

Download NGAFID dataset from [kaggle](https://www.kaggle.com/datasets/hooong/aviation-maintenance-dataset-from-the-ngafid)

Unzip to `data/` - rename archive to data if needed

Download `BRAF.xls` to `data/` from [spare-part-demand-forecasting](https://github.com/KhueNguyenTK/Spare-Part-Demand-Forecasting/blob/main/All%20Data%20sets/BRAF.xls)

Structure of `data/`:

```
data/
  BRAF.xls
  2days/2days/
    flight_data.pkl
    flight_header.csv
    stats.csv
  all_flights/all_flights/
    flight_header.csv
    one_parq/
      ...
```
