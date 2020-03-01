def greet():
  print("Ingresa el dinero inicial a depositar")
  dinero=int(input())
  print("Ingrese la tasa de interes mensual en % (si es 1% debera ingresar 1)")
  tasa=int(input())
  print("Ingrese el numero de meses del deposito")
  meses=int(input())
  print("Despues de ",meses," a usted se le devolvera ",dinero*(1+tasa/100)**meses,"pesos")
