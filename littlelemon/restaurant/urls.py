from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewset)
router.register(r'users', views.UserViewset)
router.register(r'bookings', views.BookingViewset)



urlpatterns = [
    path('restaurant/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token ),
]