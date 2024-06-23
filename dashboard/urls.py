from django.urls import path, include
from dashboard import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path("", views.dashboard_rz, name="dashboard"),
    path('aktualnosci/<int:pk>/', views.aktualnosci_details, name='aktualnosci_details'),
    # path("aktualnosci", views.aktualnosci, name="aktualnosci"),
    path("czlonkowie", views.czlonkowie_rz, name="czlonkowie"),
    path("czlonkowie_details/<int:pk>", views.czlonkowie_rz_details, name="czlonkowie_details"),
    path("ckeditor", include("ckeditor_uploader.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
