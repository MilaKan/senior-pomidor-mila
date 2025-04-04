def format_phone_number(digits):
    format_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return format_number

print(format_phone_number("1234567890"))