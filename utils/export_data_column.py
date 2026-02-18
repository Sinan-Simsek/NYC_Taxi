import pandas as pd
from helpers import load_cfg
from glob import glob
import os
from deltalake.writer import write_deltalake

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # output_folder = os.path.join(base_dir, '..', 'data', 'column')
    df = pd.read_parquet(os.path.join(base_dir, '..', 'data', 'taxi', 'yellow_tripdata_2023-07.parquet'))
    output_folder = os.path.join(base_dir, '..', 'data', 'taxi-data')
    write_deltalake(output_folder, df)
if __name__ == '__main__':
    main()
