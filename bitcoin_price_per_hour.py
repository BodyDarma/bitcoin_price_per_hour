import requests
import time

def buscar_preco_criptomoeda(criptomoeda='bitcoin'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={criptomoeda}&vs_currencies=usd,brl'
    try:
        response = requests.get(url)
        data = response.json()
        return data[criptomoeda]['usd'], data[criptomoeda]['brl']  # Retorna dois valores agora
    except Exception as e:
        print(f"Erro ao buscar o preço: {e}")
        return None, None


def monitorar_preco(criptomoeda='bitcoin', intervalo=3600):
    print(f"Monitorando o preço do {criptomoeda.capitalize()}. Atualizações a cada hora ou {intervalo} segundos.")
    preco_usd_anterior, preco_brl_anterior = buscar_preco_criptomoeda(criptomoeda)
    
    while True:
        preco_usd_atual, preco_brl_atual = buscar_preco_criptomoeda(criptomoeda)
        if preco_usd_atual != preco_usd_anterior or preco_brl_atual != preco_brl_anterior:
            print(f"Alerta de preço! O preço do {criptomoeda.capitalize()} mudou para: ${preco_usd_atual} USD / R${preco_brl_atual} BRL")
            preco_usd_anterior, preco_brl_anterior = preco_usd_atual, preco_brl_atual
        else:
            print(f"Sem mudanças. O preço do {criptomoeda.capitalize()} permanece: ${preco_usd_atual} USD / R${preco_brl_atual} BRL")
        time.sleep(intervalo)


monitorar_preco('bitcoin', 3600)

