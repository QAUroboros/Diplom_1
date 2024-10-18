import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "Кетчуп", 0.5),
    (INGREDIENT_TYPE_SAUCE, "Майонез", 0.4),
    (INGREDIENT_TYPE_FILLING, "Салат", 0.3),
    (INGREDIENT_TYPE_FILLING, "Бекон", 1.0),
])
def test_ingredient_properties(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type, f"Тип ингредиента должен быть '{ingredient_type}'"
    assert ingredient.get_name() == name, f"Название ингредиента должно быть '{name}'"
    assert ingredient.get_price() == price, f"Цена ингредиента должна быть '{price}'"


def test_ingredient_price_type():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный", 0.5)
    assert isinstance(ingredient.get_price(), float), "Цена ингредиента должна быть типа float"


def test_ingredient_with_mock(mocker):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный", 0.5)
    mocker.patch.object(ingredient, 'get_price', return_value=1.0)
    assert ingredient.get_price() == 1.0, "Метод get_price() должен вернуть замоканное значение 1.0"
