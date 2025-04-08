# ECE Design Lab Project

This repository contains the code for the ECE Design Lab Project.

## Getting Started

You have two options to work with this project:

### Option 1: Using Google Colab (Recommended)

1. Click the "Open in Colab" button below:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarMar888/ECEDesignLabProj/blob/main/MainClean.ipynb)

2. The notebook will open in Google Colab, where you can run the code directly in your browser.

### Option 2: Cloning the Repository and Using Virtual Environment

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/MarMar888/ECEDesignLabProj.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ECEDesignLabProj
   ```

3. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

6. Open the `MainClean.ipynb` notebook in your browser.

## Requirements

The project requires:
- Python 3.8 or higher
- Virtual environment (optional but recommended)
- Dependencies listed in `requirements.txt`

If you're using Google Colab, all dependencies will be handled automatically.

## Project Structure

- `MainClean.ipynb`: Main notebook containing the project code
- `requirements.txt`: List of Python dependencies
- `3D_Print_Jobs_1743518886.csv`: Dataset file
