from django.urls import path
from . import views


urlpatterns = [
   path('user',  views.UserApiView.as_view() ),
   path('user/<int:id>',  views.GetUserFromId.as_view() )
]
