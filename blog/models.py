from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=450) #заголовок поста
    author = models.ForeignKey(
        'auth.User', #автор поста, которого выбираем мы в административной панели управления
        on_delete=models.CASCADE, #удаление поста
    )
    body = models.TextField() #поле (тело) поста

    #метод - возвращение заголовка поста в виде строки
    def _str_(self):
        return self.title

