import numpy as np
from tabulate import tabulate

def create_table():
    x_vals = np.linspace(0, 2*np.pi, 1000)
    sin = np.sin(x_vals)

    header = ['x','sin']
    data = zip(x_vals,sin)
    tabulated= list(data)

    print(tabulate(tabulated,tablefmt="grid",headers = header,floatfmt=".3f"))

def main():
    create_table()

if __name__ == "__main__":
    main()