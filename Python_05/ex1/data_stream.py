# 1) classes with inheritance
# 2) super()
# 3) try/except
# 4) List comprehensions in data processing
# 5) ABC & @abstractmethod
# 6) isinstance

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    """

    """

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:

        """

        """

        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:

        """

        """

        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """

        """

        pass


class SensorStream(DataStream):

    """
    SensorStream processes temperature/sensor data with alerts for extreme values
    """

    def __init__(self, id: str = "", type: str = "",
                 sensor_batch_list: Dict[str, Union[int, float]] = {},
                 readings_processed: int = 0, avg_temp: float = 0.0,
                 criteria: str = "°C"):
        """    """
        self.__name__ = "Sensor"
        self.data_batch = []
        self.id = id
        self.type = type
        self.sensor_batch_list = sensor_batch_list
        self.criteria = criteria

        self.readings_processed = readings_processed
        self.avg_temp = avg_temp
        self.alerts = 0

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        try:
            if len(data_batch) != 3 or isinstance(data_batch[2], list) is not True:
                self.alerts += 1
                raise ValueError("\nError in SensorStream Class: Exact Place 'filter_data' method\n")

            new_list = [True] + data_batch
            new_list += [criteria]
            return new_list
        except Exception as e:
            print(e)
            return [False]

    def process_batch(self, data_batch: List[Any]) -> str:

        """
        Process a batch of data
        """
        try:
            if data_batch[0] is False:
                raise ValueError("\nError in SensorStream Class: Exact Place 'process_batch' method\n")
            del data_batch[0]

#           [ Id, sensor word, [temp:22.5, humidity:65, pressure:1013], Optional[str|None]]

            self.id, self.type, self.sensor_batch_list, criteria = data_batch

            if criteria is not None:
                self.criteria = criteria
            del data_batch[-1]

            temps_str_vals = self.sensor_batch_list[0].split(":")
            del temps_str_vals[0]
            temps = [float(val) for val in temps_str_vals]

            self.data_batch = data_batch

            self.readings_processed = len(self.sensor_batch_list)

            self.avg_temp = sum(temps)/len(temps)

            readings = "readings" if self.readings_processed > 1 else "reading"
            return (f"{self.readings_processed} {readings} processed, avg temp: {self.avg_temp}"
                    f"{self.criteria}")

        except Exception as e:
            print(e)
            return "Fail"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """
        Return stream statistics.
        """
        obj = SensorStream()
        return {"Stream ID:": f"{self.id}, Type: {self.type}",
                "Processing sensor batch:": f"{self.sensor_batch_list}",
                "Sensor analysis:": obj.process_batch(obj.filter_data(self.data_batch))}


class TransactionStream(DataStream):

    """
    TransactionStream processes buy/sell operations with net flow calculations
    """

    def __init__(self, id: str = "", type: str = "", transactoin_batch_list: str = "",
                 large_transaction: Union[int, float] = 0, net_flow: int = 0,
                 operations: int = 0):
        """
            Initializing Object Variables.
        """
        self.__name__ = "Transaction"
        self.id = id
        self.type = type
        self.transaction_batch_list = transactoin_batch_list
        self.data_batch = []
        self.criteria = "unit(s)"
        self.buys = 0
        self.sells = 0
        self.net_flow = net_flow
        self.large_transaction = large_transaction
        self.operations = operations
        self.alerts = 0

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        try:
            if len(data_batch) != 3 or isinstance(data_batch[2], list) is not True:
                self.alerts += 1
                raise ValueError("\nError in TransactionStream Class: Exact Place 'filter_data' method\n")

            new_list = [True] + data_batch
            new_list += [criteria]
            return new_list
        except Exception as e:
            print(e)
            return [False]

    def process_batch(self, data_batch: List[Any]) -> str:

        """
        Process a batch of data
        """
        try:
            if data_batch[0] is False:
                raise ValueError("\nError in TransactionStream Class: Exact Place 'process_batch' method\n")
            del data_batch[0]

#           [ Id, Transactions,  [buy:100, sell:150, buy:75], Optional[str|None]]

            self.id, self.type, self.transaction_batch_list, criteria = data_batch

            if criteria is not None:
                self.criteria = criteria
            del data_batch[-1]

            for element in (self.transaction_batch_list):
                if "buy" in element:
                    splited = element.split(":")
                    self.buys += int(splited[1])
                    # print("buy")
                if "sell" in element:
                    splited = element.split(":")
                    self.sells += int(splited[1])
                    # print("sell")

            self.data_batch = data_batch

            self.operations = len(self.transaction_batch_list)

            self.net_flow = self.buys - self.sells

            sign = "+" if self.net_flow > 0 else ""
            return (f"{self.operations} operation(s), net flow: {sign}{self.net_flow} {self.criteria}")

        except Exception as e:
            print(e)
            return "Fail"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """
        Return stream statistics.
        """
        obj = TransactionStream()
        return {"Stream ID:": f"{self.id}, Type: {self.type}",
                "Processing transaction batch:": f"{self.transaction_batch_list}",
                "Transaction analysis:": obj.process_batch(obj.filter_data(self.data_batch))}


class EventStream(DataStream):

    """
    EventStream processes system events with error detection and categorization
    """

    pass


class StreamProcessor:

    """
    StreamProcessor class can handle multiple stream types polymorphically
    """
    # use is instance to print each output format.

    def sensor_streaming_output(self):
        data = ["SENSOR_001", "Environmental Data", ["temp:22.5", "humidity:65", "pressure:1013"]]
        obj = SensorStream()
        obj.process_batch(obj.filter_data(data))
        stata = obj.get_stats()
        print("\nInitializing Sensor Stream...")
        for key in stata:
            print(key, stata[key])

    def transaction_streaming_output(self):
        obj = TransactionStream()
        data_batch = [1, "Financial Data",  ["buy:100", "sell:150", "buy:75"] ]

        obj.process_batch(obj.filter_data(data_batch))
        stata = obj.get_stats()
        print("\nInitializing Transaction Stream...")
        for key in stata:
            print(key, stata[key])

StreamProcessor().sensor_streaming_output()
StreamProcessor().transaction_streaming_output()