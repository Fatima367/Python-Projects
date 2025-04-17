from inventory.cart import Cart

def test_cart():
    # Create a bucket instance
    cart = Cart(name= "Test Bucket")
    # Add an item to the bucket
    cart.add_item("samsung")
    # Check if both items are present
    assert "samsung" in cart.items
    # Check the final state of the items list
    assert len(cart.items) == 1 