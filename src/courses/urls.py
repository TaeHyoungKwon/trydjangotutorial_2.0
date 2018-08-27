from django.urls import path
from .views import (
    CourseView,
    CourseListView
)

app_name = 'courses'
urlpatterns = [
    #path('', CourseView.as_view(template_name='pages/contact.html'),name='courses-list')
    #path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('', CourseListView.as_view(), name='courses-list')
]