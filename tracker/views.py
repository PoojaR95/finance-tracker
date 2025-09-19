from datetime import date
from calendar import monthrange
from django.db.models import Sum, Q
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer, RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "user created"}, status=status.HTTP_201_CREATED)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(Q(is_default=True) | Q(owner=self.request.user))
    def perform_create(self, serializer):
        serializer.save(is_default=False, owner=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MonthlyReportView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        month_str = request.query_params.get("month")
        if month_str:
            try:
                year, month = map(int, month_str.split("-"))
            except:
                return Response({"detail": "month must be YYYY-MM"}, status=400)
        else:
            today = date.today(); year, month = today.year, today.month

        start = date(year, month, 1)
        end = date(year, month, monthrange(year, month)[1])
        qs = Transaction.objects.filter(user=request.user, date__range=(start, end))

        totals = qs.values("type").annotate(total=Sum("amount"))
        income = sum(x["total"] for x in totals if x["type"]=="income")
        expense = sum(x["total"] for x in totals if x["type"]=="expense")
        net = float(income) - float(expense)

        return Response({
            "month": f"{year}-{month:02d}",
            "income": float(income),
            "expense": float(expense),
            "net_saving": net
        })
