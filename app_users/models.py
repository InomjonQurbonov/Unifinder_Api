from django.db import models
from django.contrib.auth import get_user_model

User  = get_user_model()

class Gender(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table = 'gender'
        verbose_name = 'Gender'
        verbose_name_plural = 'Gender'

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

        
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'User'
        
        
class PasswordResets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'
        

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        verbose_name_plural = 'Author'
        

class Paper(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    paper_title = models.CharField(max_length=255,blank=True, null=True)
    paper_section = models.CharField(max_length=255, blank=True, null=True)
    paper_tegs = models.CharField(max_length=255, blank=True, null=True)
    paper_file = models.FileField(upload_to='papers', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.paper_title