from rest_framework import generics, status
from rest_framework.response import Response
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer, PositionSerializer, TechStackSerializer, RetrieveJobSerializer
from rest_framework.parsers import FormParser , MultiPartParser 

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = JobSerializer

    

    def post(self,request,*args,**kwargs):
        self.request.data._mutable = True
        tech_stackss = self.request.data.pop('tech_stacks')
        positionss = self.request.data.pop('positions')
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            context = {'message': 'Error adding the Job instance',
                       'error': serializer.errors}
            return Response(context)
        serializer.save()
        tech_stack_objects = []
        positions_objects = []
        job_id = serializer.data['id']
        print(tech_stackss)

        for tech_stacks in tech_stackss:
            for tech_stack in tech_stacks.split(","):
                tech_stack_objects.append({'job': job_id, 'name': tech_stack})
        
        for positions in positionss:
            for position in positions.split(","):
                positions_objects.append({'job': job_id, 'name': position})

        tech_stack_serializer = TechStackSerializer(data=tech_stack_objects,many=True)
        positions_serializer =  PositionSerializer(data=positions_objects,many=True)

        if tech_stack_serializer.is_valid():
            tech_stack_serializer.save()
        else:
            context = {'message': 'Error adding the techstacks. The field is empty',
                       'error': tech_stack_serializer.errors}
            return Response(context)
        
        if positions_serializer.is_valid():
            positions_serializer.save()
        else:
            context = {'message': 'Error adding the positions. The field is empty', 'error': positions_serializer.errors}
            return Response(context)
            
        saved_job = Job.objects.get(id=job_id)
        serialized_job = JobSerializer(data=saved_job)
        if serialized_job.is_valid():
            return Response(serialized_job.data,status.HTTP_202_ACCEPTED)
        else:
            context = {'message': 'Job has been saved. But there is an error fetching the saved model',
                       'error': serialized_job.errors}
            return Response(context)

class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    parser_classes = [FormParser, MultiPartParser]

class JobRetrieveView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = RetrieveJobSerializer
