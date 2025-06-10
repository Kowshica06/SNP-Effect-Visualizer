import pandas as pd

def load_snp_data(file_path):
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = load_snp_data("data/sample_snps.csv")
    print(df)
