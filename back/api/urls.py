from django.urls import path, include
from .views import ProfessorDetail, listar_professores
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('professores/', listar_professores),  
    path('professores/<int:pk>/', ProfessorDetail.as_view(), name='professor-detail'),
]