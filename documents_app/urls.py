from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('list/', views.list_documents, name='list_documents'),
    path('delete/<int:doc_id>/', views.delete_documents, name='delete_document'),
    path('download/<int:doc_id>/', views.download_document, name='download_document'),
]