from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UploadTextFilesSerializer
class UploadFilesApiView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = []

    def post(self, request, *args, **kwargs):
        if not request.FILES.getlist('file'):
            return Response({"details": "There's no files entered to upload."})
        serializer = UploadTextFilesSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"details": "File(s) is uploaded successfully."})
