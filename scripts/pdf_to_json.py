import os
import json
from pathlib import Path
from PyPDF2 import PdfReader

PDF_ROOT = Path(".")
OUTPUT = Path("json_output")
OUTPUT.mkdir(exist_ok=True)

for pdf_file in PDF_ROOT.rglob("*.pdf"):
    reader = PdfReader(str(pdf_file))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append({"page": i + 1, "text": text})
    pdf_json = {
        "filename": str(pdf_file),
        "page_count": len(pages),
        "pages": pages
    }
    out_path = OUTPUT / (pdf_file.name.replace(".pdf", ".json"))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(pdf_json, f, ensure_ascii=False, indent=2)
    print(f"Extracted {pdf_file} -> {out_path}")
