from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """get_first should return first element."""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    get_first(dog_breeds)  # RV should be husky
    assert get_first(dog_breeds) == "husky"
