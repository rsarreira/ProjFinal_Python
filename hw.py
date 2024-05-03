from tickets import Tickets

class HW(Tickets):
    def __init__(self, *args):
        super().__init__()
        self.equipamento = None
        self.avaria = None

        if len(args) == 1 and isinstance(args[0] , HW):
            super().__init__(args[0])
            self.equipamento = args[0].equipamento
            self.avaria = args[0].avaria
        
        elif len(args) == 4:
            super().__init__(args[0] , args[1])
            self.equipamento = args[2]
            self.avaria = args[3]
            