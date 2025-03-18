import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_bar_chart(df, x_col, title, ax):
    """Creates a bar chart with counts and total count annotation."""
    counts = df[x_col].value_counts().sort_values(ascending=False)
    sorted_items = counts.index

    sns.countplot(data=df, x=x_col, order=sorted_items, ax=ax)

    ax.set_title(title)
    ax.set_xticks(range(len(sorted_items)))
    ax.set_xticklabels(list(sorted_items), rotation=45, ha='right')

    # Add integer numbers over the bars
    for p in ax.patches:
        count = int(p.get_height())
        ax.annotate(f'{count}', (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    return counts  # Return counts for potential further use


def visualize_csv(csv_file, delimiter=','):
    """Visualizes CSV data using pandas, matplotlib, and seaborn."""
    try:
        df = pd.read_csv(csv_file, sep=delimiter)

        total_count = len(df)  # Calculate total count once

        # 1. Bar chart of car manufacturers (sorted by count)
        df['manufacturer'] = df['manufacturer'].replace('Ford Shelby', 'Ford')

        fig, ax1 = plt.subplots(figsize=(12, 6))
        create_bar_chart(df, 'manufacturer', 'Car Manufacturers Distribution (Sorted by Count)', ax1)
        ax1.annotate(f'Total Entries: {total_count}', xy=(0.98, 0.98), xycoords='axes fraction',
            ha='right', va='top', fontsize=10)

        plt.tight_layout()
        plt.show()

        # 2. Bar chart of countries of origin (sorted by count)
        fig, ax2 = plt.subplots(figsize=(12, 6))
        create_bar_chart(df, 'countryOfOrigin', 'Car Countries of Origin Distribution (Sorted by Count)', ax2)
        ax2.annotate(f'Total Entries: {total_count}', xy=(0.98, 0.98), xycoords='axes fraction',
            ha='right', va='top', fontsize=10)

        plt.tight_layout()
        plt.show()

        # 3. Bar chart of colors (sorted by count)
        df['color'] = df['color'].str.split().str[0]
        color_counts = df['color'].value_counts().sort_values(ascending=False)
        color_palette = {color: color.lower() for color in color_counts.index}

        fig, ax3 = plt.subplots(figsize=(12, 6))
        sns.countplot(data=df, x='color', order=color_counts.index, hue='color', palette=color_palette, legend=False, ax=ax3)

        ax3.set_xticks(range(len(color_counts.index))) # Added set_xticks
        ax3.set_xticklabels(list(color_counts.index), rotation=45, ha='right')

        for p in ax3.patches:
            count = int(p.get_height())
            ax3.annotate(f'{count}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

        for p in ax3.patches:
            if p.get_facecolor() == (1.0, 1.0, 1.0, 1.0):
                p.set_edgecolor('black')
                p.set_linewidth(1)

        ax3.annotate(f'Total Entries: {total_count}', xy=(0.98, 0.98), xycoords='axes fraction',
            ha='right', va='top', fontsize=10)

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except pd.errors.ParserError:
        print(f"Error: Could not parse file '{csv_file}'. Check delimiter.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
visualize_csv("data.csv", delimiter=",")