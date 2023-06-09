from django.db import models

class Post(models.Model):
    title = models.CharField('Post title', max_length=100)
    description = models.TextField('Post text')
    author = models.CharField('Author`s name', max_length=100)
    date = models.DateField('Publication date')
    img = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
            return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comments(models.Model):
     email = models.EmailField()
     name = models.CharField('Name', max_length=50)
     text_comments = models.TextField('Text of the comment', max_length=2000)
     post = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)

     def __str__(self):
            return f'{self.name}, {self.post}'
    
     class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
     ip = models.CharField('IP-adress', max_length=100)
     pos=models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)