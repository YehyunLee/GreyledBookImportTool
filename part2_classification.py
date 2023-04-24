def classification(pdf_string: str) -> list[str]:
    split_lines = pdf_string.split('\n')
    new_list_without_empty = [item for item in split_lines if item != '']  # Using complehension

    # title for item in new_list_without_empty in new_list_without_empty if isinstance(item, list)
    return new_list_without_empty