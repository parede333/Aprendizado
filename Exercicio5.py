'''
Esse programa executa algumas operações da calculadora padrão do windows.
'''
def soma(x,y):
    """
    Função da soma.
    
    Parâmetros
    ----------
    x : float
        
    y : float
        
    Returns
    -------
    Retorna a soma de x e y.

    """
    print(x + y)

def subtracao(x,y):
    """
    Função da subtração.
    
    Parâmetros
    ----------
    x : float
        
    y : float        

    Returns
    -------
    Retorna a subtração de x e y.

    """
    print(x - y)

def multiplicacao(x,y):
    """
    Função da multiplicação

    Parâmetros
    ----------
    x : float
        
    y : float
        
    Returns
    -------
    Retorna o resultado da muitlipliacação de x e y.

    """
    print(x * y)

def divisao(x,y):
    """
    Função da divisão.

    Parâmetros
    ----------
    x : float
        
    y : float
      O parâmetro y deve ser diferente de zero.

    Returns
    -------
    Retorna o valor da divisão de x por y.

    """
    if y == 0 : print('Não é possivel dividir por zero')
    print( x / y)

def quadrado(base):
    """
    Função quadrado

    Parâmetros
    ----------
    base : float

    Returns
    -------
    Retorna o valor do númerio inserido elevado ao quadrado

    """
    print(base**2)

def raiz(radicando):
    """
    Função raiz quadrada.

    Parâmetros
    ----------
    radicando : float
      O parâmetro radicando deve ser maior ou igual a zero.

    Returns
    -------
    Retorna o valor da raiz quadrada do número.

    """
    print(radicando**(1/2))

def inverso(x):
    """
    Inverso de um número qualquer

    Parâmetros
    ----------
    dividendo : float
        O parâmetro x deve ser diferente de zero.

    Returns
    -------
    None.

    """
    if x == 0 : print('Não é possivel dividir por zero')
    else: print(1/x)

def porcentagem(numero,requerido):
    """
    Função da porcentagem.

    Parâmetros
    ----------
    numero : float
        
    requerido : float
        

    Returns
    -------
    Retorna o valor equivalente a porcentagem do número inserio.

    """
    print(numero*(requerido/100))
    
def transF(x):
    """
    Função de transformação de sinal.

    Parâmetros
    ----------
    x : float
        

    Returns
    -------
    Retorna o número inserido com o sinal trocado.

    """
    if x > 0: print(x*(-1))
    elif x < 0: print(x*(-1))
    else: print(x)
