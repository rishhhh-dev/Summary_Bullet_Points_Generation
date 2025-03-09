from api_app.models import Text
from django.db.utils import IntegrityError , ProgrammingError
import pytest

#Test case for accurate data
@pytest.mark.django_db
def test_model_data():
    obj = {"input_text":"Some message","summary":"""Some Summary""","bullets":['bullet1','bullet2','bullet3']}
    instance = Text.objects.create(**obj)

    assert instance.input_text == obj['input_text']
    assert instance.summary == obj['summary']
    assert instance.bullets == obj['bullets']


#Test case for storing only summary
@pytest.mark.django_db
def test_summary_data():
    obj = {"input_text":"Some message",
           "summary":"""Some Summary""",
           "bullets":[]}
    instance = Text.objects.create(**obj)

    assert instance.input_text == obj['input_text']
    assert instance.summary == obj['summary']
    assert instance.bullets == list()


#Test case for storing only bullet points
@pytest.mark.django_db
def test_bullet_data():
    obj = {"input_text":"Some message",
           "summary":"",
           "bullets":['bullet1','bullet2','bullet3']}
    instance = Text.objects.create(**obj)

    assert instance.input_text == obj['input_text']
    assert instance.summary == ""
    assert instance.bullets == obj['bullets']


#Test case for no input message
@pytest.mark.django_db
def test_no_input_data():
    obj = {"input_text":None,
           "summary":"",
           "bullets":[]}
    with pytest.raises(IntegrityError):
        Text.objects.create(**obj)


#Test case for invalid field type
@pytest.mark.django_db
def test_invalid_bullets_data():
    obj = {"input_text":"Some message",
           "summary":"",
           "bullets":{}}
    with pytest.raises(ProgrammingError):
        Text.objects.create(**obj)