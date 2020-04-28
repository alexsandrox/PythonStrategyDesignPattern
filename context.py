from order import Order
from default_shipping import DefaultShipping
from sedex_shipping import SedexShipping
from express_shipping import ExpressShipping

class Context(object):

    def execute_calculation(self, option, order, distance):
        options = {
            1: DefaultShipping,
            2: SedexShipping,
            3: ExpressShipping
        }
        if option in options:
            shipping = options[option]()
            print('{:,.2f}'.format(shipping.calculate_shipping(order, distance)).replace(',', '.'))
        else:
            print('Opção inválida')


print('############################################################################')
print('##  DESIGN PATTERN -> STRATEGY  -  PEDIDO COM TIPOS DE FRETES DIFERENTES  ##')
print()

# criar um pedido e passar o valor do pedido
order = Order(500)

# criar uma instância de Cálculo de Frete
calculo_de_frete = Context()

# agora o Cálculo do Frete já pode chamar o método execute_calculation, 
# passando a Opção de Escolha de Frete, o Pedido e a Distância do Local da Entrega
distancia = int(input('Digite a distância em KM:_'))
opcao = int(input('Digite a opção de entrega [ (1) Normal, (2) Sedex, (3) Expressa ]:_'))
calculo_de_frete.execute_calculation(opcao, order, distancia)
