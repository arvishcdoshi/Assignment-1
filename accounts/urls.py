from accounts import views
from django.urls import path

urlpatterns = [

path('hello/',views.HelloView.as_view(),name='hello'),
#path('api/token/', jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
#path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),

]
