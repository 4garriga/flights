from pathlib import Path
import pandas as pd
import dask.dataframe as dd


def getPaths():
    # Project, csv paths
    PROJECT_DIR = Path.cwd().parent
    ALL_FLIGHTS_DIR = PROJECT_DIR / "data" / "all_flights" / "all_flights"

    assert ALL_FLIGHTS_DIR.exists()

    return PROJECT_DIR, ALL_FLIGHTS_DIR


def loadFlightHeader(ALL_FLIGHTS_DIR):
    # Path to all_flights flight_header.csv
    flight_header_path = ALL_FLIGHTS_DIR / "flight_header.csv"
    assert flight_header_path.exists()

    flight_header_df = pd.read_csv(flight_header_path, index_col="Master Index")
    flight_header_df.index.name = "flight_id"
    
    return flight_header_df

def get_flight_df(ALL_FLIGHTS_DIR, flight_id: int) -> pd.DataFrame:
    """Returns flight data pd.DataFrame for specified flight"""
    one_parq_path = ALL_FLIGHTS_DIR / "one_parq"
    flights_df = dd.read_parquet(
        one_parq_path, filters=[("Master Index", "==", flight_id)]
    )
    flights_df = flights_df.rename_axis("flight_id")
    return flights_df.sort_values(by="timestep").compute()

def get_combined_df():
    # Dataset
    PROJECT_DIR = Path.cwd().parent

    parq_path = PROJECT_DIR / "data" / "combined_stats.parquet"
    df = pd.read_parquet(parq_path)
    return PROJECT_DIR,df
