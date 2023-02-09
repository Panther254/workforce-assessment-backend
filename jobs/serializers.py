from .models import Job
from rest_framework import serializers
from .models import Job, JobApplication, TechStack, Position


class JobSerializer(serializers.ModelSerializer):
    applications = serializers.StringRelatedField(many=True, read_only=True)
    positions = serializers.StringRelatedField(many=True, read_only=True)
    techstacks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ["applications","positions","techstacks"]


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ["jobs",]

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'


class RetrieveJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_title','company_title','sector']
