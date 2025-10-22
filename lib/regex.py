import re

# Name regex:
# - Starts with a capital letter
# - Allows apostrophes and hyphens after the first letter (e.g., D'Angelo, Taylor-Joy)
# - Optionally allows a space and another valid name part
name = r"^[A-Z][a-z]*(?:['-][A-Z]?[a-z]+)*(?: [A-Z][a-z]*(?:['-][A-Z]?[a-z]+)*)?$"
name_regex = re.compile(name)

# Phone regex (unchanged)
phone_number = r"^(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Email regex (unchanged)
email_address = r"^[A-Za-z][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$"
email_regex = re.compile(email_address)



