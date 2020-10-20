from django.urls import path, include
from core.views import frontpage, signup, logout_user, login_user

app_name = "core"

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('signup', signup, name="signup"),
    path('logout', logout_user, name="logout"),
    path('login_page', login_user, name="login"),
]
