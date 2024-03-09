from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,   )
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

import forum.views
import authentication.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', forum.views.home, name='home'),
    path('account/', forum.views.account, name='account'),
   
    #Password

    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/changePassword.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/changePassworddone.html'),
        name='password_change_done'
         ),
    path('password-reset/', PasswordResetView.as_view(
        template_name='authentication/resetPassword.html',
     ), name='reset_password'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='authentication/resetPassworddone.html',
        ), name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authentication/resetPasswordconfirm.html',
    ), name='password_reset_confirm'),

    path('password-reset/complete/', PasswordResetDoneView.as_view(
        template_name='authentication/resetPasswordcomplete.html',
    ), name='password_reset_complete'),
    #profile
     # Profile picture
    path('change-profile/', authentication.views.profile, name='change-profile'),

    #all sections
    path('section/IT/', forum.views.IT, name='IT-section'),    
    path('section/MATH/', forum.views.MATH, name='MATH-section'),
    path('section/PHYSICS/', forum.views.PHYSICS, name='PHYS-section'),
    path('section/MEDECINE/', forum.views.MEDECINE, name='MEDECINE-section'),
    path('section/SOCIOLOGY/', forum.views.SOCIOLOGY, name='SOCIOLOGY-section'),
    path('section/miscellaneous_topics/', forum.views.miscellaneous_topics, name='miscellaneous-topics'),
    
    #create a new forum topic   
    path('new-topic/', forum.views.new_ftopic, name='create-ftopic'),
    path('topic/<slug>/', forum.views.topic_detail, name='topic-detail'),
    #path('follow-users/', forum.views.follow_users, name='follow_users')
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

