from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from . import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
      
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})



    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            is_single = serializer.validated_data.get('is_single')

            if is_single:
                 message = f'Hello {name} you are {age} old and still single'
            else:
                 message = f'Hello {name} you are {age} old and not single'
            return Response({'message':message
            })
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})




# VIEWSETS

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    
    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            is_single = serializer.validated_data.get('is_single')

            if is_single:
                 message = f'Hello {name} you are {age} old and still single'
            else:
                 message = f'Hello {name} you are {age} old and not single'
            return Response({'message':message
            })
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    
    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


        




# class ListCreateProducts(generics.ListCreateAPIView):
#   queryset = models.InsertOrUpdateProductDetails.objects.all().order_by('-discount')
#   serializer_class = serializers.InsertOrUpdateProductDetailsSerializer


# class ListAPIView(generics.ListAPIView):
#   serializer_class = serializers.InsertOrUpdateProductDetailsSerializer
#   filter_backends= [SearchFilter, OrderingFilter]
#   search_fields = ['cat_id_id',]
#   q = models.InsertOrUpdateCategory.objects.all()
  
#   def get_queryset(self, *args, **kwargs):
#     # queryset_list = super(ListAPIView, self).get_queryset(*args, **kwargs)
#     # q = models.InsertOrUpdateProductDetails.objects.get(cat_id=self.request.cat_id)
#     queryset_list = models.InsertOrUpdateProductDetails.objects.order_by('-discount')
#     #filter(user=self.request.user)

#     query = self.request.GET.get("q")
#     if query:
#        queryset_list = queryset_list.filter(
#         Q(category__icontains=query)
#       ).order_by('-discount')
#     return queryset_list

# class ListCreateCategorys(generics.ListCreateAPIView):
#   queryset = models.InsertOrUpdateCategory.objects.all()
#   serializer_class = serializers.InsertOrUpdateCategorySerializer

# class ListCreateShops(generics.ListCreateAPIView):
#   queryset = models.InsertOrUpdateShop.objects.all()
#   serializer_class = serializers.InsertOrUpdateShopSerializer




# class RetriveUpdateDestroyProducts(generics.RetrieveDestroyAPIView):
#   # permission_classes = (permissions.IsAuthenticated,)
#   queryset = models.InsertOrUpdateProductDetails.objects.all()
#   serializer_class = serializers.InsertOrUpdateProductDetailsSerializer
 
# class RetriveUpdateDestroyCategorys(generics.RetrieveDestroyAPIView):
#   # permission_classes = (permissions.IsAuthenticated,)
#   queryset = models.InsertOrUpdateCategory.objects.all()
#   serializer_class = serializers.InsertOrUpdateCategorySerializer
# class RetriveUpdateDestroyShops(generics.RetrieveDestroyAPIView):
#   # permission_classes = (permissions.IsAuthenticated,)
#   queryset = models.InsertOrUpdateShop.objects.all()
#   serializer_class = serializers.InsertOrUpdateShopSerializer









# class ListCreateProducts(APIView):
#   def get(self, request, format=None):
#     products = models.InsertOrUpdateProductDetails.objects.all()
#     serializer = serializers.InsertOrUpdateProductDetailsSerializer(products, many=True)
#     return Response(serializer.data)

#   def post(self, request, format=None):
#     serializer = serializers.InsertOrUpdateProductDetailsSerializer(data=request.data, many=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ListCreateCategorys(APIView):
#   def get(self, request, format=None):
#     products = models.InsertOrUpdateCategory.objects.all()
#     serializer = serializers.InsertOrUpdateCategorySerializer(products, many=True)
#     return Response(serializer.data)

#   def post(self, request, format=None):
#     serializer = serializers.InsertOrUpdateCategorySerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

  


# class ListCreateShops(APIView):
#   def get(self, request, format=None):
#     products = models.InsertOrUpdateShop.objects.all()
#     serializer = serializers.InsertOrUpdateShopSerializer(products, many=True)
#     return Response(serializer.data)

#   def post(self, request, format=None):
#     serializer = serializers.InsertOrUpdateShopSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)






# @api_view(['GET', 'POST'])
# def post_collection(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = {'text': request.DATA.get('the_post'), 'author': request.user.pk}
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)