from django.conf.urls import url
from .views import StudentView, StudentDelView, StudentUpdateView, StudentAddView


urlpatterns = [
    url(r"^$", StudentView.as_view(), name="student"),
    url(r"^create$", StudentAddView.as_view(), name="create"),
    url(r"^update$", StudentUpdateView.as_view(), name="update"),
    url(r"^delete$", StudentDelView.as_view(), name="delete")
]
