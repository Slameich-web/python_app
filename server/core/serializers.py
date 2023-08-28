from base64 import b64encode

from rest_framework import serializers

from core.models import BotSettings, TelegramMedia


class BotSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotSettings

        exclude = ('id',)


class TelegramMediaSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    class Meta:
        model = TelegramMedia

        fields = '__all__'

        read_only_fields = ('type', 'file', 'id')

    def get_file(self, obj):
        with open(obj.file.path, 'rb') as file:
            return b64encode(file.read())
