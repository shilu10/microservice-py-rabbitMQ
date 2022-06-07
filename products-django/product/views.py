from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from .models import User
import random

@api_view(["GET"])
def list(request): 
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create(request): 
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# id is the route parameter.
@api_view(["GET"])
def retrieve(request, id=None):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data) 


@api_view(["DELETE"])
def delete(request, id=None): 
    product = Product.objects.get(id=id)
    product.delete()
    return Response({
        "response":"deletedi"
    })


@api_view(["PUT"])
def update(request, id=None):
    product = Product.objects.get(id=id)
    # instance will hold the current data, data holds the data from the user, so
    # it will update the instance data withe the data.
    serializer = ProductSerializer(instance=product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

# users api 
@api_view(["GET"])
def get_users(self): 
    users = User.objects.all()
    print(users, "users")
    user = random.choice(users)
    return Response(
        {
            "id": user.id
        }
    )


   