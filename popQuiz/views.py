from django.shortcuts import render

# Create your views here.
from .models import User
from .serializers import AccountSerialize


# Create your views here.
@api_view()
def list_account(request):
    accounts = Account.objects.all()
    serializer = AccountSerialize(accounts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
