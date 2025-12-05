import sys
try:
    import pypdf
    print("pypdf available")
    reader = pypdf.PdfReader("files_private/IRS Project.pdf")
    print(reader.pages[0].extract_text())
except ImportError:
    try:
        import PyPDF2
        print("PyPDF2 available")
        reader = PyPDF2.PdfReader("files_private/IRS Project.pdf")
        print(reader.pages[0].extract_text())
    except ImportError:
        print("No PDF library found")

