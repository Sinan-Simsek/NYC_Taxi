import pandas as pd
import os

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'taxi_combined', 'part0')

df = pd.read_parquet(os.path.join(base_dir, '0-ec436d91-69d4-42db-b8d0-8ce835ba225b-0.parquet'))

column_to_remove = 'Airport_fee'

df = df.drop(columns=[column_to_remove])

df.to_parquet(os.path.join(base_dir, 'new-parquet.parquet'), index=False)
