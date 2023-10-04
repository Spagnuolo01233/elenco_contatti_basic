class Contatto:
    def __init__(self, nome:str , telefono:int , mail:str):
        self.nome = nome
        self.telefono = telefono
        self.mail = mail

class Elenco_contatti:
    def __init__(self):
       self.contatti = []

    '''def troppo macchinosa come funzionamento.'''
    # def aggiungi_contatto(self,nome,telefono,mail):
    #   contatto = Contatto(nome,telefono,mail)
    #   self.contatti.append(contatto)

    def aggiungi_contatto(self,contatto):
        self.contatti.append(contatto)

    @property
    def visualizza_contatti(self):
        for contatto in self.contatti:
            print(f' Nome: {contatto.nome}\n Telefono: {contatto.telefono}\n Mail: {contatto.mail}\n')

    
    def cancella_contatto(self,contatto):
        contatto_da_cancellare = contatto
        trovato = False

        for contatto in self.contatti:
            if contatto == contatto_da_cancellare:
                self.contatti.remove(contatto)
                print(f'\nIl contatto {contatto.nome} è stato rimosso.\n')
                trovato = True
                break
     
        if not trovato:
                print(f'Il contatto {contatto_da_cancellare.nome} non esiste nella lista.\n')




