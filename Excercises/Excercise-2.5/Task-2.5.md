# Task-2.5

## Models/Tables from Exercise 2.3

### Recipe Model
- **Current Attributes**: `name`, `cooking_time`, `difficulty`
- **Changes**:
  - **Add**: `description` (TextField) - To provide more details about the recipe.
  - **Add**: `created_at` (DateTimeField) - To track when the recipe was created.
  - **Add**: `updated_at` (DateTimeField) - To track when the recipe was last updated.

### Ingredient Model
- **Current Attributes**: `recipe`, `name`, `quantity`
- **Changes**:
  - **Add**: `unit` (CharField) - To specify the unit of measurement for the quantity.
  - **Add**: `created_at` (DateTimeField) - To track when the ingredient was created.
  - **Add**: `updated_at` (DateTimeField) - To track when the ingredient was last updated.
  - **Change**: `quantity` from `CharField` to `DecimalField` - To store numeric values more accurately.

### Explanation of Changes
- **description**: Added to the `Recipe` model to provide more details about each recipe.
- **created_at** and **updated_at**: Added to both `Recipe` and `Ingredient` models to track creation and modification times.
- **unit**: Added to the `Ingredient` model to specify the unit of measurement for the quantity.
- **quantity**: Changed from `CharField` to `DecimalField` in the `Ingredient` model to store numeric values more accurately.