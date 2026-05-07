import re

def parse_text(text):

    """
    Extract units and amount from OCR text
    """

    data = {}

    # Find units
    units_match = re.search(
        r'(\d+)\s*(kWh|units|Units)',
        text,
        re.IGNORECASE
    )

    if units_match:
        data["units"] = int(units_match.group(1))
    else:
        data["units"] = 0

    # Find amount
    amount_match = re.search(r'(\d+)', text)

    if amount_match:
        data["amount"] = int(amount_match.group(1))
    else:
        data["amount"] = 0

    # Default billing days
    data["days"] = 30

    return data