from pathlib import Path
import pandas as pd
import dask.dataframe as dd
import numpy as np
from sklearn.model_selection import train_test_split
import json
import sqlite3

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

def add_cluster_column(PROJECT_DIR, df):
    # add cluster (target) column
    json_path = PROJECT_DIR / "data" / "label_cluster_map.json"
    assert json_path.exists()

    with json_path.open() as fp:
        label_cluster_map = json.loads(fp.read())

    df["cluster"] = df["label"].map(label_cluster_map)
    return df

def get_combined_df():
    PROJECT_DIR = Path.cwd().parent

    parq_path = PROJECT_DIR / "data" / "combined_stats.parquet"
    df = pd.read_parquet(parq_path)
    return PROJECT_DIR,df

def split_Train_Test(test_size=0.2, random_state=33):
    PROJECT_DIR,df = get_combined_df()

    df = add_cluster_column(PROJECT_DIR, df)
    df["target"] = df["before_after"].map({"before": 1, "after": 0})

    # Split into X, y
    X_all = df[all_features]
    y_all = df[["target", "cluster"]]

    # Remove rows with any NaN values
    X_all.replace([np.inf, -np.inf], np.nan, inplace=True)
    nan_mask = ~X_all.isna().any(axis=1)
    X = X_all[nan_mask]
    y = y_all[nan_mask]

    # Check for NaN, inf
    assert not X.isna().any().any()
    assert not np.isinf(X.select_dtypes(include=[np.number])).any().any()

    # Train-Test Split
    test_size = 0.20

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)
    
    conn = sqlite3.connect(f"{PROJECT_DIR}/data/TrainTestSplitData.db")
    X_train.to_sql("X_train", conn, if_exists="replace", index=False)
    X_test.to_sql("X_test", conn, if_exists="replace", index=False)
    y_train.to_sql("y_train", conn, if_exists="replace", index=False)
    y_test.to_sql("y_test", conn, if_exists="replace", index=False)
    


all_features = [
    "AltMSL_max",
    "AltMSL_mean",
    "AltMSL_min",
    "AltMSL_p25",
    "AltMSL_p75",
    "AltMSL_range",
    "AltMSL_rate_mean",
    "AltMSL_std",
    "E1_CHT1_EGT1_ratio_mean",
    "E1_CHT1_deviation",
    "E1_CHT1_max",
    "E1_CHT1_mean",
    "E1_CHT1_min",
    "E1_CHT1_p25",
    "E1_CHT1_p75",
    "E1_CHT1_std",
    "E1_CHT2_CHT4_corr",
    "E1_CHT2_max",
    "E1_CHT2_mean",
    "E1_CHT2_min",
    "E1_CHT2_p25",
    "E1_CHT2_p75",
    "E1_CHT2_std",
    "E1_CHT3_max",
    "E1_CHT3_mean",
    "E1_CHT3_min",
    "E1_CHT3_p25",
    "E1_CHT3_p75",
    "E1_CHT3_std",
    "E1_CHT4_EGT4_ratio_mean",
    "E1_CHT4_deviation",
    "E1_CHT4_max",
    "E1_CHT4_mean",
    "E1_CHT4_min",
    "E1_CHT4_p25",
    "E1_CHT4_p75",
    "E1_CHT4_std",
    "E1_CHT_EGT_ratio_mean",
    "E1_CHT_EGT_ratio_std",
    "E1_CHT_OAT_diff_mean",
    "E1_CHT_OAT_ratio_mean",
    "E1_CHT_acceleration",
    "E1_CHT_asymmetry",
    "E1_CHT_cruise_stability",
    "E1_CHT_cv",
    "E1_CHT_max_all",
    "E1_CHT_max_rate_change",
    "E1_CHT_mean_all",
    "E1_CHT_min_all",
    "E1_CHT_p90_p10_spread",
    "E1_CHT_range_iqr",
    "E1_CHT_rate_max",
    "E1_CHT_spread_mean",
    "E1_CHT_spread_p90",
    "E1_CHT_std_all",
    "E1_CHT_threshold",
    "E1_EGT1_EGT3_corr",
    "E1_EGT1_max",
    "E1_EGT1_mean",
    "E1_EGT1_min",
    "E1_EGT1_p25",
    "E1_EGT1_p75",
    "E1_EGT1_std",
    "E1_EGT2_max",
    "E1_EGT2_mean",
    "E1_EGT2_min",
    "E1_EGT2_p25",
    "E1_EGT2_p75",
    "E1_EGT2_std",
    "E1_EGT3_max",
    "E1_EGT3_mean",
    "E1_EGT3_min",
    "E1_EGT3_p25",
    "E1_EGT3_p75",
    "E1_EGT3_std",
    "E1_EGT4_deviation",
    "E1_EGT4_max",
    "E1_EGT4_mean",
    "E1_EGT4_min",
    "E1_EGT4_p25",
    "E1_EGT4_p75",
    "E1_EGT4_std",
    "E1_EGT_cv",
    "E1_EGT_max_all",
    "E1_EGT_max_rate_change",
    "E1_EGT_mean_all",
    "E1_EGT_min_all",
    "E1_EGT_p90_p10_spread",
    "E1_EGT_range_iqr",
    "E1_EGT_rate_max",
    "E1_EGT_spread_mean",
    "E1_EGT_std_all",
    "E1_FFlow_RPM_ratio_std",
    "E1_FFlow_acceleration",
    "E1_FFlow_max",
    "E1_FFlow_mean",
    "E1_FFlow_min",
    "E1_FFlow_p25",
    "E1_FFlow_p75",
    "E1_FFlow_std",
    "E1_OilP_RPM_corr",
    "E1_OilP_RPM_ratio",
    "E1_OilP_instability",
    "E1_OilP_mean",
    "E1_OilP_min",
    "E1_OilP_p25",
    "E1_OilP_p75",
    "E1_OilP_std",
    "E1_OilT_climb_rate",
    "E1_OilT_descend_rate",
    "E1_OilT_max",
    "E1_OilT_mean",
    "E1_OilT_min",
    "E1_OilT_p25",
    "E1_OilT_p75",
    "E1_OilT_rate",
    "E1_OilT_std",
    "E1_OilT_threshold",
    "E1_RPM_cruise_stability",
    "E1_RPM_max",
    "E1_RPM_mean",
    "E1_RPM_min",
    "E1_RPM_p25",
    "E1_RPM_p75",
    "E1_RPM_std",
    "E1_power_metric",
    "E1_specific_fuel_consumption",
    "FQtyL_consumed",
    "FQtyL_end",
    "FQtyL_max",
    "FQtyL_mean",
    "FQtyL_min",
    "FQtyL_p25",
    "FQtyL_p75",
    "FQtyL_rate",
    "FQtyL_start",
    "FQtyL_std",
    "FQtyR_consumed",
    "FQtyR_end",
    "FQtyR_max",
    "FQtyR_mean",
    "FQtyR_min",
    "FQtyR_p25",
    "FQtyR_p75",
    "FQtyR_rate",
    "FQtyR_start",
    "FQtyR_std",
    "IAS_max",
    "IAS_mean",
    "IAS_min",
    "IAS_p25",
    "IAS_p75",
    "IAS_rate_mean",
    "IAS_std",
    "NormAc_max",
    "NormAc_mean",
    "NormAc_min",
    "NormAc_p25",
    "NormAc_p75",
    "NormAc_std",
    "OAT_max",
    "OAT_mean",
    "OAT_min",
    "OAT_p25",
    "OAT_p75",
    "OAT_std",
    "VSpd_max",
    "VSpd_mean",
    "VSpd_min",
    "VSpd_p25",
    "VSpd_p75",
    "VSpd_std",
    "amp1_max",
    "amp1_mean",
    "amp1_min",
    "amp1_negative_ratio",
    "amp1_p25",
    "amp1_p75",
    "amp1_std",
    "amp2_max",
    "amp2_mean",
    "amp2_min",
    "amp2_p25",
    "amp2_p75",
    "amp2_std",
    "before_after",
    "date_diff",
    "electrical_load_variance",
    "flight_id",
    "flight_length",
    "fuel_imbalance_max",
    "fuel_imbalance_mean",
    "fuel_imbalance_trend",
    "high_power_duration_ratio",
    "high_temp_duration_ratio",
    "label",
    "num_flights_before",
    "volt1_amp1_stability",
    "volt1_max",
    "volt1_mean",
    "volt1_min",
    "volt1_p25",
    "volt1_p75",
    # "volt1_rpm_correlation", # all nan
    "volt1_std",
    "volt2_max",
    "volt2_mean",
    "volt2_min",
    "volt2_p25",
    "volt2_p75",
    "volt2_std",
]