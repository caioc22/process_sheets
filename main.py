import pandas as pd, numpy as np
from process import *


def main():

    for file in os.listdir("sheets"):
        print(file)
        sheet = pd.read_excel(f'sheets/{file}')

        valid_sheet = clean_sheet(sheet)
        print(valid_sheet)
        vector = vectorize_csv(valid_sheet, only_strings=True, method='bagwords')
        # vector
    


if __name__=="__main__":
    main()  