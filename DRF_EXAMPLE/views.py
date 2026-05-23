from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Project, Task
from .serializers import ProductModelSerializer, ProductSerializer, ProjectModelSerializer, TaskModelSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    def list(self, request, *args, **kwargs):
        return supper().list(request, *args, **kwargs)
    
class ProductAPIView(APIView):
    def get(self, request: Request):
        try:
            products = Product.objects.all()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Products retrieved successfully',
                'data': ProductModelSerializer(products, many=True).data
            }, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Product not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductModelSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(instance=product, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    "status": status.HTTP_200_OK,
                    "message": "Product updated successfully",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Invalid data",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "Product not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
class ProductListView(APIView):
    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "Product created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid data",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request: Request):
        products = None
        orders = request.query_params.get('orders', None)
        if orders:
            products = Product.objects.all().order_by('-price' if 'asc' in orders[0] else 'price')
        else:
            products = Product.objects.all()
        ser_products = ProductSerializer(products, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "Products retrieved successfully",
            "data": ser_products.data
        }, status=status.HTTP_200_OK)
    

class ExampleAPIView(APIView):
    def get(sels, request: Request):
        return Response({
            'username':"jack_nicolas",
            "email":"example@gmail.com"
        }, status=status.HTTP_200_OK)

    def post(self, request: Request):
        r = Response()

        data = {
            'status': status.HTTP_201_CREATED,
            'message': "Data received successfully",
            'data': request.data
        }

        r.data = data
        r.headers['Content-Type'] = request.content_type
        if request.data:
            body = request.data
            if body.get('name', None):
                r.headers['name'] = body['name']
        r.status_code = status.HTTP_201_CREATED
        return r    
    









class ProjectAPIView(APIView):
    def get(self, request: Request, id=None):
        if id:
            try:
                project = Project.objects.prefetch_related('members').get(id=id)
                return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': "Project retrieved successfully",
                    'data': ProjectModelSerializer(project).data
                }, status=status.HTTP_200_OK)
            
            except ObjectDoesNotExist:
                return Response(
                {
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': "Project not found",
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            projects = Project.objects.all().prefetch_related('members')
            return Response(
            {
                'status': status.HTTP_200_OK,
                'message': "Projects retrieved successfully",
                'data': ProjectModelSerializer(projects, many=True).data
            }, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        serializer = ProjectModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                'status': status.HTTP_201_CREATED,
                'message': "Project created successfully",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(
        {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': "Invalid data",
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, id):
        try:
            project = Project.objects.get(id=id)
            serializer = ProjectModelSerializer(instance=project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': "Project updated successfully",
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': "Invalid data",
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(
            {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Project not found",
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, id):
        try:
            project = Project.objects.get(id=id)
            project.delete()
            return Response(
            {
                'status': status.HTTP_200_OK,
                'message': "Project deleted successfully",
                'data': None
            }, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response(
            {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Project not found",
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)


class TaskAPIView(APIView):
    def get(self, request: Request, id=None):
        if id:
            try:
                task = Task.objects.select_related('project').get(id=id)
                return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': "Task retrieved successfully",
                    'data': TaskModelSerializer(task).data
                }, status=status.HTTP_200_OK)
            
            except ObjectDoesNotExist:
                return Response({
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': "Task not found",
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = Task.objects.all().select_related('project')
            return Response(
            {
                'status': status.HTTP_200_OK,
                'message': "Tasks retrieved successfully",
                'data': TaskModelSerializer(tasks, many=True).data
            }, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            {
                'status': status.HTTP_201_CREATED,
                'message': "Task created successfully",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(
        {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': "Invalid data",
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, id):
        try:
            task = Task.objects.get(id=id)
            serializer = TaskModelSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': "Task updated successfully",
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': "Invalid data",
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(
            {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Task not found",
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return Response(
            {
                'status': status.HTTP_200_OK,
                'message': "Task deleted successfully",
                'data': None
            }, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response(
            {
                'status': status.HTTP_404_NOT_FOUND,
                'message': "Task not found",
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)
        
