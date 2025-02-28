# Create a router and register our viewsets with it.
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views
from api.DefaultRouterWithSimpleViews import DefaultRouterWithSimpleViews

router = DefaultRouterWithSimpleViews()
router.register(r'report', views.ReportViewSet)
router.register(r'report-form', views.ReportFormTree, basename='report-form')
router.register(r'login', views.login_, 'login')
router.register(r'logout', views.logout_view, 'logout')
router.register(r'has-access', views.has_access, 'has-access')
router.register(r'csrf', views.csrf, 'csrf')
router.register(r'translation', views.TranslationViewSet, 'translation')
router.register(r'votes', views.VoteViewSetReport, 'votes')
router.register(r'notifications', views.NotificationsViewSet, 'notifications')
router.register(r'user', views.UserViewSet, 'user')  # create user
router.register(r'user-del', views.UserDeleteViewSet, 'user-del')  # destroy user
router.register(r'get-user', views.get_user, 'get-user')  # get infos on user
router.register(r'get-user-stat', views.get_user_stat, 'get-user-stat')  # get stats on user
router.register(r'patch-user', views.UserUpdateViewSet, 'patch-user')  # patch infos - first_name, last_name, alias.
router.register(r'key-validation', views.KeyValidationView, 'key-validation')
router.register(r'reset-password-send-mail', views.PasswordForgotRequestView, 'reset-password-send-mail')
router.register(r'reset-password', views.RestPasswordView, 'reset-password')
router.register(r'report-image', views.ReportImageView, 'report-image')
router.register(r'authorized-email', views.AuthorizedMailViewSet, 'authorized-email')
router.register(r'report-annotation', views.ReportAnnotationViewSet, 'reportannotation')
router.register(r'area', views.AreaViewSet, 'area')
router.register(r'document', views.DocumentViewSet, 'document')
router.register(r'report-annotation-comment', views.ReportAnnotationCommentViewSet, 'reportannotationcomment')
router.register(r'report-geojson', views.ReportGeoJsonViewSet, 'report-geojson')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]