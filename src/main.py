import logging
import time
from src.componentes.cluster import Cluster 

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger("Main")

    cluster = Cluster(5)
    logger.info("Iniciando simulação do Raft...")

    try:
        cluster.iniciar_cluster()
        time.sleep(2)

        lider = cluster.obter_lider()
        if lider:
            logger.info(f"Líder inicial: Nó {lider.id}")
            cluster.adicionar_dados("Dado 1")
            cluster.adicionar_dados("Dado 2")

        if lider:
            logger.info(f"Simulando falha do líder (Nó {lider.id})")
            cluster.simular_falha_no(lider.id)
            time.sleep(3)

            novo_lider = cluster.obter_lider()
            if novo_lider:
                logger.info(f"Novo líder eleito: Nó {novo_lider.id}")
                cluster.adicionar_dados("Dado 3")

            logger.info(f"Recuperando nó {lider.id}")
            cluster.recuperar_no(lider.id)

        time.sleep(2)
        logger.info("Simulação concluída")

    except KeyboardInterrupt:
        logger.info("Encerrando simulação...")
    finally:
        cluster.parar_cluster()

if __name__ == "__main__":
    main()