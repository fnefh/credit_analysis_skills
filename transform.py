from docling.document_converter import DocumentConverter

source = "analysis.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
test=result.document.export_to_markdown()
with open("analysis.md", "w") as f:
    f.write(test)
