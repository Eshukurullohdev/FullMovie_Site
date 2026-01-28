from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("movie_inside/<int:movie_id>/", movi_inside, name="movie_inside"),
    path("aloqa/", aloqa, name="aloqa"),
    path("qoida/", qoida, name="qoida"),
    path("premyera/", premyera, name="premyera"),
    path("ish/", work, name="ish"),
    path("ish_second/", work_second, name="second")
]


# int === raqam
# id = 1
# 1 == int

# type_hint ==== 