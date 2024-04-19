from django.urls import path, include
from Planet_Discoverers.users import views
from Planet_Discoverers.users.views import UserLoginView, UserRegisterView, details_user, UserEditView, delete_user, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
    path('<int:pk>/', include([
        path('', details_user, name='details_user'),
        path('edit/', UserEditView.as_view(), name='edit_user'),
        path('delete/', delete_user, name='delete_user'),
    ])),
)
