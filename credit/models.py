from django.db import models


class BaseModel(models.Model):
    created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Application(BaseModel):
    pass


class Contract(BaseModel):
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE
    )


class Manufacturer(BaseModel):
    pass


class Product(BaseModel):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='products'
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='products'
    )
