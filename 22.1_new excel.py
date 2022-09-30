import openpyxl




wb = openpyxl.Workbook()
sheet = wb.create_sheet("DummySheet", 4)
sheet["A1"].value = "This is sample writing"
wb.save("New wb using selenium pyhton.xlsx")