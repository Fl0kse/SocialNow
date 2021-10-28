from django.db import models
from django.contrib.auth.models import User
from SocialNetworks.models import TwitterModel, InstagramModel, VKModel, FaceBookModel

# Create your models here.
class Profile(models.Model):
    user_name = models.CharField(max_length=15)
    email = models.EmailField()
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    twitter = models.ForeignKey(TwitterModel, blank=True, null=True, on_delete=models.CASCADE)
    vk = models.ForeignKey(InstagramModel, blank=True, null=True, on_delete=models.CASCADE)
    FaceBook = models.ForeignKey(VKModel, blank=True, null=True, on_delete=models.CASCADE)
    instagram = models.ForeignKey(FaceBookModel, blank=True, null=True, on_delete=models.CASCADE)
