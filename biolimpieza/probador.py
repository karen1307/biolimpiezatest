import datetime
import calendar
import json

'''hoy = datetime.datetime.now()
ultimo = calendar.monthrange(hoy.year, hoy.month)[1]
ultimoSiguiente = calendar.monthrange(hoy.year+1, 1)

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    days = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
    dayDescriptive = days[date.strftime("%A")]
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} {} de {} del {}".format(dayDescriptive, day, month, year)

    return messsage

now = datetime.datetime.now()
print(current_date_format(now))
print(ultimo)
print(ultimoSiguiente)'''

'''ruta = "biolimpieza/static/Json/colaboradoras.json"
file = open(ruta, "r")
colaboradoras_json =  json.load(file)
file.close

print(colaboradoras_json["CLB001"]["nombres"])

for colaboradora in colaboradoras_json:
    print(colaboradoras_json[colaboradora]["nombres"])'''

'''serial_number = '48374983274832'
print(serial_number)
print(serial_number.strip())'''

'''import holidays_co
holidays = holidays_co.get_colombia_holidays_by_year(2023)
print(holidays)'''

#usuario = models.Cliente.objects.get(id=1)
#usuarios = models.Cliente.objects.all()
#print (models.Cliente)
#usuario.delete()

'''fecha_vencimiento = datetime.datetime.now() + datetime.timedelta(15)
print(fecha_vencimiento)'''

print(datetime.datetime.now().date())