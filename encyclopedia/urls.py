from django.urls import path

from . import views

"""
    Comments:
    -There's no need for a '/' at the beggining, but every URL has to end with '/'
    -Django tests each pattern in order, and if matches the view function associated will be called
"""

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('wiki/', views.main_page, name='main_page'),
    path('wiki/?/', views.search, name='wiki'),
    path('wiki/Main_Page/', views.index, name='index'),
    path('wiki/<str:page_name>/', views.display, name='display'),
    path('Create_New_Page/', views.new_page, name='new_page'),
    path('save_page/', views.save_page, name='save_page'),
    path('random_page/', views.random_page, name='random_page'),
    path('edit/<str:title>/', views.edit, name='edit'),
    path('edit_save/<str:page_name>/', views.edit_save, name='edit_save')

]
