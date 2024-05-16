from django.urls import path, include
from Planet_Discoverers.users.views import (CustomLoginView, UserRegisterView, details_user, UserEditView,
                                            delete_user, UserLogoutView, email_greeting)

urlpatterns = (
    path('login/', CustomLoginView.as_view(), name='login_user'),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('logout/', UserLogoutView.as_view(), name='logout_user'),
    path('email_greeting/', email_greeting, name='email_greeting'),
    path('<int:pk>/', include([
        path('', details_user, name='details_user'),
        path('edit/', UserEditView.as_view(), name='edit_user'),
        path('delete/', delete_user, name='delete_user'),
    ])),
)
