from PyPDF2 import PdfReader, PdfWriter

def extract_pdf_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    """
    Extracts a range of pages from an input PDF and saves them to a new PDF.

    :param input_pdf_path: Path to the original PDF file.
    :param output_pdf_path: Path for the new PDF file to be created.
    :param start_page: The first page number to include (e.g., 34 for page 34).
    :param end_page: The last page number to include (e.g., 97 for page 97).
    """
    try:
        # Create a PdfReader object for the input file
        reader = PdfReader(input_pdf_path)
        
        # Create a PdfWriter object for the new file
        writer = PdfWriter()

        # PDF page numbers are 1-based, but Python indices are 0-based.
        # To get pages from P_start to P_end (inclusive), the slice is [P_start-1 : P_end].
        # For pages 34 to 97, the indices are 33 to 97.
        start_index = start_page - 1
        end_index = end_page # The upper bound is non-inclusive in the loop below

        # Check if the requested page range is valid
        total_pages = len(reader.pages)
        if end_page > total_pages or start_page < 1:
            print(f"Error: Requested page range ({start_page}-{end_page}) is invalid. The PDF has {total_pages} pages.")
            return

        # Iterate through the desired page range and add pages to the writer
        for i in range(start_index, end_index):
            page = reader.pages[i]
            writer.add_page(page)

        # Write the content to the new PDF file
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)
            
        print(f"Successfully extracted pages {start_page} to {end_page} into {output_pdf_path}")

    except FileNotFoundError:
        print(f"Error: The file {input_pdf_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Configuration ---
INPUT_FILE = "CAST-Handbook.pdf"
OUTPUT_FILE = "Chapter_4_CAST-Handbook.pdf"
START_PAGE_NUMBER = 34
END_PAGE_NUMBER = 97
# ---------------------

# Run the function with your specified parameters
if __name__ == "__main__":
    # You must install the PyPDF2 library first: pip install PyPDF2
    extract_pdf_pages(
        input_pdf_path=INPUT_FILE,
        output_pdf_path=OUTPUT_FILE,
        start_page=START_PAGE_NUMBER,
        end_page=END_PAGE_NUMBER
    )
