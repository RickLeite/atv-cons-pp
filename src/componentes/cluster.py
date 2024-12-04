import time
import logging
from src.modelos.estado_no import EstadoNo 
from src.componentes.no import No 

class Cluster:
    def __init__(self, num_nos):
        self.nos = []
        for i in range(num_nos):
            no = No(i, num_nos)
            self.nos.append(no)
        self.logger = logging.getLogger("Cluster")

    def iniciar_cluster(self):
        for no in self.nos:
            no.iniciar()
            time.sleep(0.5)

    def parar_cluster(self):
        for no in self.nos:
            no.parar()

    def obter_lider(self):
        lideres = [no for no in self.nos if no.estado == EstadoNo.LIDER]
        return lideres[0] if lideres else None

    def simular_falha_no(self, id_no):
        if 0 <= id_no < len(self.nos):
            self.logger.info(f"Simulando falha no nó {id_no}")
            self.nos[id_no].parar()

    def recuperar_no(self, id_no):
        if 0 <= id_no < len(self.nos):
            self.logger.info(f"Recuperando nó {id_no}")
            self.nos[id_no].iniciar()

    def adicionar_dados(self, dados):
        lider = self.obter_lider()
        if lider:
            return lider.adicionar_dado(dados)
        return False
