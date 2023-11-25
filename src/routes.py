from django.urls import path,include

urlpatterns = [
    path('book/', include("src.book.urls")),
    path('/', VIEW.as_view(), name=''),
]