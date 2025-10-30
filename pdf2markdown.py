import pymupdf4llm
import pathlib

def convert_pdf_to_markdown(input_pdf_path, output_md_path):
    """
    Converts a PDF file to a structured Markdown file using pymupdf4llm.
    
    :param input_pdf_path: Path to the input PDF file (e.g., your extracted chapter).
    :param output_md_path: Path for the new Markdown file (.md) to be created.
    """
    try:
        # Convert the entire document to a single Markdown string
        # pymupdf4llm intelligently detects headers, lists, and tables for formatting.
        md_text = pymupdf4llm.to_markdown(input_pdf_path)
        
        # Write the Markdown text to an output file using pathlib for clean path handling
        pathlib.Path(output_md_path).write_bytes(md_text.encode("utf-8"))
        
        print(f"✅ Successfully converted {input_pdf_path} to {output_md_path}")

    except FileNotFoundError:
        print(f"❌ Error: The file {input_pdf_path} was not found. Check the file name.")
    except Exception as e:
        print(f"❌ An error occurred during conversion: {e}")

# --- Configuration ---
INPUT_FILE = "Chapter_4_CAST-Handbook.pdf"  # Your previous output
OUTPUT_FILE = "Chapter_4_CAST-Handbook.md"      # New Markdown file name
# ---------------------

# Run the conversion
if __name__ == "__main__":
    convert_pdf_to_markdown(INPUT_FILE, OUTPUT_FILE)
