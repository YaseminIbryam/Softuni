class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in Catalogue.products if first_letter == product[0]]

    # def __repr__(self):
    #     return f"Items in the {self.name} catalogue:\n{'\n'.join(sorted(Catalogue.products))}"
    def __repr__(self):
        info = f"Items in the {self.name} catalogue:\n"
        info += "\n".join([f"{item}" for item in sorted(Catalogue.products)])
        return info

