from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import boto3


# Create your views here.


class SentimentAnalysisView(APIView):
    def post(self, request):
        text = request.data.get('text')

        if not text:
            return Response({"error": "Text is required"}, status=status.HTTP_400_BAD_REQUEST)

        comprehend = boto3.client('comprehend')
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response.get('Sentiment')

        return Response({"sentiment": sentiment}, status=status.HTTP_200_OK)
