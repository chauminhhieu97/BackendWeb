from .api import LeadViewSet, UserViewSet, MovieViewSet, RatingViewSet, TagViewSet, LinkViewSet
from rest_framework import routers
# from .api import LeadViewSet, UserViewSet, MovieViewSet

# Manh
from django.conf.urls import url, include
from .views import RegisterAPI, LoginAPI
from knox import views as know_views


router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/user', UserViewSet, 'user')
router.register('api/movie', MovieViewSet, 'movie')


# Test
router.register('api/link', LinkViewSet, 'link')
router.register('api/tag', TagViewSet, 'tag')
router.register('api/rating', RatingViewSet, 'rating')

# Manh

urlpatterns = [
    url(r'^api/auth', include('knox.urls')),
    url(r'^api/login', LoginAPI.as_view()),
    url(r'^api/register', RegisterAPI.as_view()),

]
