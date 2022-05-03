import json
import os
import pandas as pd
from openpyxl import load_workbook
from constant import LIST_CHAMPIONSHIP, NEW_CONVERSION_LIST

xl_file = pd.ExcelFile("./Historique/Historique.xlsx")
result = {}


def check_sheet_already_analyze(sheet_name):
    try:
        with open("analysis/sheet_list.txt", "r") as sheet_file:
            data_sheet = sheet_file.read()
        if sheet_name in data_sheet:
            return True
        return False
    except FileNotFoundError:
        return False


def reverse_rows_columns(dataframe):
    dataframe_transpose = dataframe.transpose()
    dataframe_transpose.to_excel("./analysis/analysis.xlsx", sheet_name="Suivi Bets", encoding='utf-8', index=True)


def width_cells_auto_adjust(workbook_1):
    workbook_to_adjust = load_workbook(workbook_1)
    ws = workbook_to_adjust["Suivi Bets"]
    dims = {}
    for row in ws.rows:
        for cell in row:
            if cell.value:
                dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
    for col, value in dims.items():
        ws.column_dimensions[col].width = value
    workbook_to_adjust.save(workbook_1)


def analyze_datas():
    # Initialise Json File
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

        # Write in Excel File
        with open("analysis/analysis.json", encoding='utf-8-sig') as data_file:
            df = pd.read_json(data_file)

        # Reverse Rows and Columns
        reverse_rows_columns(dataframe=df)

        # Width Cells Auto-adjust
        width_cells_auto_adjust(workbook_1="./analysis/analysis.xlsx")

        result.clear()

    # GET AND WRITE DATAS
    for sheet in xl_file.sheet_names[1:]:
        if not check_sheet_already_analyze(sheet_name=sheet):
            data = pd.read_excel(xl_file, sheet).dropna(axis=0)
            # Write sheet in sheet_list
            if not data.empty:
                with open("analysis/sheet_list.txt", "a") as f:
                    f.write(f"{sheet}\n")

            # Get list championship who played this special date
            list_championship = []
            list_championship.clear()
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

        # Write in Excel
        with open("analysis/analysis.json", encoding='utf-8-sig') as data_file:
            df = pd.read_json(data_file)

        # Reverse Rows and Columns
        reverse_rows_columns(dataframe=df)

        # Width Cells Auto-adjust
        width_cells_auto_adjust(workbook_1="./analysis/analysis.xlsx")


if __name__ == "__main__":
    analyze_datas()
