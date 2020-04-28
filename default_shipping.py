from abstract_shipping import AbstractShipping

class DefaultShipping(AbstractShipping, object):
    
    def calculate_shipping(self, order, distance):
        print('Entrega Padrão')
        return (order.value + (distance * 0.16)) + 15