from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.CharField(max_length=80)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)