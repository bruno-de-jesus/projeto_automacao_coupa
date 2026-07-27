from dataclasses import dataclass

from models.TipoPedido import TipoPedido

# informações gerais do pedido
@dataclass
class InformacoesGerais:
    solicitante: str
    fornecedor: str
    texto_cabecalho: str
    tipo: TipoPedido
    orcamento: str

    def __post_init__(self):
        self._validar()

    def _validar(self):
        # Campo obrigatório
        if not self.solicitante or not self.solicitante.strip():
            raise ValueError("Solicitante é obrigatório")

        if not self.fornecedor or not self.fornecedor.strip():
            raise ValueError("Fornecedor é obrigatório")

        if not self.texto_cabecalho or not self.texto_cabecalho.strip():
            raise ValueError("Texto do cabeçalho é obrigatório")

        if not isinstance(self.tipo, TipoPedido):
            raise ValueError("Tipo deve ser do tipo TipoPedido")

        if not self.orcamento or not self.orcamento.strip():
            raise ValueError("Pedido de COMPRA deve ter orçamento")