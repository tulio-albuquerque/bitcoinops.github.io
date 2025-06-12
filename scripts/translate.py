import os
import sys
import re
from deep_translator import GoogleTranslator
from langdetect import detect

# Get the filename passed from GitHub Action
if len(sys.argv) < 2:
    print("Error: No filename provided for translation.")
    sys.exit(1)

source_file = sys.argv[1]
source_folder = os.path.dirname(source_file)
languages = [lang for lang in os.listdir("_posts") if len(lang) == 2]

CHUNK_SIZE = 5000  # Handle large markdown files

def extract_front_matter(content):
    """Extract YAML metadata while preserving formatting."""
    match = re.match(r"^(---\n.*?\n---\n)(.*)", content, re.DOTALL)
    return match.groups() if match else ("", content)

def chunk_text(text, chunk_size=CHUNK_SIZE):
    """Split large text into smaller chunks without breaking sentences."""
    chunks = []
    while len(text) > chunk_size:
        split_index = text[:chunk_size].rfind("\n")  # Prefer splitting at paragraph breaks
        split_index = split_index if split_index != -1 else chunk_size
        chunks.append(text[:split_index].strip())
        text = text[split_index:].strip()
    chunks.append(text)
    return chunks

with open(source_file, "r", encoding="utf-8") as f:
    content = f.read()

# Preserve front matter
front_matter, body = extract_front_matter(content)

# Chunk large content for translation
text_chunks = chunk_text(body)

for lang in languages:
    target_folder = f"_posts/{lang}/newsletters/"
    os.makedirs(target_folder, exist_ok=True)
    target_file = os.path.join(target_folder, os.path.basename(source_file))

    # Skip if translation already exists
    if os.path.exists(target_file):
        print(f"Skipping {source_file} for {lang} (already translated)")
        continue

    translated_chunks = [GoogleTranslator(source='en', target=lang).translate(chunk) for chunk in text_chunks]
    translated_body = "\n\n".join(translated_chunks)  # Reassemble translated text

    # Quality check - Ensure translation is in the expected language
    if detect(translated_body) != lang:
        print(f"⚠ Warning: Translation for {source_file} might be incorrect (Expected: {lang})")

    # Write translated file
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(front_matter + translated_body)