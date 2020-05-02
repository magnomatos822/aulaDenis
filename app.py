class OlaDenis():
    
    momentoDia = "" 
    
    def saudacao(self, momentoDia):
        self.momentoDia = momentoDia

    def dia(self):
        return self.momentoDia

OlaDenis.saudacao('Noite')