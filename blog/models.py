from django.db import models


class Blog(models.Model):
    objects=models.Manager()
    title=models.CharField(max_length=200)
    pub_date=models.DateField('date published')
    body=models.TextField()
    writer=models.CharField(max_length=30,default="admin")
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:20]    
