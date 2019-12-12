from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api_v1.views import LogoutView, QuotesViewSet

router = routers.DefaultRouter()
router.register(r'quotes', QuotesViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
