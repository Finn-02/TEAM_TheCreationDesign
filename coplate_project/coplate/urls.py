from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("apply_club/", views.apply_club, name="apply_club"),
    path("apply_club_a/", views.apply_club_a, name="apply_club_a"),
    path("apply_activity/", views.apply_activity, name="apply_activity"),

    path("community/", views.community, name="community"),
    path("community/add/", views.add_community, name="add_community"),
    path('community/<int:post_id>/', views.community_detail, name='community_detail'),
    path("community_delete/<int:post_id>", views.community_delete, name='community_delete'),
    path("community_update/<int:post_id>", views.community_update, name='community_update'),

    path("adboard/", views.adboard, name="adboard"),
    path("adboard/add/", views.add_adboard, name="add_adboard"),
    path('adboard/<int:post_id>/', views.adboard_detail, name='adboard_detail'),
    path("adboard_delete/<int:post_id>", views.adboard_delete, name='adboard_delete'),
    path("adboard_update/<int:post_id>", views.adboard_update, name='adboard_update'),

    path("taxi/", views.taxi, name="taxi"),
    path("taxi/add/", views.add_taxi, name="add_taxi"),
    path('taxi/<int:post_id>/', views.taxi_detail, name='taxi_detail'),
    path("taxi_delete/<int:post_id>", views.taxi_delete, name='taxi_delete'),
    path("taxi_update/<int:post_id>", views.taxi_update, name='taxi_update'),
    
    path("notice/", views.notice, name="notice"),
    path("notice/add/", views.add_notice, name="add_notice"),
    path('notice/<int:post_id>/', views.post_detail, name='post_detail'),
    path("post_delete/<int:post_id>", views.post_delete, name='post_delete'),
    path("post_update/<int:post_id>", views.post_update, name='post_update'),
]