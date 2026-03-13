from django.urls import path
from . import views

urlpatterns = [

    path('recipes/', views.get_recipes),
    path('add/', views.add_recipe),
    path('download/', views.download_recipes),
    path('import/', views.import_recipes),

]