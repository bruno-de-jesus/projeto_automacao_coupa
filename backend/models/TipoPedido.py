from enum import Enum, auto

# definição de tipos de pedidos com enum
class TipoPedido(Enum):
    MATERIAL = auto()
    SERVICO = auto()