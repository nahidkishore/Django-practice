from django.db import models

# Create your models here.
CREATE TABLE person (
  "id" serial NOT NULL PRIMARY KEY,
  "first_name" varchar(30) NOT NULL,
  "last_name" varchar(30) NOT NULL

    
);

class Person(models.Model):
  id=models.AutoField(primary_key=true)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  
  
    
    