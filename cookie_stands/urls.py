from django.urls import path
from .views import CookieStandlist, CookieStandDetail

urlpatterns = [
    path("", CookieStandlist.as_view(), name="CookieStand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="CookieStand_detail"),
]
