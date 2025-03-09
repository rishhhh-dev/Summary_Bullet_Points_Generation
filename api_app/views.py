from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TextSerializer
from .models import Text
from groq import Groq
import os
import re


# Create your views here.

client = Groq(
    api_key = os.environ.get("GROQ_API_KEY")
)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_summary(request):
    try:
        original_txt = request.data.get('message')
        if original_txt:
            chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{original_txt} without bullet points",
                }
            ],
            model="llama-3.3-70b-versatile",
            )
            result = chat_completion.choices[0].message.content
            obj = {'input_text':original_txt,'summary':result}
            serializer = TextSerializer(data=obj)

            if serializer.is_valid():
                serializer.save()
                return Response(obj['summary'])
            else:
                return Response("Invalid data")
        else:
            return Response(status=400)
        
    except Exception as e:
        return Response({"error":str(e)},status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_bullet_points(request):
    try:
        original_txt = request.data['message']
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{original_txt} with bullet points",
            }
        ],
        model="llama-3.3-70b-versatile",
        )
        result = chat_completion.choices[0].message.content
        regex_pattern = r"^\*{0,1} (.+)$"
        extracted_list = re.findall(regex_pattern,result,re.MULTILINE)

        obj = {'input_text':original_txt,'bullets':extracted_list}
        serializer = TextSerializer(data=obj)

        if serializer.is_valid():
            serializer.save()
            return Response(extracted_list)
        
    except Exception as e:
        return Response({"error":str(e)},status=400)