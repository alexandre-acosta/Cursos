def verificar_hashes(lista_hashes):
    
    for hash_comparacao in lista_hashes:
        
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        if hash_calculado.strip() == hash_esperado.strip():
            print("Correto")
        else:
            print("Inválido")
            
# Captura de entrada do usuário
hashes_usuario = input()

# Dividir os pares de hashes usando o delimitador ";"
lista_hashes = hashes_usuario.split(";")

# Chamada da função para verificar os hashes
verificar_hashes(lista_hashes)