import hashlib

from django.core.files import File
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers

from oilandgasdata.task import upload_oilstub


class UploadFileSerializer(serializers.Serializer):
    upload_file = serializers.FileField(required=True)

    def create(self, validated_data):

        storage = FileSystemStorage()
        upload_file = self.validated_data.get('upload_file')

        storage.save(upload_file.name, File(upload_file))

        return upload_oilstub.delay(path=storage.path(upload_file.name), file_name=upload_file.name)
