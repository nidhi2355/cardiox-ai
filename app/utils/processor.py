import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_pdfs(pdf_folder_path):
    # 1. Initialize the list for all chunks
    all_chunks = []
    
    # 2. Define the Splitter (300-500 tokens as per your doc)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )

    # 3. Loop through every PDF in the folder
    for file in os.listdir(pdf_folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(file_path)
            
            # Load and split the document
            docs = loader.load_and_split(text_splitter=text_splitter)
            all_chunks.extend(docs)
            print(f"Processed {file}: Created {len(docs)} chunks.")

    return all_chunks

if __name__ == "__main__":
    # Test the processor
    path = "./data/pdfs/"
    chunks = process_pdfs(path)
    print(f"Total chunks created: {len(chunks)}")