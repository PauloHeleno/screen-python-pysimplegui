import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkTeal3')
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0), key ='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0), key = 'idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key = 'Gmail'), sg.Checkbox('Outlook', key = 'Outlook'), sg.Checkbox('Yahoo', key = 'Yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartões', key = 'aceitaCartao'),sg.Radio('Não', 'cartões', key = 'naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar dados')],
            [sg.Output(size = (30,20))]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        
        
    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_Gmail = self.values['Gmail']
            aceita_Outlook = self.values['Outlook']
            aceita_Yahoo = self.values['Yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_Gmail}')
            print(f'aceita outlook: {aceita_Outlook}')
            print(f'aceita yahoo: {aceita_Yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'nao aceita cartão: {nao_aceita_cartao}')
            print(f'velocidade scriptis: {velocidade_script}')
            
tela = TelaPython()
tela.Iniciar()
        
    
