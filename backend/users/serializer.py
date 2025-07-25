from rest_framework import serializers
from .models import User,Student,Instructor


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','role','username','password','email','first_name','last_name']


        def save(self,*args, **kwargs):
            is_new = self.data['username'] is None
            super().save(*args, **kwargs)
            if is_new:
                if self.role == 'student':
                    Student.objects.create(user=self)
                elif self.role == 'instructor':
                    Instructor.objects.create(user=self)
            return self


    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.get('role')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        if role == 'student':
            Student.objects.create(user=user)
        elif role == 'instructor':
            Instructor.objects.create(user=user)

        return user


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','user']


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id','user','bio','expertise','is_approved']

