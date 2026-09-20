import os
import sys
import pandas as pd
from src.pdf_engine import extract_text_from_pdf
from src.extractor import process_report
from src.exporter import export_to_csv

def main():
    # 1. Setup Paths
    project_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(project_dir, "data", "input")
    output_file = os.path.join(project_dir, "data", "output", "esg_values_results.csv")

    # Ensure directories exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # 2. Identify PDFs
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in {input_dir}. Please add some reports and run again.")
        return

    all_results = []

    # 3. Process each PDF
    for pdf_name in pdf_files:
        print(f"Processing: {pdf_name}...")
        pdf_path = os.path.join(input_dir, pdf_name)

        text = extract_text_from_pdf(pdf_path)
        if not text:
            print(f"Skipping {pdf_name} due to extraction error.")
            continue

        metrics = process_report(text)

        # Create a unique filename based on the PDF name
        report_name = os.path.splitext(pdf_name)[0]
        company_output_file = os.path.join(project_dir, "data", "output", f"results_{report_name}.csv")

        # Export this specific company's results immediately
        export_to_csv([metrics], company_output_file)

        # Also keep track for a master summary file
        metrics["File_Name"] = pdf_name
        ordered_metrics = {"File_Name": metrics["File_Name"]}
        ordered_metrics.update({k: v for k, v in metrics.items() if k != "File_Name"})
        all_results.append(ordered_metrics)

    # 4. Export master summary to one final file
    master_output_file = os.path.join(project_dir, "data", "output", "all_companies_summary.csv")
    export_to_csv(all_results, master_output_file)
    print("\nAll analyses complete! Individual reports and a master summary have been generated.")

if __name__ == "__main__":
    main()
