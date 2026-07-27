from dataclasses import dataclass, field
from typing import List

# classe principal
@dataclass
class Pedido:
    informacoes: InformacoesGerais
    faturamento: Faturamento
    itens: List(Item) = field(default_factory=list)