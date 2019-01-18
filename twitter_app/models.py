from django.db import models


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('base_user.MyUser',
                             on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="post/",
                                null=True, blank=True)
    context = models.CharField(max_length=5000)

    # logs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.user.get_full_name())


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('base_user.MyUser', on_delete=models.CASCADE)
    context = models.CharField(max_length=2000)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self)