from django.urls import path, include
from .views import UserLoginView, UserRegisterView
# from django_email_verification import urls as email_urls

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('email/', include(email_urls)),
    # path('email/<str:token>/', confirm),
    

]
