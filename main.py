#Remover chave em um dicionário

pessoa = {
'Nome':'Marcos Veras',
'Idade':39,
'Profissao':'Programador',
'Empresa' :'SENAI',
'Genero':'Masculino'
}

#Remover chave
del pessoa[input('Informe a chave que deseja excluir: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
           
