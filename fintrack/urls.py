from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracker.views import CategoryViewSet, TransactionViewSet, RegisterView, MonthlyReportView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/reports/monthly/', MonthlyReportView.as_view(), name='monthly_report'),
    path('api/', include(router.urls)),
]
