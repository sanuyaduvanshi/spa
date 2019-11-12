from django.urls import path
from beautyapp import views

urlpatterns = [
    path('about/',views.about,name='about'),
    path('service/',views.services,name='service'),
    path('gallery/',views.spa_treatment,name='spa_treatment'),
    # path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),

]
