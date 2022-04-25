import json
import os
import pandas as pd
from openpyxl import load_workbook
from constant import LIST_CHAMPIONSHIP, NEW_CONVERSION_LIST

xl_file = pd.ExcelFile("./Historique/Historique.xlsx")
result = {}

if not os.path.exists("./analysis/analysis.xlsx"):
    if not os.path.exists("./analysis"):
        os.mkdir("./analysis")
    for championship in LIST_CHAMPIONSHIP:
        result[championship] = {
            "Bet Cards Passed": 0,
            "Bet Cards Failed": 0,
            "Bet Corners Passed": 0,
            "Bet Corners Failed": 0,
            "Bet Global Passed": 0,
            "Bet Global Failed": 0}

    # Write in json File
    json_object = json.dumps(result, indent=4)
    with open("analysis/analysis.json", "w") as f:
        f.write(json_object)

    # Write in Excel
    with open("analysis/analysis.json", encoding='utf-8-sig') as data_file:
        df = pd.read_json(data_file)

    # Reverse Rows and Columns
    df_transpose = df.transpose()
    df_transpose.to_excel("./analysis/analysis.xlsx", sheet_name="Suivi Bets", encoding='utf-8', index=True)

    # Width Cells Auto-adjust
    workbook = load_workbook("./analysis/analysis.xlsx")
    worksheet = workbook["Suivi Bets"]

    dims = {}
    for row in worksheet.rows:
        for cell in row:
            if cell.value:
                dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
    for col, value in dims.items():
        worksheet.column_dimensions[col].width = value

    workbook.save("./analysis/analysis.xlsx")
    result.clear()

######################################GET AND WRITE DATAS########################################################
for sheet in xl_file.sheet_names[1:]:
    data = pd.read_excel(xl_file, sheet).dropna(axis=0)

    # Get list championship who played this special date
    list_championship = []
    for _, row in data.iterrows():
        if row["Championnats"] not in list_championship:
            list_championship.append(row["Championnats"])

    # Data frame from a specific Championship
    for championship in list_championship:
        data_championship = data[data["Championnats"] == championship]

        for key, value in NEW_CONVERSION_LIST.items():
            if value == championship:
                championship_format = key

        with open("./analysis/analysis.json", "r") as file:
            data_file = json.load(file)

        bet_cards_passed = data_file[championship_format]["Bet Cards Passed"]
        bet_cards_failed = data_file[championship_format]["Bet Cards Failed"]
        bet_corners_passed = data_file[championship_format]["Bet Corners Passed"]
        bet_corners_failed = data_file[championship_format]["Bet Corners Failed"]
        bet_global_passed = data_file[championship_format]["Bet Global Passed"]
        bet_global_failed = data_file[championship_format]["Bet Global Failed"]

        # Get Bets Infos
        for _, row in data_championship.iterrows():
            if row["Résultats Bet Cartons"] == "Passed":
                bet_cards_passed += 1
            else:
                bet_cards_failed += 1

            if row["Résultats Bet Corners"] == "Passed":
                bet_corners_passed += 1
            else:
                bet_corners_failed += 1

            if row["Résultats Bet Global"] == "Passed":
                bet_global_passed += 1
            else:
                bet_global_failed += 1

        # Update Datas in json file
        data_file[championship_format]["Bet Cards Passed"] = bet_cards_passed
        data_file[championship_format]["Bet Cards Failed"] = bet_cards_failed
        data_file[championship_format]["Bet Corners Passed"] = bet_corners_passed
        data_file[championship_format]["Bet Corners Failed"] = bet_corners_failed
        data_file[championship_format]["Bet Global Passed"] = bet_global_passed
        data_file[championship_format]["Bet Global Failed"] = bet_global_failed

        with open("./analysis/analysis.json", "w") as f:
            json.dump(data_file, f)


###### A TESTER

# Write in Excel
with open("analysis/analysis.json", encoding='utf-8-sig') as data_file:
    df = pd.read_json(data_file)

# Reverse Rows and Columns
df_transpose = df.transpose()
df_transpose.to_excel("./analysis/analysis.xlsx", sheet_name="Suivi Bets", encoding='utf-8', index=True)

# Width Cells Auto-adjust
workbook = load_workbook("./analysis/analysis.xlsx")
worksheet = workbook["Suivi Bets"]

dims = {}
for row in worksheet.rows:
    for cell in row:
        if cell.value:
            dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
for col, value in dims.items():
    worksheet.column_dimensions[col].width = value

workbook.save("./analysis/analysis.xlsx")

list_championship.clear()
