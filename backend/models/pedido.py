from dataclasses import dataclass, field
from typing import List
from backend.models.informacoes_gerais import InformacoesGerais
from backend.models.custo import Custo
from backend.models.item import Item

@dataclass
class Pedido:
    """Entidade agregadora principal do domínio."""
    informacoes: InformacoesGerais
    custo: Custo
    itens: List[Item] = field(default_factory=list)