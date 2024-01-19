from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str) -> None:
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self) -> str:
        final_products = []
        for p in self.products:
            final_products.append(f"{p.name}: {p.quantity}")
        final_products = "\n".join(final_products)
        return final_products
