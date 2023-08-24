from django.core.exceptions import ValidationError


def validate_telegram_media_size(file_field_obj):
    filesize = file_field_obj.file.size

    megabyte_limit = 5
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError(f"Максимальный размер файла -  {megabyte_limit}MB")
