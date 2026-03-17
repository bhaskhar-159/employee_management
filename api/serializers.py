from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate_email(self, value):
        if not value.endswith("@company.com"):
            raise serializers.ValidationError("Email must be company domain")
        return value

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be positive")
        return value

    def validate_emp_id(self, value):
        if not value.startswith("EMP"):
            raise serializers.ValidationError("emp_id must start with EMP")

        number_part = value[3:]

        if not number_part.isdigit():
            raise serializers.ValidationError("emp_id must contain numbers after EMP")

        return value