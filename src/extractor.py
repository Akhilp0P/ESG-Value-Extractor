import re
from src.config import METRIC_CONFIG, VALUE_REGEX

def extract_value(text: str, anchors: list) -> str:
    """
    Finds the first occurrence of any anchor phrase and extracts the
    nearest numerical value following it.
    """
    for anchor in anchors:
        # Case-insensitive search for the anchor
        match = re.search(re.escape(anchor), text, re.IGNORECASE)
        if match:
            # Define a window (200 chars) after the anchor to look for the number
            start_idx = match.end()
            window = text[start_idx : start_idx + 200]

            # Search for the first number in the window
            val_match = re.search(VALUE_REGEX, window)
            if val_match:
                number = val_match.group(1)
                unit = val_match.group(2).strip() if val_match.group(2) else ""

                # --- FIX: Avoid capturing percentages for emission metrics ---
                # If the unit is a %, it's likely a share/percentage, not a value.
                if "%" in unit:
                    # Try to find a second number in the window that ISN'T a percentage
                    remaining_window = window[val_match.end():]
                    second_match = re.search(VALUE_REGEX, remaining_window)
                    if second_match:
                        number = second_match.group(1)
                        unit = second_match.group(2).strip() if second_match.group(2) else ""
                    else:
                        return "Not Found (Percentage detected)"

                return f"{number} {unit}".strip()

    return "Not Found"

def process_report(text: str) -> dict:
    """
    Iterates through all configured metrics and extracts values from the text.
    """
    results = {}
    for metric_name, anchors in METRIC_CONFIG.items():
        value = extract_value(text, anchors)
        results[metric_name] = value

    return results
