from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . import serializers

@api_view(['GET'])
def get_zaproz(request):
    all_persons= Person.objects.all()
    serializer = serializers.PersonSerializer(all_persons,many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def get_detail(request,pk):
    try:
        one_person = Person.objects.get(id=pk)
        serializer = serializers.PersonSerializer(one_person)
        return Response(serializer.data, status=200)
    except Person.DoesNotExist:
        return RecursionError(f'нет такого человека под id: {pk}',status=404)
    

@api_view(['POST'])
def create_person(request):
    serializer = serializers.PersonSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

@api_view(['DELETE'])
def delete_person(request,pk):
    try:
        person_delete = Person.objects.get(id=pk)
        person_delete.delete()
        return Response(f'удалили человека под id {pk}')
    except Person.DoesNotExist:
        return Response(f'такого человека под id:{pk} нет')
    
@api_view(['PUT'])
def update_person(request,pk):
    try:
        person_update = Person.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = serializers.PersonSerializer(instance=person_update,data=request.data)
        else:
            serializer = serializers.PersonSerializer(instance=person_update,data=request.data,partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status=201)
    except Person.DoesNotExist:
        return Response(f'такого человека под id:{pk} нет')