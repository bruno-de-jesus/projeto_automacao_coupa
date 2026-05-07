from dataclasses import dataclass, field
from typing import Optional

from models.TipoPedido import TipoPedido

# informações gerais do pedido
@dataclass
class InformacoesGerais:
    solicitante: str
    fornecedor: str
    texto_cabecalho: str
    tipo: TipoPedido
    orcamento: Optional[str] = None
