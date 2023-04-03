from selenium import webdriver
import requests
import json

# Configuration du driver pour le navigateur 
driver = webdriver.Chrome()

# Test de la méthode GET
response = requests.get('https://reqres.in/api/users?page=2')
if response.status_code == 200:
    
    print("La méthode GET a fonctionné correctement.")
    print("Voici le contenu de la réponse : ")
    json_data = response.json()
    print(json_data)
else:
    print("La méthode GET a échoué.")

# Lecture du contenu du fichier JSON "FileTest.json" 

with open('FileTest.json', 'r') as f:
    expected_data = json.load(f)

# Comparaison des dictionnaires

if json_data == expected_data:
    print('La réponse JSON est identique au contenu du fichier "reponse_attendue.json"')
else:
    print('La réponse JSON est différente du contenu du fichier "reponse_attendue.json"')

# Test de la méthode POST
data = {"name": "Voltaire","job": "Medecin", "id": "44"}
headers = {"Content-Type": "application/json"}
response = requests.post('https://reqres.in/api/users', data=json.dumps(data), headers=headers)
if response.status_code == 201:
    print("La méthode POST a fonctionné correctement.")
else:
    print("La méthode POST a échoué.")

# Test de la méthode DELETE
response = requests.delete('https://reqres.in/api/users/44')
if response.status_code == 204:
    print("La méthode DELETE a fonctionné correctement.")
else:
    print("La méthode DELETE a échoué.")

# Fermeture du navigateur
driver.quit()
