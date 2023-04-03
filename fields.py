balancete = {
    'Ativo': {
        'Circulante': {
            'Caixa e equivalentes de caixa': [],
            'Aplicações financeiras': [],
            'Contas a receber': [],
            'Estoques': [],
            'Despesas antecipadas': [],
            'Outros ativos circulantes': []
        },
        'Realizável a longo prazo': {
            'Contas a receber': [],
            'Aplicações financeiras': [],
            'Investimentos': [],
            'Imobilizado': [],
            'Intangível': [],
            'Outros ativos realizáveis a longo prazo': []
        },
        'Investimentos': {
            'Participações em coligadas e controladas': [],
            'Investimentos em outras empresas': [],
            'Imobilizado': [],
            'Intangível': []
        },
        'Imobilizado': {
            'Tangível': {
                'Terrenos': [],
                'Construções': [],
                'Máquinas e equipamentos': [],
                'Instalações': [],
                'Veículos': [],
                'Outros bens tangíveis': []
            },
            'Intangível': {
                'Marcas e patentes': [],
                'Software': [],
                'Direitos autorais': [],
                'Outros bens intangíveis': []
            },
            'Investimentos': {
                'Participações em coligadas e controladas': [],
                'Investimentos em outras empresas': []
            }
        },
        'Intangível': {
            'Marcas e patentes': [],
            'Software': [],
            'Direitos autorais': [],
            'Outros ativos intangíveis': []
        }
    },
    'Passivo': {
        'Circulante': {
            'Fornecedores': [],
            'Empréstimos e financiamentos': [],
            'Obrigações fiscais': [],
            'Salários e encargos sociais': [],
            'Obrigações trabalhistas': [],
            'Outros passivos circulantes': []
        },
        'Exigível a longo prazo': {
            'Empréstimos e financiamentos': [],
            'Impostos e contribuições': [],
            'Obrigações trabalhistas': [],
            'Outros passivos exigíveis a longo prazo': []
        }
    },
    'Patrimônio Líquido': {
        'Capital Social': [],
        'Reservas de Capital': [],
        'Ajustes de Avaliação Patrimonial': [],
        'Reservas de Lucros': {
            'Reservas estatutárias': [],
            'Reservas de incentivos fiscais': [],
            'Reservas de retenção de lucros': [],
            'Lucros ou prejuízos acumulados': []
        }
    },
    'Receitas': {
        'Vendas de produtos': [],
        'Vendas de serviços': [],
        'Outras receitas': []
    },
    'Despesas': {
        'Custos dos produtos vendidos': [],
        'Custos dos serviços prestados': [],
        'Despesas operacionais': {
            'Comerciais': [],
            'Administrativas': [],
            'Financeiras': []
        }
    }
}

dre = {
    'Receita': ['Vendas', 'Serviços', 'Outros'],
    'Deduções': ['Devoluções', 'Impostos'],
    'Custo': ['Matéria-prima', 'Mão-de-obra', 'Custos indiretos', 'Depreciação'],
    'Despesas Operacionais': ['Comerciais', 'Administrativas', 'Financeiras'],
    'Resultado da Equivalência Patrimonial': ['Receitas', 'Despesas'],
    'Resultado Financeiro': ['Juros de empréstimos', 'Receitas financeiras', 'Despesas financeiras'],
    'Resultado Antes do Imposto de Renda': ['Receitas', 'Custos', 'Despesas', 'Resultado da Equivalência Patrimonial', 'Resultado Financeiro'],
    'Provisão para o Imposto de Renda': ['Imposto de Renda', 'Contribuição Social sobre o Lucro'],
    'Impostos e Contribuições': ['PIS', 'COFINS', 'ICMS', 'IPI'],
    'Resultado Líquido das Operações Continuadas': [],
    'Resultado Líquido das Operações Descontinuadas': [],
    'Lucro ou Prejuízo Líquido do Exercício': [],
    'EBITDA': ['Lucro líquido', 'Depreciação', 'Amortização']
}

aleatorio = [
    'contrato', 'assinatura', 'procuração', 'declaração', 'protocolo', 
    'comunicado', 'protocolo', 'requerimento', 'solicitação', 'autorização',
    'documento', 'apresentação', 'comprovante', 'identidade', 'passaporte', 
    'visto', 'carteira', 'trabalho', 'diploma', 'certidão',
    'informação', 'atendimento', 'serviço', 'dúvida', 'orientação',
    'despacho', 'arquivamento', 'prorrogação', 'renovação', 'convocação',
    'recurso', 'procedimento', 'administrativo', 'juntada', 'remessa',
    'resposta', 'ofício', 'memorando', 'comunicado', 'aviso',
    'trâmite', 'processual', 'contencioso', 'instrução', 'processo',
    'jurídico', 'judicial', 'audiência', 'testemunho', 'acordo',
    'interrogatório', 'intimação', 'protesto', 'reclamação', 'notificação',
    'embargos', 'apelação', 'agravo', 'instrumento', 'recurso',
    'extrajudicial', 'cartório', 'certificação', 'autenticação', 'protesto',
    'tabelião', 'escrevente', 'registro', 'averbação', 'procuração',
    'escritura', 'reconhecimento', 'assinatura', 'transcrição', 'transferência',
    'contrato', 'arrendamento', 'locação', 'compra', 'venda',
    'pagamento', 'parcelamento', 'financiamento', 'apólice', 'seguro',
    'cobrança', 'indicação', 'indisponibilidade', 'oneração', 'penhora',
    'execução', 'liquidação', 'termo', 'recebimento', 'entrega',
    'extravio', 'perda', 'roubo', 'furto', 'indenização',
    'responsabilidade', 'civil', 'processo', 'administrativo', 'improbidade',
    'conduta', 'falta', 'ética', 'processo', 'disciplinar',
    'sindicância', 'correição', 'acesso', 'informação', 'transparência',
    'ouvidoria', 'atendimento', 'defensoria', 'advocacia', 'judiciária',
    'consultoria', 'jurídica', 'procuradoria', 'fazenda', 'nacional',
    'estadual', 'municipal', 'comissão', 'processante', 'perícia'
]
