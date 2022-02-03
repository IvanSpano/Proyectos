from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#primera parte del ejercicio 2
def aeropuertos(request):
    f = open("aeropuertos.csv",encoding="utf8")
    html = """
        <html>
        <title>Lista de aeropuertos</title>
        <table style="border: 1px solid">
            <thead>
                <tr>
                    <th>Aeropuerto</th>
                    <th>Ciudad</th>
                    <th>Pais</th>
                </tr>
            </thead>   
    """
    for linea in f:
        datos = linea.split(",") #separa el texto de acuerdo al parametro split
        nombre = datos[1].replace('"',"")
        ciudad = datos[2].replace('"',"")
        pais = datos[3].replace('"',"")
        html += f"""
            <tr>
                <td>{nombre}</td>
                <td>{ciudad}</td>
                <td>{pais}</td>
            <tr>
        """
        f.close()
        html += "</table></html>"
        return HttpResponse(html)