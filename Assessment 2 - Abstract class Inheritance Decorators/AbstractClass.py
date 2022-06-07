from abc import ABC, abstractmethod
import logging
logging.basicConfig(filename="AbstractLog.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class Fruit(ABC):
    """
    This abstract class will act as a blueprint for the sub classes and contains abstract methods
    """
    def __init__(self):
        logging.info("... Abstract class executed ...")

    @abstractmethod
    def showDetails(self):
        """This abstract method is just blueprint and returns None"""
        pass
    
    @abstractmethod
    def calcBill(self):
        """This abstract method is just blueprint and returns None"""
        pass

class Mango(Fruit):
    """
    This class is derived from the abstract class (Fruit) and has few properties
    """
    def __init__(self, taste, qty, price):
        self.name = "Mango"
        self.taste = taste
        self.qty = qty
        self.price = price
        logging.info("... Mango class executed ...")

    def showDetails(self):
        """
        This method will show/print the properties of Mango fruit.
        Returns: None
        """
        print("\nName of fruit:", self.name)
        print("Taste:", self.taste)
        print("Quantity:", self.qty)
        print("Price per KG:", self.price)
    
    def calcBill(self):
        """
        This method will calculate the billing amount by multiplying the unit price with quantity.
        Returns: None
        """
        try:
            print("Total Bill amount:", self.price * self.qty)
        except Exception as err:
            logging.exception(f"Exception occurred during billing calculation. Error: {err}")
    

class Apple(Fruit):
    def __init__(self, taste, qty, price):
        self.name = "Apple"
        self.taste = taste
        self.qty = qty
        self.price = price
        logging.info("... Apple class executed ...")

    def showDetails(self):
        """
        This method will show/print the properties of Apple fruit.
        Returns: None
        """
        print("\nName of fruit:", self.name)
        print("Taste:", self.taste)
        print("Quantity:", self.qty)
        print("Price per KG:", self.price)
    
    def calcBill(self):
        """
        This method will calculate the billing amount by multiplying the unit price with quantity.
        Returns: None
        """
        try:
            print("Total Bill amount:", self.price * self.qty)
        except Exception as err:
            logging.exception(f"Exception occurred during billing calculation. Error: {err}")

# Main stream
if __name__ == '__main__':
    logging.info("*** Application started ***")
    my_apple = Apple("Sweet", 3, 125)
    my_apple.showDetails()
    my_apple.calcBill()
    
    wild_mango = Mango("Sour", 5, 180)
    wild_mango.showDetails()
    wild_mango.calcBill()
    logging.info("*** End of Application process ***")
