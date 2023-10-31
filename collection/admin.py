from django.contrib import admin

from collection.models import Course
from collection.models import Lesson

admin.site.register(Course)
admin.site.register(Lesson)
