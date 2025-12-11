from hashlib import sha256
from math import ceil

class tabela_hash:
    class __Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor
        
        def __str__(self):
            return f'{self.chave}: {self.valor}'
        
        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self.__capacidade_atual = 5 
        self.__tabela_interna =  [[] for _ in range(self.__capacidade_atual)]
        self.__tamanho = 0

        self.__limiar_expandir = 0.75
        self.__fator_expansao = 2
        self.__limiar_reduzir = 0.20
        self.__fator_reducao = 0.5

    def __str__(self):
        retorno = '{'
        total= len(self)
        i = 0
        for k, v  in self:
            if isinstance(k, str):
                retorno += f"'{k}': "
            else:
                retorno += f'{k}: '

            if isinstance(v, str):
                retorno += f"'{v}'"
            else:
                retorno += f'{v}'

            if i < total - 1:
                retorno += ', '

            i += 1

        retorno += '}'

        return retorno
    
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__tamanho
    
    @property
    def __fator_carga(self):
        return self.__tamanho / self.__capacidade_atual

    @staticmethod
    def __verificar_chave(chave):
        hash(chave)

    @staticmethod
    def __hash_deterministico(chave):
        codificado = str(chave).encode()
        return int(sha256(codificado).hexdigest(), 16)

    def __descobrir_indice(self, chave):
        return self.__hash_deterministico(chave) % self.__capacidade_atual

    def __setitem__(self, chave, valor):
        self.__verificar_chave(chave)

        if self.__fator_carga >= self.__limiar_expandir:
            self.__atualizar_tabela(self.__capacidade_atual * self.__fator_expansao)

        indice = self.__descobrir_indice(chave)

        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                elemento.valor = valor 
                return 

        novo_elemento = self.__Elemento(chave, valor)
        self.__tabela_interna[indice].append(novo_elemento)
        self.__tamanho += 1

    def __iter__(self):
        for lista in self.__tabela_interna:
            for elemento in lista:
                yield elemento.chave, elemento.valor

    def __getitem__(self, chave):
        self.__verificar_chave(chave)

        indice = self.__descobrir_indice(chave)
        
        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                return elemento.valor

        raise KeyError(f'Chave {chave} não encontrada')
    
    def __delitem__(self,chave):
        self.__verificar_chave(chave)

        if self.__fator_carga <= self.__limiar_reduzir:
            self.__atualizar_tabela(ceil(self.__capacidade_atual * self.__fator_reducao))

        indice = self.__descobrir_indice(chave)

        for i, elemento in enumerate(self.__tabela_interna[indice]):
            if elemento.chave == chave:
                del self.__tabela_interna[indice][i]
                self.__tamanho -= 1
                return
        
        raise KeyError(f'Chave {chave} não encontrada')

    def __atualizar_tabela(self, nova_capacidade):
        tabela_antiga = self.__tabela_interna

        self.__tabela_interna = [[] for _ in range(nova_capacidade)]
        self.__capacidade_atual = nova_capacidade
        self.__tamanho = 0

        for lista in tabela_antiga:
            for elemento in lista:
                self[elemento.chave] = elemento.valor

######################################################################################################

if __name__ == '__main__':
    # Instância
    pessoa = tabela_hash()

    #Função put para inserir chaves e valores
    pessoa['nome'] = 'João Vilian'
    pessoa['idade'] = 30
    pessoa['sexo'] = 'Masculino'
    pessoa['profissao'] = 'Desenvolvedor'
    pessoa['nacionalidade'] = 'Brasileiro'

    #Função get para recuperar valores
    print(f'Visualização de dicionário completo: {pessoa}' )
    print(f'Quantidade de elementos: {len(pessoa)}')
    print(pessoa['nome'])
