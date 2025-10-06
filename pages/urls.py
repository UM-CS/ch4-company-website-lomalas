from django.urls import path
from .views import home_page_view, AboutPageView, ProductsPageView

urlpatterns = [
    path("", home_page_view, name="home"),          # homepage route
    path("about/", AboutPageView.as_view(), name="about"),  # class-based view
    path("products/", ProductsPageView.as_view(), name="products"),
]
