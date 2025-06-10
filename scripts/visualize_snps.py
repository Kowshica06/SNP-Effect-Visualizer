import pandas as pd
import matplotlib.pyplot as plt

def plot_snps(file_path):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 2))
    plt.scatter(df['Position'], [1]*len(df), c='red')
    plt.xlabel("SNP Position on Gene")
    plt.yticks([])
    plt.title("SNP Distribution")
    plt.tight_layout()
    plt.savefig("results/snp_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_snps("data/sample_snps.csv")
