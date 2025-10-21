from django.shortcuts import render

def index(request):
  return render(request, "index.html") # Le decimos que renderice la página index.html

def productos(request):
  return render(request, "productos.html") 

def ofertas(request):
  return render(request, "ofertas.html") 

def contacto(request):
  
  context = {
    "localizacion": {
      "direccion": "Calle Pretzel 45, Málaga, España",
    },

    "contacto": {
      "telefono": "+34 123 123 123",
      "email": "info@dulceenigma.com"
    }
  }
  return render(request, "contacto.html", context=context) 