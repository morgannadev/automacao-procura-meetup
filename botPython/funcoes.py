from botcity.web import WebBot, By
from botcity.maestro import BotMaestroSDK


def fazer_login(bot: WebBot, credencial_email: str, credencial_senha: str):
    campo_email = bot.find_element("email", By.ID)
    campo_email.send_keys(credencial_email)

    campo_senha = bot.find_element("current-password", By.ID)
    campo_senha.send_keys(credencial_senha)


def verificar_distancia(bot: WebBot, distancia_para_evento: int):
    if distancia_para_evento <= 5:
        botao_5_km = bot.find_element("event-distance-2-miles-option", By.ID)
        botao_5_km.click()
    elif distancia_para_evento <= 10:
        botao_10_km = bot.find_element("event-distance-5-miles-option", By.ID)
        botao_10_km.click()
    elif distancia_para_evento <= 25:
        botao_25_km = bot.find_element("event-distance-10-miles-option", By.ID)
        botao_25_km.click()
    elif distancia_para_evento <= 50:
        botao_50_km = bot.find_element("event-distance-25-miles-option", By.ID)
        botao_50_km.click()
    elif distancia_para_evento <= 100:
        botao_100_km = bot.find_element("event-distance-50-miles-option", By.ID)
        botao_100_km.click()
    elif distancia_para_evento <= 150:
        botao_150_km = bot.find_element("event-distance-100-miles-option", By.ID)
        botao_150_km.click()
    else:
        raise Exception("Valor da distância é inválido. Opções: 5, 10, 25, 50, 100, 150 (km).")
    

def procurar_eventos(maestro: BotMaestroSDK, informacoes_evento):
    if informacoes_evento:
        for info in informacoes_evento:
            h3_tag = info.find_element_by_tag_name('h3')
            if h3_tag.text != "SÉRIE DE EVENTOS":
                encontrar_link_evento = info.find_element_by_tag_name('a')
                if encontrar_link_evento:
                    link_evento = encontrar_link_evento.get_attribute('href')
                    print(link_evento)                    

                encontrar_nome_evento = info.find_element_by_tag_name('h2')
                if encontrar_nome_evento:
                    nome_evento = encontrar_nome_evento.text
                    print(nome_evento)

                encontrar_data_evento = info.find_element_by_tag_name('time')
                if encontrar_data_evento:
                    data_evento = encontrar_data_evento.text
                    print(data_evento)

            registrar_log(maestro, nome_evento, data_evento, link_evento)
            
    else:
        raise Exception("Nenhum evento encontrado.")
    

def registrar_log(maestro: BotMaestroSDK, nome_evento, data_evento, link_evento):
    maestro.new_log_entry(
        activity_label="eventos_meetup",
        values={
            "nome":nome_evento,
            "data_evento":data_evento,
            "link":link_evento
        }
    )
