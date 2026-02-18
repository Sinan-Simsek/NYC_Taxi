import pandas as pd
import pyarrow.parquet as pq
import os


BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'taxi')

if __name__ == '__main__':
#List the paths to the 12 Parquet files
    parquet_file_paths = [
        os.path.join(BASE_DIR, "yellow_tripdata_2022-08.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2022-09.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2022-10.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2022-11.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2022-12.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-01.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-02.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-03.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-04.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-05.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-06.parquet"),
        os.path.join(BASE_DIR, "yellow_tripdata_2023-07.parquet")
        # Add the paths for the other files here
    ]

    # #Initialize an empty DataFrame to store the combined data
    # combined_df = pd.DataFrame()

    # #Read and concatenate the Parquet files
    # for path in parquet_file_paths:
    #     table = pq.read_table(path)
    #     df = table.to_pandas()
    #     combined_df = pd.concat([combined_df, df])

    # #Write the combined DataFrame to a new Parquet file
    # combined_output_path = "path_to_combined_file.parquet"
    # table = pq.Table.from_pandas(combined_df)
    # pq.write_table(table, combined_output_path)


    with pq.ParquetWriter("output.parquet", schema=pq.ParquetFile(parquet_file_paths[0]).schema_arrow) as writer:
        for file in parquet_file_paths:
            writer.write_table(pq.read_table(file))
