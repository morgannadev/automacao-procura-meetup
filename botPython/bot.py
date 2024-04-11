# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from funcoes import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    # busca as credenciais
    credencial_email = maestro.get_credential(label="login_meetup", key="email")
    credencial_senha = maestro.get_credential(label="login_meetup", key="senha")

    # busca o parâmetro de pesquisa
    evento_para_pesquisar = execution.parameters.get("evento_para_pesquisar")
    local_para_evento = execution.parameters.get("local_para_evento")
    distancia_para_evento = execution.parameters.get("distancia_para_evento")  

    bot = WebBot()

    # significa que vamos visualizar a execução, não será em background
    bot.headless = False

    # vamos utilizar o firefox como browser
    bot.browser = Browser.FIREFOX

    # informa o caminho do webdriver
    bot.driver_path = r"resources\geckodriver.exe"

    try:
        # abre o site do meetup
        bot.browse("https://www.meetup.com/")

        # encontra o login para clicar
        botao_entrar = bot.find_element("login-link", By.ID)
        botao_entrar.click()

        # aguarda 1 segundo
        bot.wait(1000)

        fazer_login(bot, credencial_email, credencial_senha)

        bot.enter()

        bot.wait(3000)

        # informa o evento que vai pesquisar
        campo_pesquisa = bot.find_element("keyword-bar-in-search", By.ID)
        campo_pesquisa.send_keys(evento_para_pesquisar)

        # damos o tab para mudar para o campo de local
        bot.tab()

        # seleciona o conteúdo que estiver para poder digitar em cima o valor recebido
        bot.control_a()

        bot.type_keys(local_para_evento)
        bot.wait(2000)

        # seta para baixo para selecionar a primeira opção
        bot.type_down()    
        bot.enter()

        bot.wait(2000)

        botao_distancia = bot.find_element("event-distance-filter-drop-down", By.ID)
        botao_distancia.click()

        verificar_distancia(bot, int(distancia_para_evento))

        informacoes_evento = bot.find_elements('//div[@class="w-full overflow-hidden"]', By.XPATH)

        procurar_eventos(maestro, informacoes_evento)

        status = AutomationTaskFinishStatus.SUCCESS
        mensagem = "Busca de eventos finalizada com sucesso"

    except Exception as erro:
        status = AutomationTaskFinishStatus.FAILED
        mensagem = "Busca de eventos finalizada com erro"

        bot.screenshot("erro.png")

        maestro.error(
            task_id=maestro.task_id, 
            exception=erro,
            screenshot="erro.png"
        )

    finally:
        # fecha o browser
        bot.stop_browser()

        maestro.finish_task(
            task_id=execution.task_id,
            status=status,
            message=mensagem
        )    


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
