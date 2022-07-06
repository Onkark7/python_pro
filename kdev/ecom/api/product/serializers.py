from dataclasses import fields
from email.mime import image
from pyexpat import model

from pkg_resources import require
from rest_framework import serializers

from .models import product

class productSerializer(serializers.HyperlinkedModelSerializer) :
  image =serializers.ImageField(
    max_length=None, allow_empty_file=False, allow_null=True, required=False)
  class Meta:
        model = product
        fields = ('id', 'name','description','price','image','category')