from ckeditor_uploader.fields import RichTextUploadingField
from contas.models import Perfil
from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    imagem_capa = models.ImageField(
        null=True, blank=True, upload_to='static/blog/'
    )
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo


class Tag(models.Model):
    nome = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)


class Assunto(models.Model):
    nome = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)


class Situacao(models.Model):
    nome = models.CharField(max_length=50)
    posts = models.ManyToManyField(
        Post, through='PostSituacao', through_fields=('situacao', 'post')
    )


class PostSituacao(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
    post_situacao = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_situacao'
    )
    data = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ['post', 'situacao']


class Topico(models.Model):
    conteudo = RichTextUploadingField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comentario(models.Model):
    texto = models.TextField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
