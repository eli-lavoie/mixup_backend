import boto3
import os
import mimetypes
import json
from django.http import HttpResponse
from rest_framework.views import APIView


class s3_link(APIView):
  
  def get(self, request):
    s3 = boto3.client('s3', 'us-east-2')
    s3_bucket = os.environ.get('S3_BUCKET')

    file_name = request.GET['file_name']
    file_type = mimetypes.guess_type(file_name)[0]
    presigned_post = s3.generate_presigned_post(
      Bucket = s3_bucket,
      Key = file_name,
      Fields = {"acl": "public-read", "Content-Type": file_type },
      Conditions = [
        {"acl": "public-read"},
        {"Content-Type": file_type}
      ],
      ExpiresIn= 3600
    )

    data = {
      "signed_url": presigned_post,
      "url": 'https://%s.s3.amazonaws.com/%s' % (s3_bucket, file_name)
    }
    # print(json.dumps(data))
    return HttpResponse(json.dumps(data))