
from django.urls import path
from .views import (
    home_page,about_page,
    CreatePage,detail_page,delete_page,
    update_page,contact_page)

# from .views import detail_page,update_page,home_page,about_page,create_page,delete_page

urlpatterns = [
    path("",home_page.as_view(),name="home_page"),
    path("about/",about_page,name="about_page"),
    path("create/",CreatePage.as_view(template_name="create.html"),name="create_page"),
    path("<int:id>/",detail_page,name="detail_page"),
    path("<int:pk>/delete/",delete_page.as_view(template_name="delete.html"),name="delete_page"),
    path("<int:pk>/update/",update_page.as_view(template_name="update.html"),name="update_page"),
    path("contact/",contact_page,name="contact_page"),

   # path("<int:id>/delete/",delete_page,name="delete_page"),
    # path("<int:id>/update/",update_page,name="update_page"),

]
