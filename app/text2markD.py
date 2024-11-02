import streamlit as st

def process_text(text):
    # Simple text processing to format headings and bullet points
    lines = text.split('\n')
    processed_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.endswith(':'):
            # Convert lines ending with ':' to headings
            processed_lines.append(f'## {stripped_line[:-1]}')
        elif stripped_line.startswith('- ') or stripped_line.startswith('* '):
            # Keep bullet points as is
            processed_lines.append(f'{stripped_line}')
        else:
            # Regular text
            processed_lines.append(stripped_line)
    return '\n\n'.join(processed_lines)

st.title("Text to Markdown Converter")

input_text = st.text_area("Paste your unstructured text here:")

if st.button("Convert to Markdown"):
    if input_text.strip() == "":
        st.warning("Please paste some text to convert.")
    else:
        markdown_text = process_text(input_text)
        st.subheader("Converted Markdown:")
        st.code(markdown_text, language='markdown')

        # Option to download the markdown file
        st.download_button("Download Markdown File",
                           data=markdown_text,
                           file_name="converted.md",
                           mime="text/markdown")
