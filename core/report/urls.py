from django.urls import path
from .views import create_report, success_view, edit_report, delete_report, report_list, like_report, add_comment, map_view

app_name = 'report'

urlpatterns = [
    path('', create_report, name='create_report'),
    path('report_list', report_list, name='report_list'),
    path('success/', success_view, name='success'),
    path('edit/<int:report_id>/', edit_report, name='edit_report'),
    path('delete/<int:report_id>/', delete_report, name='delete_report'),
    path('like/<int:report_id>/', like_report, name='like_report'),
    path('comment/<int:report_id>/', add_comment, name='add_comment'),
    path('map/', map_view, name='map'),
]
