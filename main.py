from pdf_parser import extract_text_from_pdf, parse_fields_from_text, convert_to_json


def process_paystub(pdf_path, fields_to_extract):
    """
    Processes the PDF paystub to extract specified fields and return JSON data.
    """
    text = extract_text_from_pdf(pdf_path)
    # print("text=", text)
    if not text:
        print("No text extracted from PDF.")
        return None
    parsed_data = parse_fields_from_text(text, fields_to_extract)
    json_data = convert_to_json(parsed_data)
    return json_data


if __name__ == "__main__":
    # Define the path to your PDF file
    pdf_path = "paystub.pdf"

    # Define the fields you want to extract
    fields_to_extract = [
        "Employee Name",
        "Employee ID",
        "Pay Period",
        "Total Pay",
        "Net Pay",
        # Add other fields as needed
    ]

    # Process the paystub and print the JSON output
    json_output = process_paystub(pdf_path, fields_to_extract)
    if json_output:
        print(json_output)
