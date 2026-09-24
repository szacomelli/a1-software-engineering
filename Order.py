class Product():
  def __init__(self, name: str, price: float, quantity: int = 1):
    self.name = name
    self.price = price
    self.quantity = quantity


  def __str__(self):
    return f"{self.name}; Quantity: {self.quantity}; Price: {self.price:.2f}"


class Client():
  def __init__(self, name: str):
    self.name = name

  def __str__(self):
    return self.name


class Order():
  def __init__(self, client: Client):
    self.client = client
    self.coupon = None
    self.address = None
    self.pay_method = None
    self.observation = None
    self.products = []


  def total(self) -> float:
    total_value = 0
    for product in self.products:
      total_value += product.price * product.quantity

    return total_value


  def __str__(self):
    prods = "".join(f" - {idx+1}: {product}\n" for idx, product in enumerate(self.products))
    text = [f"Client name: {self.client or 'None'}\n",
      f"Coupon used: {self.coupon}\n" if self.coupon else "",
      f"Address inputed: {self.address}\n" if self.address else "",
      f"Payment method: {self.pay_method}\n" if self.pay_method else "",
      f"Obs.: {self.observation}\n" if self.observation else "",
      f"Products:\n{prods}"]

    return "".join(txt for txt in text)


class OrderBuilder():
  def __init__(self, order = Order):
    self.order = order(None)


  def set_client(self, client: Client):
    # Set the parameter client 
    self.order.client = client
    return self


  def set_coupon(self, coupon: str):
    # Set the optional parameter 'coupon'
    self.order.coupon = coupon
    return self


  def set_address(self, address: str):
    # Set the optional parameter 'address'
    self.order.address = address
    return self


  def set_pay_method(self, pay_method):
    # Set the optional parameter 'pay_method'
    self.order.pay_method = pay_method
    return self


  def set_observation(self, observation: str):
    # Set the optional parameter 'observation'
    self.order.observation = observation
    return self


  def add_product(self, product: Product):
    # Add a product item with type Product
    for old_product in self.order.products:
      if old_product.name == product.name:
        old_product.quantiy += product.quantity
        return self
      
    self.order.products.append(product)
    return self

  def add_product_by_name(self, name: str, price: float, quantity: int = 1):
    # Add a product by its values
    for old_product in self.order.products:
      if old_product.name == name:
        old_product.quantity += quantity
        return self
      
    product = Product(name, price, quantity)
    self.order.products.append(product)
    return self


  def build(self):
    if not self.order.client:
      raise ValueError("You must set a client for the order")
    return self.order


if __name__ == "__main__":
  print("Rodando main...\n")

  print("Definindo produtos\n")
  maca = Product("Maçã", 1.00, 4)
  print(maca)
  macarrao = Product("Macarrão", 3.99, 6)
  print(macarrao)

  print("Definindo cliente\n")
  cliente = Client("Ada Lovelace")
  print(cliente)

  print("Construindo pedido\n")
  order = (OrderBuilder(Order)
             .set_client(cliente)
             .set_address("Rua Voluntários da Pátria")
             .set_coupon("OMELHORCUPOM")
             .set_pay_method("Pix")
             .set_observation("Pedido deve ser entregue com urgência")
             .add_product(maca)
             .add_product(macarrao)
             .add_product_by_name("Pera", 0.80, 3)
             .build())

  print(order)
  print(f"{order.total():.2f}")