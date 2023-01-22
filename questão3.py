#questão 3.
# Na programação é comum relacionar dados usando um campo que identifica
#registros (id). Elabore uma modelagem de dados em que os registros estão
#relacionados através de um campo identificador (o id), atendendo as seguintes
#afirmações:
#○ O bairro Betânia é da cidade Diamantina.
#○ Os bairros Agostinho e Natal são da cidade Noronha.
#○ A cidade Diamantina é do estado Goiás.
#○ A cidade Noronha é do estado Paraná.
#Siga o exemplo desta outra modelagem já implementada:
#○ Afirmações:
#■ O produto Frango é da empresa Açougue.
#■ O produto Pão é da empresa Padaria.
#■ O produto Leite é da empresa Padaria.
#○ Modelagem resultante (os ids foram gerados aleatoriamente):
#empresas = [{id:44, nome:’Açougue’},
#{id:71, nome:’Padaria’}]
#produtos = [{id:83, nome:’Pão’, empresa_id:71},
#{id:84, nome:’Leite’, empresa_id:71},
#{id:85, nome:’Frango’, empresa_id:44}]


bairro = [
    {'id': 0, 'local': 'Betânia', 'cidade_id': 0},
    {'id': 1, 'local': 'Agostinho', 'cidade_id': 1},
    {'id': 2, 'local': 'Natal', 'cidade_id': 1}
]

cidade = [
    {'id': 0, 'local': 'Diamantina', 'estado_id': 0},
    {'id': 1, 'local': 'Noronha', 'estado_id': 1}
]

estado = [
    {'id': 0, 'local': 'Goiás'},
    {'id': 1, 'local': 'Paraná'}
]

#goiás - diamantina - betânia
#paraná - noronha - agostinho - natal