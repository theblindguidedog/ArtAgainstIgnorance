from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('music', views.music, name="music"),
    path('video', views.video, name="video"),
    path('shop', views.shop, name="shop"),
    path('shop_details', views.shop_details, name="shop_details"),
    path('shop_details_liamgervaise', views.shop_details_liamgervaise, name="shop_details_liamgervaise"),
    path('news', views.news, name="news"),
    path('news_details', views.news_details, name="news_details"),
    path('news_details_utopians', views.news_details_utopians, name="news_details_utopians"),
    path('artists', views.artists, name="artists"),
    path('contact', views.contact, name="contact"),
    path('test', views.test, name="test"),
    path('artist_details_briangervaise', views.artist_details_briangervaise, name="artist_details_briangervaise"),
    path('artist_details_zacharygervaise', views.artist_details_zacharygervaise, name="artist_details_zacharygervaise"),
    path('artist_details_darceygervaise', views.artist_details_darceygervaise, name="artist_details_darceygervaise"),
    path('artist_details_darceygervaise2', views.artist_details_darceygervaise2, name="artist_details_darceygervaise2"),
    path('artist_details_wally', views.artist_details_wally, name="artist_details_wally"),
    path('artist_details_johnno', views.artist_details_johnno, name="artist_details_johnno"),
    path('artist_details_ganna', views.artist_details_ganna, name="artist_details_ganna"),
    path('artist_details_ganna2', views.artist_details_ganna2, name="artist_details_ganna2"),
    path('artist_details_nerdyrodent', views.artist_details_nerdyrodent, name="artist_details_nerdyrodent"),
    path('artist_details_nerdyrodent2', views.artist_details_nerdyrodent2, name="artist_details_nerdyrodent2"),
    path('artist_details_blatantblatheist', views.artist_details_blatantblatheist, name="artist_details_blatantblatheist"),
    path('artist_details_blatantblatheist2', views.artist_details_blatantblatheist2, name="artist_details_blatantblatheist2"),
    
    
]
