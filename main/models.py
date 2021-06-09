from django.db import models

class Posts(models.Model):
    img = models.ImageField('Фото', upload_to='posts_media/', default='')
    title = models.CharField(max_length=50, default='title')
    #datetime = models.DateTimeField()
    description = models.TextField('Описание к посту', max_length=500, default='description')
    user_nickname = models.CharField('Никнэйм юзера', max_length=50, default='user_nickname')
    user_avatar = models.ImageField('Аватар профиля', upload_to='posts_media/', default='')
    place = models.CharField('Местоположение', max_length=50, default='place')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'


