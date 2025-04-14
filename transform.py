import pandas as pd

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    
    if df.empty:
        print("No data to transform.")
        return df

    print("Transformed DataFrame Columns:", df.columns)  # Print column names to ensure 'score' is there
    df_sorted = df.sort_values(by="score", ascending=False)
    return df_sorted
