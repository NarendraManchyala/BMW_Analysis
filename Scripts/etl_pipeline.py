import pandas as pd
def extract_data(file_path):
    df = pd.read_csv(r"C:\Users\mnare\Documents\New folder (2)\data\raw\BMW sales data (2010-2024) (1).csv")
    return df
def transform_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=['Price_USD','Sales_Volume'])
    df['Year'] = df['Year'].astype(int)
    df['Revenue'] = df['Price_USD'] * df['Sales_Volume']
    return df
def load_data(df, output_path):
    df.to_csv("C:\\Users\\mnare\\Documents\\New folder (2)\\data\\processed\\processed.csv", index=False)
    print(f"✅ Data successfully saved to {output_path}")
def run_etl(input_path, output_path):
    df = extract_data(input_path)
    df = transform_data(df)
    load_data(df, output_path)
    return df