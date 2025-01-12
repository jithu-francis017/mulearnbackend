from django.urls import path

from . import profile_view

urlpatterns = [
    path('user-profile/', profile_view.UserProfileAPI.as_view()),
    path('user-profile/<str:muid>/', profile_view.UserProfileAPI.as_view()),
    # path('edit-user-profile/', profile_view.UserProfileAPI.as_view()),
    path('user-log/', profile_view.UserLogAPI.as_view()),
    path('user-log/<str:muid>/', profile_view.UserLogAPI.as_view()),
    path('share-user-profile/', profile_view.ShareUserProfileAPI.as_view()),
    path('rank/<str:muid>/', profile_view.UserRankAPI.as_view()),
    path('get-user-levels/', profile_view.UserLevelsAPI.as_view()),
    path('get-user-levels/<str:muid>/', profile_view.UserLevelsAPI.as_view()),
]
