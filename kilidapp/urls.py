from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('usermgmt/', views.usermgmt, name='usermgmt'),
    path('login/', views.my_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.my_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_house/', views.add_house, name='add_house'),
    path('edit_house/<int:pk>/', views.edit_house, name='edit_house'),
    path('delete_house/<int:pk>/', views.delete_house, name='delete_house'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('promote_user/<int:pk>/', views.promote_user, name='promote_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('promote_user_ajax/<int:pk>/', views.promote_user_ajax, name='promote_user_ajax'),
    path('delete_user_ajax/<int:pk>/', views.delete_user_ajax, name='delete_user_ajax'),
    path('delete_house_ajax/<int:pk>/', views.delete_house_ajax, name='delete_house_ajax'),
    path('all_houses/', views.all_houses, name='all_houses'),
    path('bookmark_ajax/<int:pk>/', views.bookmark_ajax, name='bookmark_ajax'),
    path('unbookmark_ajax/<int:pk>/', views.unbookmark_ajax, name='unbookmark_ajax'),
    path('my_bookmarks/', views.my_bookmarks, name='my_bookmarks'),
    path('load_all_ajax/', views.load_all_ajax, name='load_all_ajax'),
    path('house/<int:pk>', views.house, name='house'),
    path('search/', views.search, name='search'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')

path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='kilidapp/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='kilidapp/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='kilidapp/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='kilidapp/password_reset_complete.html'
         ),
         name='password_reset_complete')

]