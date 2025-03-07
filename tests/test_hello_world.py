from src.rye_template.hello_world import hello_world


def test_hello_world():
    """Test the correct greeting."""
    actual = hello_world()
    expected = "Hello world!"
    assert actual == expected
