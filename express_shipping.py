from abstract_shipping import AbstractShipping

class ExpressShipping(AbstractShipping, object):
    
    def calculate_shipping(self, order, distance):
        print('Entrega Expressa')
        return (order.value + (distance * 0.28)) + 30