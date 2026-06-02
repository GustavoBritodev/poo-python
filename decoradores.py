'''
Definição:
No Python um decorador é um tipo especial de função 
que permite modificar ou extender o comportamento de outras funções
'''

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

'''
Usando o decorador acima da função, é como se o decorador chamasse a função
Assim mudando o comportamento da função, adicionando código antes e depois da função
'''
@meu_decorador
def minha_funcao():
    print("Minha função foi chamada.")
    
minha_funcao()

'''
Outra abordagem é utilizar uma função ao invés de uma função
Mas essa abordagem é menos utilizada
'''
class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    '''
    Essa função call será executada quando a função passada como parâmetro for chamada
    A única diferença é que no decorador como Classe, a propriedade já foi definida como parâmetro
    dentro do construtor, por isso ao ser chamada na função __call__ é com o self.func
    '''    
    def __call__(self) -> any:
        print("Antes da função ser chamada (Decorador de Classe)")
        self.func()
        print("Depois da função ser chmada (Decorador de Classe)")
        pass
    
@MeuDecoradorDeClasse    
def segunda_funcao():
    print("Segunda função foi chamada.")
    
segunda_funcao()