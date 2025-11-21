from docx import Document
import os

def extract_docx(file_path):
    doc = Document(file_path)
    content = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:  # ignore empty paragraphs
            style = para.style.name  # e.g., 'Heading 1', 'Normal'
            content.append({
                "text": text,
                "style": style
            })

    # Extract tables
    tables = []
    for table in doc.tables:
        table_data = []
        for row in table.rows:
            table_data.append([cell.text.strip() for cell in row.cells])
        tables.append(table_data)

    return {"paragraphs": content, "tables": tables}

# Example usage
all_files = os.listdir("submissions")
for file in all_files:
    if file.endswith(".docx"):
        result = extract_docx(os.path.join("submissions", file))
        print(f"{file} extracted, {len(result['paragraphs'])} paragraphs, {len(result['tables'])} tables")