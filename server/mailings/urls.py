from rest_framework.routers import DefaultRouter

from mailings.views import MailingsViewSet

router = DefaultRouter()

router.register('', MailingsViewSet, basename='mailings_list_retrieve')

urlpatterns = [

] + router.get_urls()
