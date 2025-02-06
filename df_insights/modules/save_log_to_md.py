from .analyse_column_consistency import analyze_column_consistency
from .check_identifiers import check_identifiers

def save_log_to_md(df, filename="data_analysis_log.md"):
    """
    Runs data consistency analysis, finds possible unique identifiers and composite keys,
    and saves the results into a well-structured markdown log file.

    Args:
        df (pd.DataFrame): The input dataframe.
        filename (str): The name of the markdown file to save.

    Returns:
        None: Saves the log to a markdown file.
    """
    # Analyze consistency for the entire dataset
    full_consistency_report = analyze_column_consistency(df).fillna("N/A")

    # Identify highly unique identifiers and their consistency
    highly_unique_report, composite_keys = check_identifiers(df)
    if highly_unique_report is not None:
        highly_unique_report = highly_unique_report.fillna("N/A")

    # Start writing the markdown content
    md_content = "# Data Analysis Log\n\n"
    md_content += f"**Total Rows:** {df.shape[0]}  \n"
    md_content += f"**Total Columns:** {df.shape[1]}\n"
    md_content += f"**Total NaN Values:** {df.isna().sum().sum()}\n"
    md_content += f"**Total Duplicated Rows:** {df.duplicated().sum()}\n"

    # Highly Unique Identifiers Section
    if highly_unique_report is not None:
        md_content += "## Highly Unique Identifiers Consistency Report\n"
        md_content += "| {:<20} | {:<10} | {:<12} | {:<10} | {:<14} | {:<9} | {:<10} | {:<10} |\n".format(
            "Column Name", "Data Type", "Unique Values", "Duplicates", "Missing Values", "% Missing", "Max Length", "Min Length"
        )
        md_content += "| " + "-" * 18 + " | " + "-" * 10 + " | " + "-" * 12 + " | " + "-" * 10 + " | " + "-" * 14 + " | " + "-" * 9 + " | " + "-" * 10 + " | " + "-" * 10 + " |\n"

        for col in highly_unique_report.index:
            row = highly_unique_report.loc[col]
            md_content += "| {:<20} | {:<10} | {:<12} | {:<10} | {:<14} | {:<9.2f} | {:<10} | {:<10} |\n".format(
                col, str(row['Data Type']), str(row['Unique Values']), str(row['Duplicate Values']),
                str(row['Missing Values']), float(row['Percentage Missing']), str(row['Max Length']), str(row['Min Length'])
            )

    else:
        md_content += "## No Highly Unique Identifiers Found\n\n"

    # Composite Keys Section
    if composite_keys:
        md_content += "## Composite Key Found\n"
        md_content += f"- `{', '.join(composite_keys)}`\n\n"
    else:
        md_content += "## No Composite Key Found\n\n"

    # Full Dataset Consistency Report
    md_content += "\n## Full Dataset Consistency Report\n"
    md_content += "| {:<20} | {:<10} | {:<12} | {:<10} | {:<14} | {:<9} | {:<10} | {:<10} |\n".format(
        "Column Name", "Data Type", "Unique Values", "Duplicates", "Missing Values", "% Missing", "Max Length", "Min Length"
    )
    md_content += "| " + "-" * 18 + " | " + "-" * 10 + " | " + "-" * 12 + " | " + "-" * 10 + " | " + "-" * 14 + " | " + "-" * 9 + " | " + "-" * 10 + " | " + "-" * 10 + " |\n"

    for col in full_consistency_report.index:
        row = full_consistency_report.loc[col]
        md_content += "| {:<20} | {:<10} | {:<12} | {:<10} | {:<14} | {:<9.2f} | {:<10} | {:<10} |\n".format(
            col, str(row['Data Type']), str(row['Unique Values']), str(row['Duplicate Values']),
            str(row['Missing Values']), float(row['Percentage Missing']), str(row['Max Length']), str(row['Min Length'])
        )

    # Save to a markdown file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Log saved as {filename}")

