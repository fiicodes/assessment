from django.db import models

# todo model to store the task and the owner of that task which is a primary key and the created time.


class todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    task = models.TextField()
   
    owner = models.ForeignKey('auth.User', related_name='mess', on_delete=models.CASCADE,default="")

    class Meta:
        ordering = ['created_at']