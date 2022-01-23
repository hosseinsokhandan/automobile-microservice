from tortoise import fields, models


class AutomobileModel(models.Model):
    id = fields.IntField(pk=True)
    model = fields.CharField(max_length=64)
    manufacturer = fields.CharField(max_length=64)
    type = fields.CharField(max_length=64)

    class Meta:
        model = "automobile"

    def __str__(self) -> str:
        return self.model
