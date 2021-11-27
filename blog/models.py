from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=30)
    maqola = models.TextField() 
    def __str__(self):
        return self.maqola

class Rasm(models.Model):
    rasm = models.URLField()
    maqolaid = models.ForeignKey(Maqola, on_delete=models.CASCADE)
    def __str__(self):
        return self.maqolaid.sarlavha