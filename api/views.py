from django.shortcuts import render
from django.http import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializer import productserializer,cartserializer,RegisterSerializer, UserSerializer
from .models import product,cart_product
from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework import status
from knox.auth import TokenAuthentication

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        # ... other routes ...
    ]
    return Response(routes)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_user_by_token(request):
    user = request.user
    if user.is_authenticated:
        # Serialize the user data as needed
        serialized_user = {
            'username': user.username,
            'email': user.email,
            # other user fields
        }
        return Response(serialized_user)
    else:
        return Response({'error': 'Authentication credentials were not provided.'})
    

    
@api_view(['GET'])
def getproducts(request):
    # data_transfer()
    products = product.objects.all()
    serializer = productserializer(products, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getproduct(request, x):
    product_instance = product.objects.get(id=x)
    serializer = productserializer(product_instance, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getcart_products(request):
    products = cart_product.objects.filter(user=request.user)
    serializer = cartserializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_api(request, format=None):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    print(user)
    login(request, user)
    knox_login_view = KnoxLoginView()
    response = knox_login_view.post(request, format=None)
    return response

# The global variable can be accessed outside the function

@api_view(['PUT'])
# @csrf_exempt
def update_product(request, x):
 
    data = request.data
    # print(data)
    product_instance = product.objects.get(id=x)
    # print(product_instance)
    serializer = productserializer(instance=product_instance, data=data)

    if serializer.is_valid():
        # product_instance.incart=serializer.data.get('incart')
        serializer.save()

    return Response(serializer.data)





@api_view(['PUT'])
#

# @csrf_exempt
def update_cart_product(request, x):
    data = request.data
    # print(data)
    cart_product_instance = cart_product.objects.get(id=x,user=request.user)
    # print(product_instance)
    serializer = cartserializer(instance=cart_product_instance, data=data)

    if serializer.is_valid():
        # product_instance.incart=serializer.data.get('incart')
        serializer.save()

    return Response(serializer.data)




def check(data,user):
    obj_id=data.get('p_key')
    obj_user=user
    # print(obj_id)
    current_obj=cart_product.objects.all()
    a=True
    for cu_obj in current_obj:
        if(obj_id==cu_obj.p_key and obj_user==cu_obj.user):
                # print(cu_obj.id)
                a=False
                break
    return a
    


@api_view(['DELETE'])
#

def deleteitem(request,x):
    item=cart_product.objects.get(id=x,user=request.user)
    item.delete()
    return Response({'message':'product removed from cart'})


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_api(request):
    print(request.data)
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    # token = Token.objects.create(user=user)
    
    return Response({
        "user": UserSerializer(user, context={'request': request}).data,
        "token": AuthToken.objects.create(user)[1]
    })


# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def login_api(request, format=None):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     login(request, user)
    
#     # Create a KnoxLoginView instance and call the post method
#     knox_login_view = KnoxLoginView()
#     response = knox_login_view.post(request, format=None)
    
#     return Response({
#         'token': response.data['token'],
#         'user': {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#         }
#     })

@api_view(['POST'])
#
def addtocart(request):
   data=request.data
#    print(data)
   if(check(data,request.user)):

     p_key=data.get('p_key')
     name=data.get('name')
     description=data.get('description')
     price=data.get('price')
     discount=data.get('discount')
     img=data.get('img')
     cart_item=cart_product.objects.create(  
      user=request.user,
      name=name,
      price=price,
      discount=discount,
      img=img,
      p_key= p_key

    )
     serializer=productserializer(cart_item)
     return Response(serializer.data)
   else:
       return Response({'message': 'Item already exists in the cart'})