from base.views import user_views
from django.urls import path

urlpatterns = [
    
    path('api/', user_views.getRoutes, name='routes'),
    path('login/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', user_views.registerUser, name='register'),
    path('profile/', user_views.getUserProfile, name='users-profile'),
    path('profile/update/', user_views.updateUserProfile, name='users-profile-update'),
    path('', user_views.getUsers, name='users'),
    path('<str:pk>/', user_views.getUsersById, name='users-by-id'),
    path('update/<str:pk>/', user_views.updateUser, name='user-update'),
    path('delete/<str:pk>/', user_views.deleteUser, name='user-delete'),

]
