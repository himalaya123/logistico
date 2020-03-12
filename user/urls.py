
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('services/',views.services ,name='services'),
    path('about/',views.about ,name='about'),
    path('service-details/',views.service_details ,name='service-details'),
    path('image-gallery/',views.image_gallery ,name='image-gallery'),
    path('blog/',views.blog ,name='blog'),
    path('single-blog/',views.single_blog ,name='single-blog'),
    path('contact/',views.contact ,name='contact'),
]