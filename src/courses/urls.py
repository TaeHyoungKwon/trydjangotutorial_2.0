from django.urls import path
from .views import (
    CourseView
)

app_name = 'courses'
urlpatterns = [
    #path('', CourseView.as_view(template_name='pages/contact.html'),name='courses-list')
    path('<int:id>/', CourseView.as_view(), name='courses-detail')
]