import logging
logging.basicConfig(filename="MultiInhertLog.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# definition of the class starts here
class TeleConsumer:
    """
    This Telecom Consumer Base class will hold the consumer details like Name, 
    Mobile Directory Number(MDN) and City
    """
    def __init__(self, ConsumerName, ConsumerMDN, City):
        self.name = ConsumerName
        self.mdn = ConsumerMDN
        self.city = City
        logging.info("... TeleConsumer base class executed ...")
        
    def showConsumerDetails(self):
        """
        This method will print the consumer details.
        returns: None
        """
        print("\nConsumer Name:", self.name)
        print("Consumer MDN:", self.mdn)
        print("Consumer City:", self.city)

        
# defining another class
class TeleTariff:
    """
    This Telecom Tariff Base class will hold the tariff details including the Tariff amount.
    """
    def __init__(self, TariffId, TariffName, TariffAmount):
        self.TariffId = TariffId
        self.TariffName = TariffName
        self.TariffAmount = TariffAmount
        logging.info("... TeleTariff base class executed ...")
  
    def showTariffData(self):
        """
        This method will print the Tariff details
        returns: None
        """
        print("Tariff ID:", self.TariffId)
        print("Tariff Name:", self.TariffName)
        print("Tariff Amount:", self.TariffAmount)
  
  
class ConsumerBill(TeleConsumer, TeleTariff): 
    """
    This sub class extends both TeleConsumer and TeleTariff classes 
    and calculates the billing amount considering the Tax percent as 18%.
    """
    def __init__(self, ConsumerName, ConsumerMDN, City, TariffId, TariffName, TariffAmount):
        # logging.info(f"... New object was initiated for the derived class: {self.name} ...")
        TeleConsumer.__init__(self, ConsumerName, ConsumerMDN, City)
        TeleTariff.__init__(self, TariffId, TariffName, TariffAmount)
        logging.info(f"... New object was initiated for the derived class: {self.name} ...")
        
    def calcBillAmount(self):
        """
        This method calculates the billing amount using the Tax percent as 18% and print the total amount
        """
        try:
            print("Bill Amount: ", (self.TariffAmount * 18 / 100) + self.TariffAmount)
        except Exception as err:
            logging.exception(f"Exception occurred during billing calculation. Error: {err}")

# Main stream
if __name__ == '__main__':
    logging.info("*** Application started ***")
    NiTech = ConsumerBill('NiTech Automation', 9842098420, 'Chennai', 1132, "Unlimited-5G", 1200)
    NiTech.showConsumerDetails()
    NiTech.showTariffData()
    NiTech.calcBillAmount()

    iNeuron = ConsumerBill('iNeuron', 9840098400, 'Bangalore', 1035, "Unlimited-Fiber", 1800)
    iNeuron.showConsumerDetails()
    iNeuron.showTariffData()
    iNeuron.calcBillAmount()
    logging.info("*** End of Application process ***")