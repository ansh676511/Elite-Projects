import pandas as pd
from fpdf import FPDF

# Step 1: CSV file read karo
df = pd.read_csv("data.csv")

# Step 2: Data analysis
average_scores = df.mean(numeric_only=True)
topper = df.loc[df["Maths"].idxmax()]["Name"]

# Step 3: PDF Report banao
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Student Marks Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, f"Average Maths Marks: {average_scores['Maths']:.2f}", ln=True)
pdf.cell(200, 10, f"Average Science Marks: {average_scores['Science']:.2f}", ln=True)
pdf.cell(200, 10, f"Average English Marks: {average_scores['English']:.2f}", ln=True)
pdf.cell(200, 10, f"Topper in Maths: {topper}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Full Data Table:", ln=True)

pdf.set_font("Arial", size=10)
# Table Header
pdf.cell(40, 10, "Name", border=1)
pdf.cell(30, 10, "Maths", border=1)
pdf.cell(30, 10, "Science", border=1)
pdf.cell(30, 10, "English", border=1)
pdf.ln()

# Table Rows
for index, row in df.iterrows():
    pdf.cell(40, 10, row["Name"], border=1)
    pdf.cell(30, 10, str(row["Maths"]), border=1)
    pdf.cell(30, 10, str(row["Science"]), border=1)
    pdf.cell(30, 10, str(row["English"]), border=1)
    pdf.ln()

# Save PDF
pdf.output("report.pdf")

print("✅ Report generated successfully as 'report.pdf'")
