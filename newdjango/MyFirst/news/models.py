from django.db import models
class Article(models.Model):
    title = models.CharField('Title', max_length=40)
    announce = models.CharField('Announce', max_length=256)
    full_text = models.TextField('Full text')
    image = models.ImageField('Image', upload_to='uploads/', height_field=None, width_field=None, max_length=100)
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/news/{self.id}'
# Create your models here.
