class Tornillo:
    def __init__(self):
        self.users = {}
        self.productos = self.cargar_productos() 
        
    def menu_principal(self):
     while True:
        print("Ferreteria El Tornillo Feliz")
        print("Menu:")
        print("1. Iniciar sesion")
        print("2. (Nuevo usuario)Registrarte")
        print("3. Salir")
        selected_option = input("Seleccione una opción: ")

        match selected_option:
            case "1":
                user = self.login()
                if user:
                    self.menu_secun(user)
            case "2":
                self.registrar_cuenta()
            case "3":
                print("Muchas gracias,vuelva pronto")
                break

    def menu_secun(self, user):
        while True:
            print(" ")
            print(f"Bienvenido: {user}")
            print("1. Ver productos")
            print("2. Comprar")
            print("3. Ver historial de compras")
            print("4. Cerrar Sesión")
            opcion = input("Seleccione una opción: ")
            match opcion:
             case "1":
                print(" ")
                print("Productos:")
                self.productos.mostrar(mostrar_r=False)
             case "2":
                self.comprar(user)
             case "3":
                self.ver_historial_compras(user)
             case "4":
                print("")
                print("Sesion cerrada.")
                break
           
                 
    def cargar_productos(self):
        productos = Producto("El Tornillo Feliz", None)

        try:
            with open("productos.txt", "r") as archivo:
             for linea in archivo:
                name, precio = linea.strip().split(":")
                producto = Producto(name, float(precio))
                productos.agregar_nodoh(producto)
        except FileNotFoundError:
          print("El archivo 'productos.txt' no existe.")

        return productos
    
    def registrar_cuenta(self):
        name = input("Ingrese su nombre: ")
        contrasenia = input("Ingrese una contraseña: ")
        self.users[name] = contrasenia
        self.guardar_users()
        
    def cargar_users(self):
        try:
          with open("user.txt", "r") as archivo:
            for linea in archivo:
                user, contrasenia = linea.strip().split(":")
                self.users[user] = contrasenia
        except FileNotFoundError:
            print("El archivo 'user.txt' no existe.")

    def login(self):
        self.cargar_users()
        name = input("Ingrese su nombre: ")
        contrasenia = input("Ingrese una contraseña: ")
        if self.users.get(name) == contrasenia:
          print(" ")
          print("Inicio de sesión exitoso.\n")
          return name
        else:
          print("Datos incorrectos.")
        return None

    def guardar_users(self):
       with open("user.txt", "w") as archivo:
        for user, contrasenia in self.users.items():
            archivo.write(f"{user}:{contrasenia}\n")

    def comprar(self, user):
        print(" ")
        print("Lista de productos:")
        for index, producto in enumerate(self.productos.nodosh, start=1):
            print(f"{index}. {producto.name} - costo: s/{producto.precio}")
        try:
            print(" ")
            opcion = int(input("Seleccione el producto: "))
            if 1 <= opcion <= len(self.productos.nodosh):
                producto_elegido = self.productos.nodosh[opcion - 1]
                with open("his_comp.txt", "a") as archivo:
                    archivo.write(f"{user}:{producto_elegido.name}\n")
                print("Compra exitosa.")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")
    def ver_historial_compras(self,user):
        try:
            with open("his_comp.txt", "r") as archivo:
                compras = [linea.strip().split(":") for linea in archivo if linea.startswith(user)]
                if compras:
                    print(" ")
                    print("Historial de compras:")
                    for compra in compras:
                        print("*",f"{compra[1]}")
                else:
                    print("No hay productos en su historial.")
        except FileNotFoundError:
            print("No hay historial de compras.")
    
class Producto:
    
    def __init__(self, name, precio):
        self.name = name
        self.precio = precio
        self.nodosh = []
        
    def agregar_nodoh(self, producto):
        self.nodosh.append(producto)
        
    def mostrar(self, nivel=0, mostrar_r=True):
        if mostrar_r:
            
            print("  " * nivel + f"{self.name} - costo: s/{self.precio}")
        for nodosh in self.nodosh:
            nodosh.mostrar(nivel + 1)
                             
if __name__ == "__main__":
    tienda = Tornillo()
    tienda.menu_principal()

