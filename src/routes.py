from django.urls import path,include

urlpatterns = [
    path('book/', include("src.book.urls")),
    path('user/', include("src.user.urls")),
]