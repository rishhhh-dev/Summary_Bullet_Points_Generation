from api_app.serializers import TextSerializer
import pytest

@pytest.fixture
def text_data():
    obj = {"input_text":"Some message",
           "summary":"""Some Summary""",
           "bullets":['bullet1','bullet2','bullet3']}
    return obj

#Test case for passing accurate data to serializer
@pytest.mark.django_db
def test_serializer(text_data):
    serializer = TextSerializer(data=text_data)

    assert serializer.is_valid() == True
    serializer.save()
    serializer_data = serializer.data

    assert serializer_data['input_text'] == text_data['input_text']
    assert serializer_data['summary'] == text_data['summary']
    assert serializer_data['bullets'] == text_data['bullets']


#Test case for no input text to serializer
def test_no_input_serializer(text_data):
    text_data['input_text'] = None
    serializer = TextSerializer(data=text_data)

    assert serializer.is_valid() == False
    assert text_data['input_text'] is None
    assert serializer.errors

#Test case for invalid field type in serializer
def test_no_list_serializer(text_data):
    text_data['bullets'] = {}
    serializer = TextSerializer(data=text_data)

    assert serializer.is_valid() == False
    assert text_data['bullets'] is not list()
    assert serializer.errors
