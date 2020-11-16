 #-*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
import MySQLdb


class RocaSpider(scrapy.Spider):
    name = 'roca'
    allowed_domains = ['roca.com.br']
    start_urls = ['https://www.roca.com.br/indice/imoveis/residenciais/locacao/apartamento/todos/todos']

    

    def parse(self, response):
        site = response.text
        bairro = Selector(text=site).xpath("//h2/a/text()").getall()
        endereco = Selector(text=site).xpath("//h3/text()").getall()
        valor = Selector(text=site).xpath("//div[1]/h4/text()").getall()
        area = Selector(text=site).xpath("//div/div/div/div/div/div/div/div/div/div[1]/text()").getall()
        quarto = Selector(text=site).xpath("//div/div/div/div/div/div/div/div/div/div[2]/text()").getall()
        banheiro = Selector(text=site).xpath("//div/div/div/div/div/div/div/div/div/div[3]/text()").getall() 
        vaga = Selector(text=site).xpath("//div/div/div/div/div/div/div/div/div/div[4]/text()").getall()   
        #idimovel = Selector(text=site).xpath("//div/div/div/div/div/div/div/div/div/div/a/@id").getall()
        
        #variaveis de tratamento da variavel bairro
        bairro_String = '-'.join(bairro)  # transforma em string
        bairro_RemoveTraco = bairro_String.split('-') # separa por - 
        bairro_SeparaPorVirgula = ','.join(bairro_RemoveTraco) # transforma em string colocando virgula em cada um
        bairro_RetiraN = bairro_SeparaPorVirgula.replace("\n","") #substitui/remove \n por nada
        bairro_RetiraTipo = bairro_RetiraN.replace("Apartamento","") #remove apartamento
        bairro_RemoveTab = bairro_RetiraTipo.replace("        ", "")#substitui/remove tabulação
        bairro_RemoveSpa = bairro_RemoveTab.replace("  ", "")#substitui/remove espaços
        bairro_AcertaVirgula = bairro_RemoveSpa.replace(", ","") #tira as virgulas desnecesárias
        bairro_CriaList = bairro_AcertaVirgula.split(',') # transforma em lista novamente
        bairro_Tratado = bairro_CriaList # resultado da tipo tratado

        #variaveis de tratamento da variavel endereco
        endereco_String = ','.join(endereco) # transforma em string
        endereco_RetiraN = endereco_String.replace("\n","") #substitui/remove \n por nada
        endereco_RemoveTab = endereco_RetiraN.replace("        ", "")#substitui/remove tabulação
        endereco_RemoveSpa = endereco_RemoveTab.replace("  ", "")#substitui/remove espaços
        endereco_CriaList = endereco_RemoveSpa.split(',')# transforma em lista novamente
        endereco_Tratado = endereco_CriaList

        #variaveis de tratamento da variavel valor
        valor_String = ','.join(valor)# transforma em string
        valor_RetiraN = valor_String.replace("\n","") #substitui/remove \n por nada
        valor_RemovePonto = valor_RetiraN.replace(".","")
        valor_RemoveSpa = valor_RemovePonto.replace("        ", "")#substitui/remove tabulação
        valor_ConfiguraDecimal = valor_RemoveSpa.replace(",0", ".0")#substitui virgula por ponto
        valor_RetiraMoeda = valor_ConfiguraDecimal.replace("R$","")#tira o sifrão
        valor_RemoveSpa = valor_RetiraMoeda.replace("  ", "")#substitui/remove espaços
        valor_CriaList = valor_RemoveSpa.split(',')# transforma em lista novamente
        valor_Tratado = valor_CriaList

        #variaveis de tratamento da variavel area
        area_String = ','.join(area)# transforma em string
        area_SeparaNum = re.sub('[^0-9]', ' ', area_String)
        area_RemoveTab = area_SeparaNum.replace("        ", "")#substitui/remove tabulação
        area_RemoveSpa = re.sub(r'\s+',',',area_RemoveTab)#substitui/remove espaços
        area_AcertaPontuacao = area_RemoveSpa.rstrip(',')#tira a ultima virgula
        area_CriaList = area_AcertaPontuacao.split(',')# transforma em lista novamente
        area_Tratado = area_CriaList

        #variaveis de tratamento da variavel quarto
        quarto_String = ','.join(quarto)# transforma em string
        quarto_SeparaNum =re.sub('[^0-9]', ' ', quarto_String)#substitui/remove \n por nada
        quarto_RemoveTab = quarto_SeparaNum.replace("      ", "")#substitui/remove tabulação
        quarto_RemoveSpa =re.sub(r'\s+',',',quarto_RemoveTab)#substitui/remove espaços
        quarto_RemoveVirgulaExtra = quarto_RemoveSpa.strip(',')
        quarto_CriaList = quarto_RemoveVirgulaExtra.split(',')# transforma em lista novament
        quarto_Tratado = quarto_CriaList

        #variaveis de tratamento da variavel banheiro
        banheiro_String = ','.join(banheiro) #transforma em strigs
        banheiro_SeparaNum =re.sub('[^0-9]', ' ', banheiro_String)#romeve banheiros 
        banheiro_RemoveTab = banheiro_SeparaNum.replace("        ", "")# tira as espaços extras
        banheiro_RemoveSpa =re.sub(r'\s+',',',banheiro_RemoveTab)
        banheiro_RemoveVirgulaExtra =banheiro_RemoveSpa.strip(',')#tira a primeira virgula
        banheiro_CriaList = banheiro_RemoveVirgulaExtra.split(',')# transforma em lista novament
        banheiro_Tratado = banheiro_CriaList

        #variaveis de tratamento da variavel vaga_
        vaga_String = ','.join(vaga)#transforma em string
        vaga_SeparaNum = re.sub('[^0-9]', ' ', vaga_String)#remove garagens
        vaga_RemoveTab = vaga_SeparaNum.replace("        ", "")# remove tabulação
        vaga_RemoveSpa =re.sub(r'\s+',',',vaga_RemoveTab)#substitui/remove espaços
        vaga_RemoveVirgulaExtra = vaga_RemoveSpa.strip(',')
        vaga_CriaList = vaga_RemoveVirgulaExtra.split(',')
        vaga_Tratado = vaga_CriaList

        # id_Imovel = '-'.join(idimovel)
        # id_SeparaNumeros = re.sub('[^0-9]', ' ', id_Imovel)
        # id_RemoveTab = id_SeparaNumeros.replace("        ", ",")
        # id_RemoveSpa = id_RemoveTab.replace("  ", "")
        # id_RemoveSpaA = id_RemoveSpa.replace(" ","")
        # id_CriaList = id_RemoveSpaA.split(',')
        # id_Tratado= id_CriaList

        row_data=zip(bairro_Tratado,endereco_Tratado,valor_Tratado,area_Tratado,quarto_Tratado,banheiro_Tratado,vaga_Tratado)
        con = MySQLdb.connect('localhost', 'root', '4991')
        con.select_db('imobiliaria')
        cursor = con.cursor() 

        insert = (
                'INSERT INTO apartamento(bairroBD, enderecoBD, valorBD, areaBD, quartoBD,banheiroBD,vagaBD ) VALUES (%s,%s, %s, %s, %s,%s,%s);'
            )

        for item in row_data:
            data = (
                (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
            )
            cursor.execute(insert, data)
            

        con.commit()
        con.close()

        proximaPagina = Selector(text=site).xpath("//div/nav/ul/li/a/@href").getall()
        for i in proximaPagina:
            next_page = i
            if next_page:
                yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse)