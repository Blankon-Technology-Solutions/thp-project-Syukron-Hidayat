from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path, include
from allauth.socialaccount.views import signup
from authentication import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todos', viewset=views.TodoViewSet)

urlpatterns = [
    path('login/', views.Login, name = 'Login'),
    path('register/', views.Register, name = 'Register'),
    path('home/', views.Home, name = 'Home'),
    path('Logout',views.Logout, name = 'Logout'),
    path("auth/register/", RegisterView.as_view(), name="rest_register"),
    path("auth/login/", LoginView.as_view(), name="rest_login"),
    path("auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path("auth/user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("auth/signup/", signup, name="socialaccount_signup"),
    path('', include(router.urls), name="todos"),
]