from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a Product instance from a dictionary."""
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """Fetches and returns a list of Product instances."""
    return [Product.from_dict(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Fetches and returns a single Product instance by ID."""
    product_data = dao.get_product(product_id)
    return Product.from_dict(product_data)


def add_product(product: dict):
    """Adds a new product to the database."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Updates the quantity of a product by ID. Raises an error for negative values."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
