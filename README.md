# text2markD (Text to Markdown) Converter

A Python application that converts unstructured text into clean, structured Markdown files. This repository contains:

- A Streamlit web application.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Tkinter Version](#tkinter-version)
  - [Streamlit Version](#streamlit-version)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Convert unstructured text to Markdown format.
- Supports headings, bullet points, and regular text.
- Two interfaces:
  - Desktop GUI using Tkinter.
  - Web-based interface using Streamlit.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- For the Streamlit version:
  - Install Streamlit:

    ```bash
    pip install streamlit
    ```

## Usage

### Streamlit Version

1. Navigate to the `streamlit_version` directory:

    ```bash
    cd streamlit_version
    ```

2. Run the application (with poetry):

    ```bash
    poetry run streamlit run app/text2markD_app.py
    ```

3. Open the URL provided in the terminal (usually `http://localhost:8501`) in your web browser.
4. Use the interface to paste text and convert it to Markdown.
5. Download the converted Markdown file using the **"Download Markdown File"** button.
