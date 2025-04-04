
# import csv
# def account_statement(account_number):
#     activities = []
#     try:
#         with open('activity_log.csv', newline='') as logfile:
#             reader = csv.DictReader(logfile)
#             for row in reader:
#                 if int(row['Account Number']) == account_number:
#                     activities.append((row['Timestamp'], row['Activity']))
#     except FileNotFoundError:
#         print("Activity log file not found.")
#         return
    
#     if activities:
#         print(f"Account Statement for Account Number: {account_number}")
#         print("--------------------------------------------------")
#         for timestamp, activity in activities:
#             print(f"{timestamp}: {activity}")
#     else:
#         print("No activities found for this account.")
# # import csv
# from fpdf import FPDF

# def generate_pdf(account_number, activities):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt=f"Account Statement for Account Number: {account_number}", ln=True, align="C")
#     pdf.cell(200, 10, txt="--------------------------------------------------", ln=True, align="C")
#     for timestamp, activity in activities:
#         pdf.cell(200, 10, txt=f"{timestamp}: {activity}", ln=True, align="L")
#     pdf.output(f"account_statement_{account_number}.pdf")

# def account_statement(account_number):
#     activities = []
#     try:
#         with open('activity_log.csv', newline='') as logfile:
#             reader = csv.DictReader(logfile)
#             for row in reader:
#                 if int(row['Account Number']) == account_number:
#                     activities.append((row['Timestamp'], row['Activity']))
#     except FileNotFoundError:
#         print("Activity log file not found.")
#         return
    
#     if activities:
#         print(f"Account Statement for Account Number: {account_number}")
#         print("--------------------------------------------------")
#         for timestamp, activity in activities:
#             print(f"{timestamp}: {activity}")
#         generate_pdf(account_number, activities)
#         print("PDF file generated successfully.")
#     else:
#         print("No activities found for this account.")
# import csv
# from fpdf import FPDF

# def generate_pdf(account_number, activities):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt=f"Account Statement for Account Number: {account_number}", ln=True, align="C")
#     pdf.cell(200, 10, txt="--------------------------------------------------", ln=True, align="C")
#     for timestamp, activity in activities:
#         pdf.cell(200, 10, txt=f"{timestamp}: {activity}", ln=True, align="L")
#     pdf.output(f"account_statement_{account_number}.pdf")

# def account_statement(account_number):
#     activities = []
#     try:
#         with open('activity_log.csv', newline='') as logfile:
#             reader = csv.DictReader(logfile)
#             for row in reader:
#                 if int(row['Account Number']) == account_number:
#                     activities.append((row['Timestamp'], row['Activity']))
#     except FileNotFoundError:
#         print("Activity log file not found.")
#         return
    
#     if activities:
#         print(f"Account Statement for Account Number: {account_number}")
#         print("--------------------------------------------------")
#         for timestamp, activity in activities:
#             print(f"{timestamp}: {activity}")
#         generate_pdf(account_number, activities)
#         print("PDF file generated successfully.")
#     else:
#         print("No activities found for this account.")


# import csv
# from docx import Document
# from docx.shared import Pt

# def generate_word_doc(account_number, activities):
#     doc = Document()
#     doc.add_heading(f"Account Statement for Account Number: {account_number}", level=1)
#     doc.add_paragraph("--------------------------------------------------")

#     for timestamp, activity in activities:
#         p = doc.add_paragraph()
#         run = p.add_run(f"{timestamp}: {activity}")
#         run.font.size = Pt(12)

#     doc.save(f"account_statement_{account_number}.docx")

# def account_statement(account_number):
#     activities = []
#     try:
#         with open('activity_log.csv', newline='') as logfile:
#             reader = csv.DictReader(logfile)
#             for row in reader:
#                 if int(row['Account Number']) == account_number:
#                     activities.append((row['Timestamp'], row['Activity']))
#     except FileNotFoundError:
#         print("Activity log file not found.")
#         return
    
#     if activities:
#         print(f"Account Statement for Account Number: {account_number}")
#         print("--------------------------------------------------")
#         for timestamp, activity in activities:
#             print(f"{timestamp}: {activity}")
#         generate_word_doc(account_number, activities)
#         print("Word document generated successfully.")
#     else:
#         print("No activities found for this account.")
# import csv
# from docx import Document
# from docx.shared import Pt
# from datetime import datetime

# def generate_word_doc(account_number, activities):
#     doc = Document()
#     doc.add_heading(f"Account Statement for Account Number: {account_number}", level=1)
#     doc.add_paragraph("--------------------------------------------------")

#     for timestamp, activity in activities:
#         p = doc.add_paragraph()
#         run = p.add_run(f"{timestamp}: {activity}")
#         run.font.size = Pt(12)

#     doc.save(f"account_statement_{account_number}.docx")

# def account_statement(account_number):
#     activities = []
#     try:
#         with open('activity_log.csv', newline='') as logfile:
#             reader = csv.DictReader(logfile)
#             for row in reader:
#                 if int(row['Account Number']) == account_number:
#                     activities.append((row['Timestamp'], row['Activity']))
#     except FileNotFoundError:
#         print("Activity log file not found.")
#         return
    
#     if activities:
#         print(f"Account Statement for Account Number: {account_number}")
#         print("--------------------------------------------------")
#         for timestamp, activity in activities:
#             print(f"{timestamp}: {activity}")
#         generate_word_doc(account_number, activities)
#         print("Word document generated successfully.")
#     else:
#         print("No activities found for this account.")

# import csv
# from fpdf import FPDF
# from datetime import datetime

# class PDF(FPDF):
#     def header(self):
#         self.set_font('Arial', 'B', 12)
#         self.cell(200, 10, f"Account Statement for Account Number: {self.account_number}", ln=True, align='C')
#         self.cell(200, 10,  ln=True, align='C')

#     def footer(self):
#         self.set_y(-15)
#         self.set_font('Arial', 'I', 8)
#         self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

#     def account_statement_table(self, header, activities):
#         self.set_font('Arial', 'B', 12)
#         self.cell(40, 10, header[0], 1)
#         self.cell(40, 10, header[1], 1)
#         self.cell(60, 10, header[2], 1)
#         self.cell(50, 10, header[3], 1)
#         self.ln()
#         self.set_font('Arial', '', 12)
#         for row in activities:
#             self.cell(40, 10, row['Date'], 1)
#             self.cell(40, 10, row['Time'], 1)
#             self.cell(60, 10, row['Activity'], 1)
#             self.cell(50, 10, row['Balance'], 1)
#             self.ln()

# def generate_pdf(account_number, activities):
#     pdf = PDF()
#     pdf.account_number = account_number
#     pdf.add_page()
#     header = ['Date', 'Time', 'Activity', 'Balance']
#     pdf.account_statement_table(header, activities)
#     pdf.output(f"account_statement_{account_number}.pdf")

# def account_statement(account_number):
#     activities = []
#     try:
#         with open('activity_log.csv', newline='') as logfile:
#             reader = csv.DictReader(logfile)
#             for row in reader:
#                 if int(row['Account Number']) == account_number:
#                     timestamp = datetime.strptime(row['Timestamp'], '%Y-%m-%d %H:%M:%S')
#                     activity = {
#                         'Date': timestamp.strftime('%Y-%m-%d'),
#                         'Time': timestamp.strftime('%H:%M:%S'),
#                         'Activity': row['Activity'],
#                         'Amount': ''  # Assuming amount is included in activity description
#                     }
#                     activities.append(activity)
#     except FileNotFoundError:
#         print("Activity log file not found.")
#         return
    
#     if activities:
#         print(f"Account Statement for Account Number: {account_number}")
#         print("--------------------------------------------------")
#         for activity in activities:
#             print(f"{activity['Date']} {activity['Time']}: {activity['Activity']}")
#         generate_pdf(account_number, activities)
#         print("PDF document generated successfully.")
#     else:
#         print("No activities found for this account.")

import csv
from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(200, 10, f"Account Statement for Account Number: {self.account_number}", ln=True, align='C')
        self.cell(200, 10, "--------------------------------------------------", ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def account_statement_table(self, header, activities):
        self.set_font('Arial', 'B', 12)
        self.cell(40, 10, header[0], 1)
        self.cell(40, 10, header[1], 1)
        self.cell(60, 10, header[2], 1)
        self.cell(50, 10, header[3], 1)
        self.ln()
        self.set_font('Arial', '', 12)
        for row in activities:
            self.cell(40, 10, row['Date'], 1)
            self.cell(40, 10, row['Time'], 1)
            self.cell(60, 10, row['Activity'], 1)
            self.cell(50, 10, row['Amount'], 1)
            self.ln()

def generate_pdf(account_number, activities):
    pdf = PDF()
    pdf.account_number = account_number
    pdf.add_page()
    header = ['Date', 'Time', 'Activity', 'Amount']
    pdf.account_statement_table(header, activities)
    # Save to a temporary directory or a known accessible directory
    output_dir = os.path.join(os.path.expanduser('~'), 'Documents')
    output_path = os.path.join(output_dir, f"account_statement_{account_number}.pdf")
    pdf.output(output_path)
    print(f"PDF document generated successfully at {output_path}")

def account_statement(account_number):
    activities = []
    try:
        with open('activity_log.csv', newline='') as logfile:
            reader = csv.DictReader(logfile)
            for row in reader:
                if int(row['Account Number']) == account_number:
                    timestamp = datetime.strptime(row['Timestamp'], '%Y-%m-%d %H:%M:%S')
                    activity = {
                        'Date': timestamp.strftime('%Y-%m-%d'),
                        'Time': timestamp.strftime('%H:%M:%S'),
                        'Activity': row['Activity'],
                        'Amount': ''  # Assuming amount is included in activity description
                    }
                    activities.append(activity)
    except FileNotFoundError:
        print("Activity log file not found.")
        return
    
    if activities:
        print(f"Account Statement for Account Number: {account_number}")
        print("--------------------------------------------------")
        for activity in activities:
            print(f"{activity['Date']} {activity['Time']}: {activity['Activity']}")
        generate_pdf(account_number, activities)
    else:
        print("No activities found for this account.")

def log_activity(account_number, activity):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('activity_log.csv', 'a', newline='') as logfile:
        fieldnames = ['Timestamp', 'Account Number', 'Activity']
        writer = csv.DictWriter(logfile, fieldnames=fieldnames)
        if logfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'Timestamp': timestamp, 'Account Number': account_number, 'Activity': activity})
