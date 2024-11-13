from django.db import models
from django.conf import settings

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet_description = models.TextField()
    post_description = models.TextField()
    media = models.ImageField(upload_to='reports/', null=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='report_likes', blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)  # Campo para latitud
    longitude = models.DecimalField(max_digits=12, decimal_places=9, null=True, blank=True)  # Campo para longitud

    def __str__(self):
        return f"Report by {self.user.username}"

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.report}"
