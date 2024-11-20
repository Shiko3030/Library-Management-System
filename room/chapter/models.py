from django.db import models


class Category(models.Model):

    name=models.CharField(max_length=50)


    def __str__(self):

        return self.name


class Book(models.Model):
    STATUS={
        'available':'available',
        'rental':'rental',
        'sold':'sold',
    }
    ACTIVE={
        'Yes':'Yes',
        'No':'No',
    }
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    title =models.CharField(max_length=50,null=True,blank=True)
    authoer=models.CharField(max_length=50,null=True,blank=True)
    photo_book=models.ImageField(upload_to='photo',null=True,blank=True)
    photo_authoer=models.ImageField(upload_to='photo',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    retal_price_day=models.IntegerField(null=True,blank=True)
    retal_period=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=50,choices=STATUS,null=True,blank=True)
    total_rental=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)



    def __str__(self):

        return self.title or "Untitled Book"



        




    @property
    def image_authoer(self):
        try:
            url_1 = self.photo_authoer.url
        except:
            url_1 = '\media\photo\_null.jpg'
        return url_1
    
    @property
    def image_books(self):
        try:
            url_2 = self.photo_book.url
        except:
            url_2 = '\media\photo\_null.jpg'
        return url_2
    

  