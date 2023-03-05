from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Firefox
import time
import funcoes
from datetime import datetime, timedelta



def esperar_clicavel(variavel, driver):
    wait = WebDriverWait(driver, 10)  # defino uma variavel com a propriedade de esperar um determinado tempo
    wait.until(EC.element_to_be_clickable((By.ID, variavel)))  # aqui aplico a condição da qual espero

def abrir_filtro(filtro, driver):
    esperar_clicavel("form-filtroAcss-btnOpenDlgPrefs", driver)
    driver.find_element(by=By.ID, value="form-filtroAcss-btnOpenDlgPrefs").click()
    esperar_clicavel(filtro, driver)
    driver.find_element(by=By.ID, value=filtro).click()

def filtro_data(data1, data2, driver):
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-dataId-dataTipo-beginDate").clear()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-dataId-dataTipo-beginDate").click()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-dataId-dataTipo-beginDate").send_keys(data1)
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-dataId-dataTipo-endDate").clear()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-dataId-dataTipo-endDate").click()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-dataId-dataTipo-endDate").send_keys(data2)
    time.sleep(0.6)

def trocar_localidade(localidade, bairro, driver):
    esperar_clicavel("form-filtroAcss-toolbox-btn-search", driver)
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-solicitacaoLocalidadeId-j_idt198-cb-input").clear()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-solicitacaoLocalidadeId-j_idt198-cb-input").click()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-solicitacaoLocalidadeId-j_idt198-cb-input").send_keys(localidade)

    esperar_clicavel("form-filtroAcss-toolbox-btn-search", driver)
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-solicitacaoBairroId-j_idt205-bairro-input").clear()
    time.sleep(1)
    driver.find_element(by=By.ID, value="form-filtroAcss-solicitacaoBairroId-j_idt205-bairro-input").click()
    time.sleep(0.6)
    driver.find_element(by=By.ID, value="form-filtroAcss-solicitacaoBairroId-j_idt205-bairro-input").send_keys(bairro)

def pesq_exp(driver):
    esperar_clicavel("form-filtroAcss-toolbox-btn-search", driver)
    driver.find_element(by=By.ID, value="form-filtroAcss-toolbox-btn-search").click()
    time.sleep(0.5)
    driver.find_element(by=By.ID, value="form-filtroAcss-toolbox-btn-search").click()
    time.sleep(0.5)

    try:
        driver.find_element(by=By.ID, value="form-grid-grid-exportBtn-exportarxls").click()
        time.sleep(1)
    except: print("Planilha extraida com Sucesso!")

# def gerar_datas():
#     data0 = input("Por favor digite o mes/ano desejado(mm/aaaa): ")
#     data0 = data0.split("/")

#     if data0[0] == "01":
#         data = ["26/" + "12/" + str(int(data0[1]) - 1),
#                 "10/" + data0[0] + "/" + str(int(data0[1])),
#                 "11/" + data0[0] + "/" + str(int(data0[1])),
#                 "25/" + data0[0] + "/" + str(int(data0[1]))
#                 ]

#     else:
#         data = ["26/" + str(int(data0[0]) - 1).rjust(2, "0") + "/" + data0[1],
#                 "10/" + data0[0] + "/" + str(int(data0[1])),
#                 "11/" + data0[0] + "/" + str(int(data0[1])),
#                 "25/" + data0[0] + "/" + str(int(data0[1]))
#                 ]
#     return data

# def gerar_datas():
#     data_inicio = input("Por favor digite a data de início (dd/mm/aaaa): ")
#     data_fim = input("Por favor digite a data de fim (dd/mm/aaaa): ")
    
#     data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
#     data_fim = datetime.strptime(data_fim, '%d/%m/%Y')
    
#     datas = []
#     delta = timedelta(days=1)
    
#     while data_inicio <= data_fim:
#         dia = data_inicio.strftime('%d')
#         mes = data_inicio.strftime('%m')
#         ano = data_inicio.strftime('%Y')
#         datas.append(dia + "/" + mes + "/" + ano)
#         data_inicio += delta
    
#     return datas

def gerar_datas(data_inicio_str, data_fim_str):

    formato_data = '%d/%m/%Y'
    data_inicio = datetime.strptime(data_inicio_str, formato_data)
    data_fim = datetime.strptime(data_fim_str, formato_data)
    
    datas = []
    delta = timedelta(days=1)

    while data_inicio <= data_fim:
        datas.append(data_inicio)
        data_inicio += delta

    return datas



def definitiva(filtro, datas):
    # Declaração de Variaveis
    user = "t034183"
    passw = "CNB@2022"

    url = 'http://sciweb.embasanet.ba.gov.br/sci-web/'
    driver = Firefox()
    driver.get(url)

    time.sleep(1)
    # Coletar a informação da tag aleatoria gerada pelo SCI
    randomtag = driver.find_element(by=By.ID, value="random-tag").get_attribute('value')
    driver.find_element(by=By.ID, value="loginForm-usuario-{randomtag}".format(randomtag=randomtag)).send_keys(user)
    driver.find_element(by=By.ID, value="loginForm-senha-{randomtag}".format(randomtag=randomtag)).send_keys(passw)
    driver.find_element(by=By.ID, value="loginForm-submit").click()

    # Neste bloco é feito a seleção de qual tela desejo abrir, no caso é a consulta geral
    driver.find_element(by=By.ID, value="arvoreSearch").send_keys("gera")

    wait = WebDriverWait(driver, 10)  # defino uma variavel com a propriedade de esperar um determinado tempo
    element = wait.until(EC.element_to_be_clickable((By.ID, 'CRSS_anchor')))  # aqui aplico a condição da qual espero

    driver.find_element(by=By.ID, value="CRSS_anchor").click()
    driver.switch_to.frame("frame-content")

    funcoes.abrir_filtro(filtro, driver)

    for i in range(0, len(datas) - 1, 2):
        data_inicio = datas[i].strftime('%d/%m/%Y')
        data_fim = datas[i + 1].strftime('%d/%m/%Y')

        funcoes.filtro_data(data_inicio, data_fim, driver)
        funcoes.trocar_localidade("700", "0", driver)
        funcoes.pesq_exp(driver)

        funcoes.trocar_localidade("900", "22", driver)
        funcoes.pesq_exp(driver)

    # funcoes.filtro_data(data[2], data[3], driver)
    # funcoes.trocar_localidade("700", "0", driver)
    # funcoes.pesq_exp(driver)

    # funcoes.trocar_localidade("900", "22", driver)
    # funcoes.pesq_exp(driver)
    time.sleep(10)


