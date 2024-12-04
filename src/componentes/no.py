import threading
import time
import random
import logging
from src.modelos.estado_no import EstadoNo 

class No:
    def __init__(self, id_no, total_nos):
        self.id = id_no
        self.total_nos = total_nos
        self.estado = EstadoNo.SEGUIDOR
        self.termo_atual = 0
        self.votou_para = None
        self.dados = []  # Lista de dados para demonstrar consenso
        self.executando = True
        self.lock = threading.Lock()
        self.logger = logging.getLogger(f"No_{id_no}")

    def iniciar(self):
        self.thread = threading.Thread(target=self._loop_principal)
        self.thread.start()
        self.logger.info(f"Nó {self.id} iniciado como {self.estado.value}")

    def parar(self):
        self.executando = False
        if self.thread:
            self.thread.join()
        self.logger.info(f"Nó {self.id} parado")

    def adicionar_dado(self, dado):
        if self.estado == EstadoNo.LIDER:
            self.dados.append(dado)
            return True
        return False

    def _loop_principal(self):
        while self.executando:
            if self.estado == EstadoNo.SEGUIDOR:
                if random.random() < 0.1:  # 10% chance
                    self._iniciar_eleicao()
            elif self.estado == EstadoNo.LIDER:
                self._enviar_heartbeat()
            time.sleep(1)

    def _iniciar_eleicao(self):
        with self.lock:
            self.estado = EstadoNo.CANDIDATO
            self.termo_atual += 1
            votos = 1  # Vota em si mesmo
            
            for _ in range(self.total_nos - 1):
                if random.random() < 0.7:  # 70% chance de receber voto
                    votos += 1

            if votos > self.total_nos / 2:
                self.estado = EstadoNo.LIDER
                self.logger.info(f"Nó {self.id} eleito líder no termo {self.termo_atual}")
            else:
                self.estado = EstadoNo.SEGUIDOR
                self.logger.info(f"Nó {self.id} voltou a seguidor após eleição falhar")

    def _enviar_heartbeat(self):
        self.logger.debug(f"Líder {self.id} enviando heartbeat")