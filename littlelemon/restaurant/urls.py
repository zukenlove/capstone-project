from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewset)
router.register(r'users', views.UserViewset)
router.register(r'tables',views.BookingViewset)



urlpatterns = [
    # path('home/', views.homeView, name='home'),
    # path('restaurant/',views.index, name="index"),
    # path('menu/',views.menuView, name ='menu'),
    path('restaurant/', include(router.urls)),
]