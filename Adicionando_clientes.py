# Dicionário para armazenar os clientes
customers = {}

# Função para adicionar um cliente ao dicionário "clientes"
def add_customer(cpf, name, age, city):
    customers[cpf] = {
        "name": name,
        "age": age,
        "city": city
    }

cpf = input()
name = input()
age = input()
city = input()

add_customer(cpf, name, age, city)

print("Customer Registered!")
print("Document:", cpf)
print("Name:", customers[cpf]["name"])
print("Age:", customers[cpf]["age"])
print("City:", customers[cpf]["city"])


