from django.urls import path
from .import views

urlpatterns=[
    path('',views.main),
    path('contest/',views.contest),
    path('problemset/',views.problems_list),
    path('problemset/description/<int:id>',views.problem_details)
]