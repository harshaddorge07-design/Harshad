import openpyxl
import os 
from rich.console import Console
console = Console()
from pyfiglet import figlet_format

#INITIALIZATION
file_name = "bank_records.xlsx"

print(figlet_format("BY BANK"))

# Excel Creation Function

def create_excel_file():
    """this function create a excel name bank_records.xlsx"""
    if not os.path.exists(file_name):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Bank Records"
        headers = ["Account No", "Name", "PIN", "Transaction ID", "transaction Type", "Amount", 
                   "Previous Balance", "Current Balance", "Date-Time"]
        sheet.append(headers)

        wb.save(file_name)
        wb.close()
        console.print("[bold cyan]Excel File created successfully[/bold cyan]")
create_excel_file()
# os.startfile(file_name)

