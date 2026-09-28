import re


records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]


def extract_names(records):
    names = []

    for record in records:
        match = re.search(r"Name:\s*([^|]+)", record)

        if match:
            names.append(match.group(1).strip())

    return names


def extract_emails(records):
    emails = []

    pattern = r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}"

    for record in records:
        match = re.search(pattern, record)

        if match:
            emails.append(match.group())

    return emails


def normalize_phones(records):
    phones = []

    # Matches all of these:
    # (555) 123-4567
    # 555.987.6543
    # 555 111 2222
    # (555)444-3333
    pattern = r"\(?(\d{3})\)?[\s.-]*(\d{3})[\s.-]*(\d{4})"

    for record in records:
        match = re.search(pattern, record)

        if match:
            area = match.group(1)
            prefix = match.group(2)
            line = match.group(3)

            phones.append(f"{area}-{prefix}-{line}")

    return phones


def extract_dates(records):
    dates = []

    # Matches:
    # MM/DD/YYYY
    # MM-DD-YYYY
    # YYYY/MM/DD
    pattern = r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}/\d{2}/\d{2})\b"

    for record in records:
        match = re.search(pattern, record)

        if match:
            dates.append(match.group())

    return dates


# Bonus
def parse_records(records):
    parsed = []

    for record in records:
        name_match = re.search(r"Name:\s*([^|]+)", record)
        email_match = re.search(
            r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}",
            record
        )
        phone_match = re.search(
            r"\(?(\d{3})\)?[\s.-]*(\d{3})[\s.-]*(\d{4})",
            record
        )
        date_match = re.search(
            r"\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}/\d{2}/\d{2})\b",
            record
        )

        phone = None

        if phone_match:
            phone = (
                f"{phone_match.group(1)}-"
                f"{phone_match.group(2)}-"
                f"{phone_match.group(3)}"
            )

        parsed.append({
            "name": name_match.group(1).strip() if name_match else None,
            "email": email_match.group() if email_match else None,
            "phone": phone,
            "joined": date_match.group() if date_match else None,
        })

    return parsed


# Test output

print("Names:")
print(extract_names(records))

print("\nEmails:")
print(extract_emails(records))

print("\nNormalized Phones:")
print(normalize_phones(records))

print("\nDates:")
print(extract_dates(records))

print("\nParsed Records:")
for record in parse_records(records):
    print(record)