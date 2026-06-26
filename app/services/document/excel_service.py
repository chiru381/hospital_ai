import pandas as pd


def read_excel(path):

    xls = pd.ExcelFile(path)

    output = []

    for sheet in xls.sheet_names:

        df = pd.read_excel(path, sheet_name=sheet)

        output.append(f"Sheet : {sheet}")

        output.append(df.to_string(index=False))

    return "\n\n".join(output)