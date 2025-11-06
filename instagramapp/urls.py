from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import CreatePostView,ListPostView, RegisterView,UserLoginView,UserLogoutView,DeletePostView,ProfileDetailView,UserUpdateView

urlpatterns = [
    path("listpost/",ListPostView.as_view(),name="listpost"),
    path("createpost/",CreatePostView.as_view(),name="createpost"),
    path("<int:pk>/deletepost/",DeletePostView.as_view(),name="deletepost"),
    path("<int:pk>/profile/",ProfileDetailView.as_view(),name="profile"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("logout/",UserLogoutView.as_view(),name="logout"),
    path("register/",RegisterView.as_view(),name="register"),
    path("<int:pk>/usup/",UserUpdateView.as_view(),name="usup")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

