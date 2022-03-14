from django.core.validators import ValidationError

def validate_symbols(value):
    if '@' in value or '#' in value:
        raise ValidationError("'@'와 '#'는 포함될 수 없습니다")
