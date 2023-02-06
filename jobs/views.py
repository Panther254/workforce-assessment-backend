from rest_framework import generics, status
from rest_framework.response import Response
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer, PositionSerializer, TechStackSerializer
from rest_framework.parsers import FormParser , MultiPartParser 

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = JobSerializer

    

    def post(self,request,*args,**kwargs):
        self.request.data._mutable = True
        tech_stacks = self.request.data.pop('techstacks')
        positionss = self.request.data.pop('positions')
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors)
        serializer.save()
        tech_stack_objects = []
        positions_objects = []
        job_id = serializer.data['id']
        print(job_id)

        for tech_stack in tech_stacks:
            tech_stack_objects.append({'job': job_id, 'name': tech_stack})
        
        for positions in positionss:
            for position in positions.split(","):
                positions_objects.append({'job': job_id, 'name': position})

        tech_stack_serializer = TechStackSerializer(data=tech_stack_objects,many=True)
        positions_serializer =  PositionSerializer(data=positions_objects,many=True)

        if tech_stack_serializer.is_valid() and positions_serializer.is_valid():
            tech_stack_serializer.save()
            positions_serializer.save()
        else:
            context = { 'error': 'Error adding the content' }
            print(tech_stack_serializer.errors)
            print(positions_serializer.errors)
            return Response(context)

        saved_job = Job.objects.get(pk=job_id)
        serialized_job = JobSerializer(data=saved_job)
        if serialized_job.is_valid():
            return Response(serialized_job.data,status.HTTP_202_ACCEPTED)
        else:
            print("You are looking for me")
            return Response(serialized_job.errors)

class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    parser_classes = [FormParser, MultiPartParser]

