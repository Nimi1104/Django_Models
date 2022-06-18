from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        'auth.User', 
        on_delete= models.CASCADE,
    )
    body = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    
    def datepublished(self):
        return self.created_date.strftime('%d, %B %Y')

    def  __str__(self):
        return self.title
    class Meta:
        ordering = ['created_date']

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])
