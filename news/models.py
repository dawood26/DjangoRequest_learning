from django.db import models
# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70 )
    contact = models.CharField(max_length=30 ,null=True)
    email = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
