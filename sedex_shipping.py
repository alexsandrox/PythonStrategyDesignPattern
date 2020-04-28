from abstract_shipping import AbstractShipping

class SedexShipping(AbstractShipping, object):
    
    def calculate_shipping(self, order, distance):
        print('Entrega Sedex')
        return (order.value + (distance * 0.22)) + 22