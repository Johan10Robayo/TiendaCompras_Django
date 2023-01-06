class Carro:
    def __init__(self,request):
        self.__request=request
        self.__session=request.session
        carro=self.__session.get("carro")
        if not carro:
            carro=self.__session["carro"]={}
        #else:
        self.__carro=carro

    def agregar(self,producto):
        if str(producto.id) not in self.__carro.keys():
            self.__carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key,value in self.__carro.items():
                if key==str(producto.id):
                    value["cantidad"]+=1
                    value["precio"]=float(value["precio"])+float(producto.precio)
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.__session["carro"]=self.__carro
        self.__session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.__carro:
            del self.__carro[producto.id]
            self.guardar_carro()

    def restar_producto(self,producto):
        for key, value in self.__carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                value["precio"] = float(value["precio"]) - float(producto.precio)
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.__session["carro"]={}
        self.__session.modified = True