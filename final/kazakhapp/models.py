from audioop import reverse
from django.db import models

# Create your models here.
class City(models.Model):
          name = models.CharField(max_length = 200)
          content = models.TextField()
          launch_year = models.DateTimeField("launched year")
          slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL" , default='city')
          city_photo = models.URLField(max_length=200, blank=True, null=False)
          def get_absolute_url(self):
                    return reverse('post', kwargs={'post_slug':self.slug})

          def __str__(self):
                    return self.name

# CRUD
class Comment(models.Model):
          # author_name = models.CharField(max_length = 200)
          title = models.CharField(max_length = 200)
          content = models.TextField()
          launch_year = models.DateTimeField("published year")


          def __str__(self):
                    return self.title

#REGISTRATION
class User(models.Model):
          firstname = models.CharField(max_length = 200)
          lastname = models.CharField(max_length = 200)
          iin = models.CharField(max_length=12, null=True, blank=True)
          birthdate = models.DateField("birthdate", null=True, blank=True)
          email = models.EmailField(null=True, blank=True)
          phone = models.CharField(max_length=11,null=True, blank=True)
          gender = models.CharField(max_length= 10,null=True, blank=True)
          
          def __str__(self):
                    return self.firstname 
          def get_absolute_url(self):
                    return "test/fail"

class Artist(models.Model):
          art_id = models.IntegerField(default=0)
          name = models.CharField(max_length = 200)
          biography = models.TextField(blank=True)
          def __str__(self):
                    return self.name
          def get_absolute_url(self):
                    return "test/fail"
                    
class Region(models.Model):
          name = models.CharField(max_length = 200)
          illness = models.IntegerField()
          def __str__(self):
                    return self.name

