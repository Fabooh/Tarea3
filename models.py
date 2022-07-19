import email
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy()

#Creamos tablas
class Personas(db.Model):
    __tablename__='personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    usuario_suscripcion_activa = db.Column(db.Boolean)
    artista_nombre_artistico = db.Column(db.String(100))
    artista_verificado = (db.Column(db.Boolean))
    tipo_de_persona = (db.Column(db.Boolean, nullable=False))

    @classmethod
    def create(cls, nombre,email,password,tipo_de_persona):
        persona = Personas(nombre = nombre,email=email,password=password,tipo_de_persona=tipo_de_persona)
        return persona.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False
    
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return self
        except:
            return False

    
    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.apellido,
            'password':self.password,
            'estado de suscripcion':self.usuario_suscripcion_activa,
            'nombre artistico':self.artista_nombre_artistico,
            'artista verificado':self.artista_verificado,
            'tipo de usuario':self.tipo_de_persona
        }


class Facturas(db.Model):
    __tablename__ = 'facturas'
    id_factura = db.Column(db.Integer, primary_key = True)
    monto_facturado = db.Column(db.Integer)
    fecha_facturacion = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    estado = db.Column(db.Boolean)
    metodo_de_pago = db.Column(db.String(100))
    fecha_hora_pago = db.Column(db.DateTime)
    id_persona = db.Column(db.Integer, db.ForeignKey("personas.id"))

    @classmethod
    def create(cls, monto_facturado, fecha_facturacion,fecha_vencimiento,estado,metodo_de_pago,fecha_hora_pago,id_persona):
        factura = Facturas(cls, monto_facturado = monto_facturado, fecha_facturacion = fecha_facturacion, fecha_vencimiento=fecha_vencimiento,estado=estado,metodo_de_pago=metodo_de_pago,fecha_hora_pago=fecha_hora_pago,id_persona=id_persona)
        return factura.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False
    
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return self
        except:
            return False
    
    def json(self):
        return {
            'id factura': self.id_factura,
            'monto facturado': self.monto_facturado,
            'fecha de facturacion': self.fecha_facturacion,
            'fecha de vencimiento': self.fecha_vencimiento,
            'estado':self.estado,
            'metodo de pago':self.metodo_de_pago,
            'fecha y hora del pago':self.fecha_hora_pago,
            'id persona':self.id_persona
        }


class Canciones(db.Model):
    __tablename__ = 'canciones'
    id_cancion = db.Column(db.Integer, primary_key = True)
    nombre_cancion = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String)
    fecha_composicion = db.Column(db.Date)   
    
    @classmethod
    def create(cls, nombre_cancion,letra,fecha_composicion):
        cancion = Canciones(nombre_cancion = nombre_cancion,letra=letra,fecha_composicion=fecha_composicion)
        return cancion.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False
    
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return self
        except:
            return False

    
    def json(self):
        return {
            'id': self.id_cancion,
            'nombre':self.nombre_cancion,
            'letra': self.letra,
            'fecha de composicion':self.fecha_composicion
        }

class Reproducciones(db.Model):
    __tablename__ = 'reproducciones'
    id_persona = db.Column(db.Integer,db.ForeignKey("personas.id") ,primary_key = True )
    id_cancion = db.Column(db.Integer,db.ForeignKey("canciones.id_cancion") ,primary_key = True,)
    cantidad_reproducciones = db.Column(db.BigInteger)
    ultima_reproduccion = db.Column(db.DateTime)
    
    @classmethod
    def create(cls, nombre_cancion,letra,fecha_composicion):
        cancion = Canciones(nombre_cancion = nombre_cancion,letra=letra,fecha_composicion=fecha_composicion)
        return cancion.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False
    
    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return self
        except:
            return False

    
    def json(self):
        return {
            'id': self.id_cancion,
            'nombre':self.nombre_cancion,
            'letra': self.letra,
            'fecha de composicion':self.fecha_composicion
        }