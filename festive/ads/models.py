from django.db import models
from PIL import Image as PILImage
# Create your models here.


def upload_location(instance, title):
    return "%s/%s" % (instance.title, filename)


class images(models.Model):
        title = models.CharField(max_length=50)
        image = models.ImageField(upload_to=upload_location,
                                null=True,
                                blank=True,
                                width_field="width_field",
                                height_field="height_field",
                                default='media/def.jfif'
                                )

        height_field = models.IntegerField(default=122)
        width_field = models.IntegerField(default=122)


		def save(self, *args, **kwargs):
			if self.image:
				img = PILImage.open( BytesIO( self.image.read() ) )
				# if img.mode =='RGBA':
				# 	img.convert('RGB')
				width, height = img.size
				if width > 500 or height > 500:
					width, height = 500, 500
				img.thumbnail( (width, height), PILImage.ANTIALIAS )
				save_buff = BytesIO()
				img2 = PILImage.open('media\cooltext333913402881516.png')
				img2.convert('RGBA')
				img.convert('RGBA')
				img.paste(img2, (0, 0), img2)

				img.save( save_buff,format='JPEG', optimize=True, quality=100)
				self.image = InMemoryUploadedFile( save_buff, 'ImageField', "%s.jpg" %self.image.name, 'image/jpeg',save_buff.__le__,  None )
			super( record, self ).save( *args, **kwargs )