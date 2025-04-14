
from extract import stream_reddit
from transform import transform_data
from load import load_data

def run_etl():
    # Extract data from Reddit
    extracted_data = stream_reddit(["StockMarket", "investing"], 10)
    
    # Transform data
    transformed_data = transform_data(extracted_data)
    
    # Load data into SQLite database
    load_data(transformed_data)
    print("ETL Process Completed!")

if __name__ == "__main__":
    run_etl()
