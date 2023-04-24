def classification(pdf_string: str) -> dict[str, list[str]]:
    split_lines = pdf_string.split('\n')
    list_without_empty = [item for item in split_lines if not item == '']  # Using complehension

    big_elements = [item for item in list_without_empty if '[' in item and ']' in item]
    list_without_empty_big_elements = [item for item in list_without_empty if not isinstance(item, list)]

    paragraphs = [item for item in list_without_empty_big_elements if '\t' in item]

    bullet_points = [item for item in list_without_empty_big_elements if contains_symbols(item)]

    data = {'big_elements': big_elements, 'paragraphs': paragraphs, 'bullet_points': bullet_points}
    return data


def contains_symbols(string: str) -> bool:
    symbols = ["•", "‣", "⁃", "⁌", "⁍", "∙", "○", "●", "◘", "◦", "☙", "❥", "❧", "⦾", "⦿", ...]
    return any(each_chr in symbols for each_chr in string)
