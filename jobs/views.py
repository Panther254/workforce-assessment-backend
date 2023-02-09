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
            
        context = {
            "id": serializer.data['id'],
            "job_title": serializer.data['job_title'],
            "company_title": serializer.data['company_title'],
            "company_logo_url": serializer.data['company_logo_url'],
            "techstacks": tech_stack_serializer.data,
            "positions": positions_serializer.data,
            "number_of_employees": serializer.data['number_of_employees'],
            "country": serializer.data['country'],
            "salary_range": serializer.data['salary_range'],
            "job_type": serializer.data['job_type'],
            "sector": serializer.data['sector'],
            "applications": [],
            "date_posted": serializer.data['date_posted'],
        }
        
        return Response(context,status=status.HTTP_201_CREATED)

class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    parser_classes = [FormParser, MultiPartParser]

class JobRetrieveView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = RetrieveJobSerializer
