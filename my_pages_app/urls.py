from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('home', views.home, name='homepage'),
    path('whoweare/', views.who_we_are, name='whoweare'),
    path('programs/', views.programs, name='programs'),
    path('makeanimpact/', views.make_an_impact, name='impact'),
    path('getintouch/', views.get_in_touch, name='contact'),
    path('donate/', views.donate, name='donate'),
    # path('partnerwithus/', views.partner_view, name='partner_with_us'),
    path("success/", views.success, name="success"),
    path("communitysupport/", views.community_support, name='community_support'),
    path("mentoringandcounselling/", views.mentoring_counselling, name='mentoring_counselling'),
    path("placementandreintegration/", views.placement_reintegration, name='placement_reintegration'),
    path("mobilelearning/", views.mobile_learning, name='mobile_learning'),
    path("gallery/", views.gallery, name='gallery'),
    

]