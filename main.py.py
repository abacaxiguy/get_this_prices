"""
Pegar os preços do sites
colocar eles numa planilha
"""

import requests
from bs4 import BeautifulSoup
from time import sleep

urls = ['https://www.kabum.com.br/produto/107545/processador-amd-ryzen-5-1600-cache-19mb-3-2ghz-3-6ghz-max-turbo-am4-yd1600bbafbox',
        'https://www.kabum.com.br/produto/95677/placa-mae-asus-ex-a320m-gaming-amd-am4-matx-ddr4',
        'https://www.kabum.com.br/produto/84108/hd-seagate-barracuda-1tb-3-5-sata-st1000dm010?',
        'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=103547',
        'https://www.kabum.com.br/produto/91021/fonte-corsair-450w-80-plus-bronze-cx450-cp-9020120-br',
        'https://www.kabum.com.br/produto/99927/gabinete-gamer-nox-hummer-tgm-rgb-rainbow-4-coolers-lateral-e-frontal-em-vidro-nxhummertgm',
        ]
for url in urls:
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    print(html.select_one('.preco_desconto').text)
    print(html.select_one('.preco_normal').text)
    sleep(1)