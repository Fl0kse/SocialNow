from django.db import models


# Create your models here.
class TwitterModel(models.Model):
    api_key = models.CharField(max_length=150)


class FaceBookModel(models.Model):
    api_key = models.CharField(max_length=150)


class VKModel(models.Model):
    api_key = models.CharField(max_length=150)


class InstagramModel(models.Model):
    api_key = models.CharField(max_length=150)
