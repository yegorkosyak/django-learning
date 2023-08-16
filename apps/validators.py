from django.core.validators import RegexValidator

phone_regex_validator = RegexValidator(
    regex=r"^\d{7,10}$", message="Phone number must consist of 7-10 digits."
)
