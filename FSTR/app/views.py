from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics, viewsets, mixins
from .serializers import *


class PerevalAddAPI(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request, **kwargs):
        pereval = PerevalSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data, status=200, safe=False)

        except Exception as exc:
            responseData = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(responseData, status=400, safe=False)


class PerevalDetailAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalDetailSerializer

    def update(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        try:
            instance = PerevalAdded.objects.get(pk=pk)
        except:
            return Response({'error': 'Такого перевала не существует'}, status=400)

        if instance.status !='N':
            return Response({'message': 'Перевал на модерации, вы не можете вносить изменения',
                             'state': 0}, status=400)
        else:
            serializer = PerevalDetailSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'state': 1}, status=200)


class AuthEmailPerevalAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = AuthEmailPerevalSerializer

    def get(self, **kwargs):
        email = kwargs.get('email', None)
        if PerevalAdded.objects.filter(user__email=email).is_exist:
            responseData = AuthEmailPerevalSerializer(PerevalAdded.objects.filter(user__email=email), many=True).data
        else:
            responseData = {'message': f'Нет записей от email = {email}'}
        return Response(responseData, status=200)
