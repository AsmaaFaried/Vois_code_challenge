from rest_framework import serializers

from attachment.models import Attachment


class UploadTextFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = '__all__'

    def validate(self, attrs):
        files = self.context.get('request').FILES.getlist('file')
        invalid_files = []
        for file in files:
            if not file.content_type.startswith('text/'):
                invalid_files.append(file.name)
        if invalid_files:
            raise serializers.ValidationError(
                {
                    'detail': f"There is file(s) not supported with names : {invalid_files} Only text files are allowed."
                }
                    )
        return attrs

    def create(self, validated_data):
        text_files = self.context.get('request').FILES.getlist('file')
        attachments = [Attachment(file=file) for file in text_files]
        Attachment.objects.bulk_create(attachments)
        return validated_data
