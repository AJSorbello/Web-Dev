from django.db import models


class Ingredient(models.Model):
    recipe = models.ForeignKey(
        "recipe.Recipe", on_delete=models.CASCADE, related_name="ingredient_set"
    )  # This related_name should be unique
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.unit:
            return f"{self.quantity} {self.unit} of {self.name} for {self.recipe.name}"
        return f"{self.quantity} of {self.name} for {self.recipe.name}"
