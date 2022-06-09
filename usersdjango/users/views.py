from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProductDisplay
from .serializers import ProductDisplaySerializer

@api_view(["GET"])
def get_products(request):

    all_products = ProductDisplay.objects.all()
    # deserialize the models into browser understandable data format.
    serializers = ProductDisplaySerializer(all_products,  many=True)
    return Response(serializers.data)


@api_view(["POST"])
def post_likes(request, id=None): 
    product_id = id 
    print(f"product id{product_id} is been liked")
    return Response("success")
