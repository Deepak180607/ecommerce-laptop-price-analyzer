import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def make_plots():
    # 1. Load Data with error handling
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, "data", "cleaned_laptop.csv")
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: 'cleaned_laptop.csv' not found. Run analysis.py first.")
        return

    if df.empty:
        print("Warning: The dataset is empty. Check your scraper logic or filters.")
        return

    sns.set_theme(style="white")
    plt.rcParams['figure.figsize'] = (12, 8)
    
    def label_inside_bars(ax, labels):
        for i, (bar, label) in enumerate(zip(ax.patches, labels)):
            ax.text(
                bar.get_width() * 0.02,
                bar.get_y() + bar.get_height()/2,
                f"{label}",
                va='center',
                ha='left',
                fontsize=9,
                fontweight='bold',
                color='black'
            )

    #GRAPH 1: Top 10 Cheapest Gaming Laptops
    plt.figure()
    cheapest = df.sort_values(by="Price").head(10)
    ax1 = sns.barplot(x="Price", y="Name", data=cheapest, palette="Blues_d")
    
    label_inside_bars(ax1, cheapest["Name"])
    ax1.set_yticklabels([])
    
    plt.title("Top 10 Cheapest Gaming Laptops", fontsize=16, pad=20, fontweight='bold')
    plt.xlabel("Price (₹)", fontsize=12)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("data/cheapest_laptop.png", dpi=300)
    plt.close()

    #GRAPH 2: Top 10 Best Value Laptops
    plt.figure()
    best_value = df.sort_values(by="value_score", ascending=False).head(10)
    ax2 = sns.barplot(x="value_score", y="Name", data=best_value, palette="Reds_d")
    
    label_inside_bars(ax2, best_value["Name"])
    ax2.set_yticklabels([])
    
    plt.title("Top 10 Best Value Laptops (Rating/Price)", fontsize=16, pad=20, fontweight='bold')
    plt.xlabel("Value Score", fontsize=12)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("data/best_value_laptops.png", dpi=300)
    plt.close()

    #GRAPH 3: Price vs Rating Relationship
    plt.figure()
    sns.regplot(x="Price", y="Ratings", data=df,
                scatter_kws={'alpha':0.6, 'color':'teal'},
                line_kws={'color':'orange'})
    
    plt.title("Relationship: Price vs Rating", fontsize=16, fontweight='bold')
    plt.xlabel("Price (₹)", fontsize=12)
    plt.ylabel("Rating (Out of 5)", fontsize=12)
    plt.tight_layout()
    plt.savefig("data/price_vs_rating.png", dpi=300)
    plt.close()

    #GRAPH 4: Price Distribution
    plt.figure()
    sns.histplot(df["Price"], bins=15, kde=True, color="purple")
    
    plt.title("Gaming Laptop Price Distribution", fontsize=16, fontweight='bold')
    plt.xlabel("Price (₹)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.tight_layout()
    plt.savefig("data/price_distribution.png", dpi=300)
    plt.close()

    print("All 4 professional charts have been saved in the data folder!")

if __name__ == "__main__":
    make_plots()

    print("Charts saved in data folder!")
    


