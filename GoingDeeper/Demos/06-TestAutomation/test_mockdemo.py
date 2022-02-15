import mockdemo_mycode

def test_build_url(mocker):

    # Mock BASE_URL, when used in mockdemo_mycode.
    mocker.patch.object(mockdemo_mycode, 'BASE_URL', 'http://localhost/products')

    # Call function-under-test.
    actual = mockdemo_mycode.build_url(minPrice=100, maxPrice=500, order='desc')

    # This is the result we're expecting.
    expected = 'http://localhost/products?minPrice=100&maxPrice=500&order=desc'

    # Verify the result was correct.
    assert expected == actual


def test_get_meaning_of_life(mocker):

    # Mock calculate_meaning_of_life(), when called from mockdemo_mycode.
    mocker.patch(
        'mockdemo_mycode.calculate_meaning_of_life',
        return_value='wibble'
    )

    # Call function-under-test.
    actual = mockdemo_mycode.get_meaning_of_life()

    # This is the result we're expecting.
    expected = 'The meaning of life is wibble'

    # Verify the result was correct.
    assert expected == actual


def test_get_product(mocker):

    def dummy_get_product(self):
        return 'wibble'

    # Mock DataLoader.load_product(), when called from mockdemo_mycode.
    mocker.patch(
        'mockdemo_mycode.DataLoader.load_product',
        dummy_get_product
    )

    # Call function-under-test.
    actual = mockdemo_mycode.get_product()

    # This is the result we're expecting.
    expected = 'Product is wibble'

    # Verify the result was correct.
    assert expected == actual
