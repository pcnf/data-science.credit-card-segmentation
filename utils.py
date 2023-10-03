import matplotlib.pyplot as plt
import pandas as pd

def plot_bar(
    df,
    segment,
    xlabel,
    ylabel,
    title,
    color
):
    plt.figure(figsize = (14, 6))
    bars = plt.bar(df['Segment'], df[segment], alpha = 0.7, color = color)

    for bar, value in zip(bars, df[segment]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15, str(round(value, 2)),
                 ha='center', va='bottom', fontsize=10)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)  
    plt.tight_layout()