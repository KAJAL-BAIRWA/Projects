from openpyxl import Workbook
import os

def save_to_excel(data, solar_data):

    """
    Save data into Excel file
    """

    # Create output folder if missing
    os.makedirs("output", exist_ok=True)

    wb = Workbook()

    sheet = wb.active

    sheet.title = "Solar Report"

    # Headings
    sheet["A1"] = "Parameter"
    sheet["B1"] = "Value"

    # Data rows
    sheet["A2"] = "Units"
    sheet["B2"] = data["units"]

    sheet["A3"] = "Amount"
    sheet["B3"] = data["amount"]

    sheet["A4"] = "Solar Size (kW)"
    sheet["B4"] = solar_data["system_size_kw"]

    sheet["A5"] = "Estimated Cost"
    sheet["B5"] = solar_data["estimated_cost_rs"]

    sheet["A6"] = "Payback Years"
    sheet["B6"] = solar_data["payback_years"]

    # Output path
    file_path = "output/result.xlsx"

    # Save file
    wb.save(file_path)

    return file_path



