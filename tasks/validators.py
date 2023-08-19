from rest_framework.validators import UniqueValidator
from .models import *

unique_title = UniqueValidator(Task.objects.all())