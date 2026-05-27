from docling.document_converter import DocumentConverter

def parse_document(file_path):
    converter = DocumentConverter()
    result = converter.convert(file_path)
    text = result.document.export_to_markdown()
    return text