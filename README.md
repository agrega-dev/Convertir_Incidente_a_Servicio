#H1
Introduccion

La mesa de ayuda SDP permite crear tickets por correo electronico, al crear el ticket este se crea como incidente, existe el caso que el ticket lo necesitamos como solicitud de servicio.
Para lograr esto en SDP usamos la funcionalidad de custom script y script hecho en python.

Este ejemplo contiene el codigo de script de python que permite hacer este proceso.

#H2
Configuracion

Parametros de acceso
URL de SDP en linea 7
technician_key en linea 6

Parametros de asignacion de tickets
La funcion template() sirve para mapear el contenido del campo subject con la plantilla del catalogo de servicios

```
def template(requestObj):
    subject = requestObj['subject']
    #print(subject)
    template=""
    if ("place" in subject):
    	template = "Request a CRM account"
    elif ("account" in subject):
    	template = "Request a new email account creation"
    elif ("request for a mail list" in subject):
    	template="Request a new mailing list creation"
    return template
```

En este ejemplo en linea el contenido "place" asigna template = "Request a CRM account"


#h2
ToDO

En proxima version se separar en un json los mapeos de subject => templates
