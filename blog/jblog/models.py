from django.db import models

#class Category(models.Model):
#    name = models.CharField(
#        max_length=80,
#        verbose_name="Categoria"
#    )

class Article(models.Model):
    published_at = models.DateTimeField(
        verbose_name = "Data da Publicação",
        auto_now=True
    )

    title = models.CharField(
        max_length=140, 
        verbose_name="Título",
        db_index = True
    )

    text = models.TextField(
        verbose_name="Artigo"
    )

    #category = models.ForeignKey(
    #    Category, 
    #    on_delete = models.SET_NULL,
    #    blank = True,
    #    null = True
    #)
