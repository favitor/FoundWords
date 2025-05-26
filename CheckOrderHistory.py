import json
from datetime import datetime


#vars
orderhistory_file = "./orderhistory.json"
today_str = datetime.now().date().strftime("%d/%m/%Y")
today_date= datetime.strptime(today_str, "%d/%m/%Y").date()


###Função checar normalidade dos pedidos
def check_orders(json_file):
    with open(json_file, 'r') as file:
        orders_data = json.load(file)
    
    orders_with_null = {}
    for i, pedido in enumerate(orders_data["pedidos"]):
        campos_vazios_ou_nulos = [field for field, value in pedido.items() if value in (None, '', [], {})]
        if campos_vazios_ou_nulos:
            orders_with_null[f"Pedido {i+1}"] = campos_vazios_ou_nulos
    
    '''if orders_with_null:
        print("Os seguintes pedidos têm campos vazios ou nulos:")
        for pedido, campos in orders_with_null.items():
            print(f"{pedido}: {campos}")
    else:
        print("Não há campos vazios ou nulos nos pedidos.")'''
    
    return orders_with_null

# Exemplo de uso:
pedidos_com_faltas = check_orders('./orderhistory.json')


####Checando previsão de entrega
def late_orders(json_file):
    with open(json_file, 'r') as file:
        prev_data = json.load(file)

    results = []   
    for pedido in prev_data["pedidos"]:
        previsao_entrega_date = datetime.strptime(pedido["previsao_entrega"], "%d/%m/%Y").date()

        if previsao_entrega_date < today_date and pedido["status"] == "Em transporte":
            results.append(pedido)

    return results




teste_datas = late_orders('./orderhistory.json')
print(teste_datas)