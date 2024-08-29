from django.test import TestCase
from decimal import Decimal
from .models import Recipe
from django.urls import reverse
from django.urls import resolve
from recipe.views import RecipeListView, RecipeDetailView


class RecipeTestCase(TestCase):
    def setUp(self):
        # Set up initial data for testing
        self.recipe = Recipe.objects.create(
            name="Spaghetti Bolognese", cooking_time=45, difficulty="Medium"
        )
        self.taco_recipe = Recipe.objects.create(
            name="Taco", cooking_time=20, difficulty="Easy"
        )

    def test_recipe_creation(self):
        # Test that the recipe is created successfully
        self.assertEqual(self.recipe.name, "Spaghetti Bolognese")
        self.assertEqual(self.recipe.cooking_time, 45)
        self.assertEqual(self.recipe.difficulty, "Medium")

    def test_recipe_string_representation(self):
        # Test the string representation of the recipe
        self.assertEqual(str(self.recipe), "Spaghetti Bolognese")

    def test_taco_recipe_creation(self):
        # Test that the taco recipe is created successfully
        self.assertEqual(self.taco_recipe.name, "Taco")
        self.assertEqual(self.taco_recipe.cooking_time, 20)
        self.assertEqual(self.taco_recipe.difficulty, "Easy")

    def test_taco_recipe_string_representation(self):
        # Test the string representation of the taco recipe
        self.assertEqual(str(self.taco_recipe), "Taco")


class RecipeDetailViewTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Taco", cooking_time=20, difficulty="Easy"
        )

    def test_recipe_detail_view(self):
        response = self.client.get(
            reverse("recipe:recipe-detail", kwargs={"pk": self.recipe.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.name)
        self.assertTemplateUsed(
            response, "recipe/recipe_detail.html"
        )  # Use the correct template name


class RecipeUrlTest(RecipeTestCase):
    def test_recipe_list_url_is_resolved(self):
        url = reverse("recipe:recipe-list")
        self.assertEqual(resolve(url).func.view_class, RecipeListView)

    def test_recipe_detail_url_is_resolved(self):
        url = reverse("recipe:recipe-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, RecipeDetailView)
