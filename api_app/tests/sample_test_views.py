from api_app.views import *
from api_app.serializers import TextSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import MagicMock,patch
import re
import pytest

#Fixture for creating a user.
@pytest.fixture
@pytest.mark.django_db
def create_user():
    user = User.objects.create_user(username="testuser", password="testpass")
    refresh = RefreshToken.for_user(user)
    return {"user":user,"access_token":str(refresh.access_token)}

#Fixture for creating a api_client.
@pytest.fixture
def api_client(create_user):
    client=APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {create_user['access_token']}")
    return client

#Mock fixture response for Groq api
@pytest.fixture
def mock_groq_response():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="This is a summary."))]
    return mock_response


#Test successful summary generation.
@pytest.mark.django_db
@patch("api_app.views.client.chat.completions.create")
def test_generate_summary_success(mock_groq, api_client, mock_groq_response):
    mock_groq.return_value = mock_groq_response()

    response = api_client.post("/generate-summary/", {"message": "Test content"})
    
    assert response.status_code == status.HTTP_200_OK


#Test when 'message' key is missing.
@pytest.mark.django_db
@patch("api_app.views.client.chat.completions.create")
def test_generate_summary_missing_message(mock_groq, api_client):
    response = api_client.post("/generate-summary/", {})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


#Test when 'message' is empty.
@pytest.mark.django_db
@patch("api_app.views.client.chat.completions.create")
def test_generate_summary_empty_message(mock_groq, api_client):
    response = api_client.post("/generate-summary/", {"message": ""})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


#Test Groq API failure handling.
@pytest.mark.django_db
@patch("api_app.views.client.chat.completions.create", side_effect=Exception("API Error"))
def test_generate_summary_groq_failure(mock_groq, api_client):
    response = api_client.post("/generate-summary/", {"message": "Test content"})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "API Error" in str(response.data)


#Test bullet points generation.
@pytest.mark.django_db
@patch("api_app.views.client.chat.completions.create")
def test_generate_bullet_points_success(mock_groq, api_client, mock_groq_response):
    mock_groq.return_value = mock_groq_response()
    mock_groq.return_value.choices[0].message.content = "* Point 1\n* Point 2"

    response = api_client.post("/generate-bullet-points/", {"message": "Test content"})
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == ["Point 1", "Point 2"]


#Test when the bullet points don't match expected format.
@pytest.mark.django_db
@patch("api_app.views.client.chat.completions.create")
def test_generate_bullet_points_invalid_format(mock_groq, api_client , mock_groq_response):
    mock_groq.return_value = mock_groq_response()
    mock_groq.return_value.choices[0].message.content = "This is just a text."

    response = api_client.post("/generate-bullet-points/", {"message": "Test content"})
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


#Test that unauthenticated users cannot access the API.
@pytest.mark.django_db
def test_generate_summary_unauthenticated():
    client = APIClient()
    response = client.post("/generate-summary/", {"message": "Test content"})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
