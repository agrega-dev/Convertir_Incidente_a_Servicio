import requests
import sys
import json
import os

headers = {"technician_key":"1996B81F-C8A0-4C7A-8EE8-9EFFD7FEEBF5"}
app_url = 'http://localhost:8085'

#funciona para borrado de ticket
def borrado(request_id):
    endpoint = '/api/v3/requests'
    url = app_url + '/api/v3/requests/'+ request_id + '/move_to_trash'
    response = requests.delete(url,headers=headers,verify=False)
    return
#funcion para crear ticket
def creacion(input_data,headers,app_url):
    endpoint = '/api/v3/requests'
    url = app_url + endpoint
    data = {'input_data': input_data}
    response = requests.post(url,headers=headers,data=data,verify=False)
#lectura de json
def lectura():
    #procesamiento de archivo
    file_path = sys.argv[1]
    #para realizar pruebas locales
    #file_path = os.getcwd()+"/Salida.json"
    requestObj = read_file(file_path,"request")
    #print(requestObj)
    return requestObj
def read_file(file_Path, key=None):
    with open(file_Path,encoding='utf-8') as data_file:
        data = json.load(data_file)
    if key is None:
        return data
    elif key in data:
        dataObj = data[key]
        return dataObj
    else:
        return None
def construyejson(data):
    json_data = ''' {"request": ''' + data + '''}'''
    return json_data
#funcion para construir la data de nuevo ticket
def construyedata(template,requestObj):
    reqObj={}
    reqObj['requester']=requestObj['requester']
    reqObj['subject']=requestObj['subject']
    reqObj['template']={}
    reqObj['template']['name']=template
    reqObj['description']=requestObj['description']

    reqObj = json.dumps(reqObj)
    json_data = construyejson(reqObj)
    print(json_data)
    return json_data
#funcion para asociar subject con template en catalogo de servicio
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

if __name__ == '__main__':
    requestObj=lectura()
    template_name=template(requestObj)
    dataObj=construyedata(template_name,requestObj)
    request_delete=requestObj['id']
    print('fin')
