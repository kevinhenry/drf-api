from django.urls import path
from .views import PlogList, PlogDetail

urlpatterns = [
    path('', PlogList.as_view(), name='post_list'),
    path('<int:pk>/', PlogDetail.as_view(), name='post_detail')
]