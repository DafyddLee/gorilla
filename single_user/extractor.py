import re
import pandas as pd
from datetime import datetime
import streamlit as st

def parse_lab_results(textfile):

    # textfile = 'textfiles/173293317.txt'  # Replace with your file path
    with open(textfile, 'r') as file:
        text_content = file.read()
    # Split the text into episodes
    episodes = re.split(r'Episode\s+\w+', text_content)
    # Remove the first split which does not contain lab data
    episodes = episodes[1:]

    # Initialize results dictionary
    results = {}

    # Process each episode
    for episode in episodes:
        # Find the date for the episode
        date_match = re.search(r'Date collected\s+(\d{2}/\d{2}/\d{4})', episode)
        if not date_match:
            continue
        date = datetime.strptime(date_match.group(1), '%d/%m/%Y').date()

        # Define the tests and corresponding regex patterns
        tests = {
            "Urine protein": r"Urine protein\s+([\d.]+)?\s*g/L",
            "Urine protein creat ratio": r"Urine protein\s+creat ratio\s+([\d.]+)?\s*H?\s*g/mmol creat",
            "Creatinine": r"Creatinine\s+(\d+)\s*L?\s*umol/L",
            "eGFR (CKD-EPI)": r"eGFR \(CKD-EPI formula\)\s+(\d+|\>\d+)\s*mL/min/1\.73 m2",
            "eGFR (MDRD)": r"eGFR \(MDRD formula\)\s+([\d]+|\>\d+)\s*mL/min/1\.73 m2",
        }

        # Initialize the date entry in results
        results.setdefault(date, {test: 'N/A' for test in tests})

        # Search for each test result in the episode
        for test, pattern in tests.items():
            match = re.search(pattern, episode)
            if match and match.group(1):
                results[date][test] = match.group(1)

    # Convert to DataFrame and transpose
    df = pd.DataFrame.from_dict(results, orient='index')
    df_transposed = df.transpose()

    output_file = 'sheets/'  + st.session_state.id  + '.xlsx'
    df_transposed.to_excel(output_file, index_label='Investigation')

    print(f"Excel file saved: {output_file}")

    df_transposed = df_transposed.reset_index()

    # Rename the first column to 'Investigation'
    df_transposed.rename(columns={'index': 'Investigation'}, inplace=True)
    # df_transposed = df_transposed.rename(columns={'index': 'Investigation'})

    return df_transposed

# Read the text from the file
# input_file_path = 'textfiles/173293317.txt'  # Replace with your file path
# with open(input_file_path, 'r') as file:
#     text_content = file.read()

# df_transposed = parse_lab_results(text_content)

# The output file path
# parse_lab_results('textfiles/173293317.txt')