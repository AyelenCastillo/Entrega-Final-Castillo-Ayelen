class Cliente:
    def __init__(self, usuario, email, telefono, direccion):
        self.usuario = usuario
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.usuario}, Email: {self.email}, Teléfono: {self.telefono}, Dirección: {self.direccion}"

    def buy(self, producto):
        print(f"{self.usuario} ha comprado {producto}.")
