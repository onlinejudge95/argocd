from argopy import dummy


def test_dummy_function():
    response = dummy.add(1, 2)
    assert response == 3
