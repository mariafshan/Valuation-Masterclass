"""
File: WorldGDP.py
------------------
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Stock Code': ['GSPC']})
stock_value = 0

GWP = pd.read_csv("GDP/GWPCSV.csv", index_col=0)

def main():
    GWP["Trend"] = GWP["GWP US$"].rolling(10).mean()
    plt.figure(figsize=(20, 8))
    plt.title("Gross World Product in 000,000,000 US$", size=30)
    GWP["GWP US$"].plot(label='Gross World Product')
    GWP["Trend"].plot(label='10 Years Trend')
    plt.legend()
    plt.show()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
