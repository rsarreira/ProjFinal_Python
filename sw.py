from tickets import Tickets


class SW(Tickets):

    """
            Inicializar um objeto da classe SW.

            Args:
                *args: Argumentos variáveis para inicializar o objeto.

            Note:
                Se um único argumento do tipo SW for fornecido, os dados desse ticket serão copiados para o novo objeto SW.
                Se três argumentos forem fornecidos, eles devem ser, respectivamente, idColab, software e necessidade.
                Se quatro argumentos forem fornecidos, eles devem ser, respectivamente, idColab, tipoTicket, software e necessidade.
    """
    def __init__(self, *args):
        super().__init__()
        self.software = None
        self.necessidade = None

        if len(args) == 1 and isinstance(args[0] , SW):
            super().__init__(args[0])
            self.software = args[0].software
            self.necessidade = args[0].necessidade

        elif len(args) == 3:
            super().__init__(args[0])            
            self.software = args[1]
            self.necessidade = args[2]
        
        elif len(args) == 4:
            super().__init__(args[0] , args[1])            
            self.software = args[2]
            self.necessidade = args[3]