from abc import ABC, abstractmethod

class AbstractShipping(ABC, object):
    
    @abstractmethod
    def calculate_shipping(self, order, distance):
        pass