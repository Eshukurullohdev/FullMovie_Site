from django.db import models


class Main_Movie(models.Model):
    main_banner = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=50)
    janr = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    yili = models.IntegerField()
    davomiy = models.CharField(max_length=50)
    tavsifi = models.TextField()
    video_img = models.ImageField(upload_to='media/', null=True)
    
    def __str__(self):
        return self.nomi
    
    
# OOP 