from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #HOMEPAGE
    path("class_page/", views.class_page, name="class_page"), ##DONT KNOW WHAT THIS IS FOR
    path("classes/", views.ClassListView.as_view(), name="classes"),
    path("class/<int:pk>", views.ClassDetailView.as_view(), name="class-detail"),
    path("profile", views.profile, name="profile"), #HOMEPAGE
    path("search_results", views.SearchResults.as_view(), name="search_results"),
    path("submissions_page", views.submissions_page, name="submissions_page"),
    path("advanced_search", views.advanced_search, name="advanced_search"),
]
