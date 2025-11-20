from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (CreatePostView,ListPostView, RegisterView,UserLoginView,UserLogoutView,DeletePostView,ProfileDetailView,
                    UserUpdateView,CreateCommentView,DetailPostView,BaseView,UpdatePostView,MassageListView,CreateMassageView,DetailMassageView
)

urlpatterns = [
    path("home/",BaseView.as_view(),name="basee"),
    path("listpost/",ListPostView.as_view(),name="listpost"),
    path("createpost/",CreatePostView.as_view(),name="createpost"),
    path("<int:pk>/deletepost/",DeletePostView.as_view(),name="deletepost"),
    path("<int:pk>/updatepost/",UpdatePostView.as_view(),name="updatepost"),
    path("<int:pk>/postdetail/",DetailPostView.as_view(),name="postdetail"),
    path("<int:pk>/profile/",ProfileDetailView.as_view(),name="profile"),
    path("<int:pk>/createcoment/",CreateCommentView.as_view(),name="createcoment"),
    path("massagelist/",MassageListView.as_view(),name="massagelist"),
    path("createmassage/",CreateMassageView.as_view(),name="createmassage"),
    path("<int:pk>/detailmassage/",DetailMassageView.as_view(),name="detailmassage"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("logout/",UserLogoutView.as_view(),name="logout"),
    path("register/",RegisterView.as_view(),name="register"),
    path("<int:pk>/usup/",UserUpdateView.as_view(),name="usup")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

