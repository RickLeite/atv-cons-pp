

- `src/componentes/cluster.py`: Implementa a classe `Cluster` que gerencia um grupo de nós.
- `src/componentes/no.py`: Implementa a classe `No` que representa um nó no cluster.
- `src/modelos/estado_no.py`: Define o enum `EstadoNo` que representa os estados de um nó (Seguidor, Candidato, Líder).
- `src/main.py`: Script principal que executa a simulação.

1. **Clone o repositório**

2. **Execute a simulação**:
   ```sh
   python -m src.main
   ```

## Funcionalidades

- **Iniciar Cluster**: Inicia todos os nós no cluster.
- **Parar Cluster**: Para todos os nós no cluster.
- **Obter Líder**: Obtém o nó que é o líder atual do cluster.
- **Simular Falha**: Simula a falha de um nó específico.
- **Recuperar Nó**: Recupera um nó que falhou.
- **Adicionar Dados**: Adiciona dados ao nó líder.

## Exemplo de Uso

```python
from src.componentes.no import No
from src.modelos.estado_no import EstadoNo

def main():
    no1 = No(1, 5)
    no2 = No(2, 5)
    
    print(f"Nó {no1.id} está no estado {no1.estado.value}")
    print(f"Nó {no2.id} está no estado {no2.estado.value}")

if __name__ == "__main__":
    main()
```
