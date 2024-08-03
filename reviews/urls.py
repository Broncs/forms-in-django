from django.urls import path
from . import views
urlpatterns =[
    path("",views.ReviewView.as_view()),
    path("thank-you",views.Thankyou.as_view()),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>",views.ReviewDetailView.as_view(), name="single-review"),
    
]