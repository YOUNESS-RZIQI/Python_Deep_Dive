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
        Abstract base class.
    """

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:

        """
        Process a batch of data
        """

        return "In Abstract Class"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        return ["In Abstract Class"]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """
        Return stream statistics
        """

        return {"Stream ID:": "In Abstract Class",
                "Processing sensor batch:": "In Abstract Class",
                "Sensor analysis:": "In Abstract Class"}


class SensorStream(DataStream):

    """
    SensorStream processes temperature/sensor data with alerts
    for extreme values
    """

    def __init__(self, id: str = "", type: str = "",
                 sensor_batch_list: List[str] = [],
                 readings_processed: int = 0, avg_temp: float = 0.0,
                 criteria: str = "°C"):
        """
        Initializing Object variables.
        """
        self.__name__ = "Sensor"
        self.data_batch: List = []
        self.id = id
        self.type = type
        self.sensor_batch_list = sensor_batch_list
        self.criteria = criteria

        self.readings_processed = readings_processed
        self.avg_temp = avg_temp
        self.alerts = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        try:
            if len(data_batch) == 3:
                result = isinstance(data_batch[2], list)
            else:
                result = False
            if len(data_batch) != 3 or result is not True:
                self.alerts += 1
                raise ValueError("\nError in SensorStream Class: Exact"
                                 " Place 'filter_data' method\n")

            new_list = [True] + data_batch
            new_list += [criteria]
            return new_list
        except Exception:
            return [False]

    def process_batch(self, data_batch: List[Any]) -> str:

        """
        Process a batch of data
        """
        try:
            if data_batch[0] is False:
                raise ValueError("\nError in SensorStream Class: Exact Place "
                                 "'process_batch' method\n")
            del data_batch[0]

#   [ Id, sensor word, [temp:22.5, humidity:65, pressure:1013],
#                                               Optional[str|None]]

            self.id, self.type, self.sensor_batch_list, criteria = data_batch

            if criteria is not None:
                self.criteria = criteria
            del data_batch[-1]

            temps_str_vals = (self.sensor_batch_list[0]).split(":")
            del temps_str_vals[0]
            temps = [float(val) for val in temps_str_vals]

            self.data_batch = data_batch

            self.readings_processed = len(self.sensor_batch_list)

            self.avg_temp = sum(temps)/len(temps)

            readings = "readings" if self.readings_processed > 1 else "reading"
            return (f"{self.readings_processed} {readings} processed,"
                    f" avg temp: {self.avg_temp}"
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
                "Sensor analysis:":
                obj.process_batch(obj.filter_data(self.data_batch))}


class TransactionStream(DataStream):

    """
    TransactionStream processes buy/sell operations with net flow calculations
    """

    def __init__(self, id: str = "", type: str = "",
                 transactoin_batch_list: str = "",
                 large_transaction: int = 0, net_flow: int = 0,
                 operations: int = 0):
        """
            Initializing Object Variables.
        """
        self.__name__ = "Transaction"
        self.id = id
        self.type = type
        self.trsctio_batch_list = transactoin_batch_list
        self.data_batch: List = []
        self.criteria = "unit(s)"
        self.buys = 0
        self.sells = 0
        self.net_flow = net_flow
        self.large_transaction = large_transaction
        self.operations = operations
        self.alerts = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        try:
            if len(data_batch) == 3:
                result = isinstance(data_batch[2], list)
            else:
                result = False
            if len(data_batch) != 3 or result is not True:
                self.alerts += 1
                raise ValueError("\nError in TransactionStream Class: Exact "
                                 "Place 'filter_data' method\n")

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
                raise ValueError("\nError in TransactionStream Class:"
                                 " Exact Place 'process_batch' method\n")
            del data_batch[0]

#           [ Id, Transactions,  [buy:100, sell:150, buy:75],
#                                                   Optional[str|None]]

            self.id, self.type, self.trsctio_batch_list, criteria = data_batch

            if criteria is not None:
                self.criteria = criteria
            del data_batch[-1]

            for element in (self.trsctio_batch_list):
                if "buy" in element:
                    splited = element.split(":")
                    self.buys += int(splited[1])
                if "sell" in element:
                    splited = element.split(":")
                    self.sells += int(splited[1])

            self.data_batch = data_batch

            self.operations = len(self.trsctio_batch_list)

            self.net_flow = self.buys - self.sells

            if self.net_flow > 20:
                self.large_transaction += 1

            sign = "+" if self.net_flow > 0 else ""
            return (f"{self.operations} operation(s) processed, net flow:"
                    f" {sign}{self.net_flow} {self.criteria}")

        except Exception as e:
            print(e)
            return "Fail"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """
        Return stream statistics.
        """
        obj = TransactionStream()
        return {"Stream ID:": f"{self.id}, Type: {self.type}",
                "Processing transaction batch:":
                f"{self.trsctio_batch_list}",
                "Transaction analysis:":
                obj.process_batch(obj.filter_data(self.data_batch))}


class EventStream(DataStream):

    """
    EventStream processes system events with error detection and categorization
    """

    def __init__(self):
        """
        Initializing Object Variables.
        """
        self.__name__ = "Event"
        self.id = ""
        self.type = ""
        self.event_batch_list = []
        self.data_batch = []
        self.criteria = "error"
        self.errors = 0
        self.logins = 0
        self.logouts = 0
        self.alerts = 0
        self.events = 0

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        try:
            if len(data_batch) == 3:
                result = isinstance(data_batch[2], list)
            else:
                result = False
            if len(data_batch) != 3 or result is not True:
                self.alerts += 1
                raise ValueError("\nError in TransactionStream Class: "
                                 "Exact Place 'filter_data' method\n")

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
                raise ValueError("\nError in TransactionStream Class: "
                                 "Exact Place 'process_batch' method\n")
            del data_batch[0]

#           [ Id, Transactions,  [buy:100, sell:150, buy:75],
#                                               Optional[str|None]]

            self.id, self.type, self.event_batch_list, criteria = data_batch

            if criteria is not None:
                self.criteria = criteria
            del data_batch[-1]

            for element in (self.event_batch_list):
                if element == "login":
                    self.logins += 1
                elif element == "error":
                    self.errors += 1
                elif element == "logout":
                    self.logouts += 1

            self.data_batch = data_batch

            self.events = len(self.event_batch_list)

            if self.criteria == "error":
                return (f"{self.events} event(s) processed, "
                        f"{self.errors} error detected")
            elif self.criteria == "login":
                return (f"{self.events} event(s) processed, "
                        f"{self.logins} login detected")
            else:
                return (f"{self.events} event(s) processed, "
                        f"{self.logouts} logout detected")

        except Exception as e:
            print(e)
            return "Fail"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """
        Return stream statistics.
        """
        obj = EventStream()
        return {"Stream ID:": f"{self.id}, Type: {self.type}",
                "Processing event batch:": f"{self.event_batch_list}",
                "Event analysis:":
                obj.process_batch(obj.filter_data(self.data_batch))}


class StreamProcessor:

    """
    StreamProcessor class can handle multiple stream types polymorphically
    """

    def sensor_streaming_output(self) -> None:

        """
            sensor streaming output
        """

        data = ["SENSOR_001", "Environmental Data",
                ["temp:22.5", "humidity:65", "pressure:1013"]]
        obj = SensorStream()
        obj.process_batch(obj.filter_data(data))
        stata = obj.get_stats()
        print("\nInitializing Sensor Stream...")
        for key in stata:
            print(key, stata[key])

    def transaction_streaming_output(self) -> None:

        """
            transaction streaming output
        """

        obj = TransactionStream()
        data_batch = ["TRANS_001", "Financial Data",
                      ["buy:100", "sell:150", "buy:75"]]

        obj.process_batch(obj.filter_data(data_batch))
        stata = obj.get_stats()
        print("\nInitializing Transaction Stream...")
        for key in stata:
            print(key, stata[key])

    def event_streaming_output(self) -> None:

        """
            event streaming output
        """

        obj = EventStream()
        data_batsh = ["EVENT_001", "System Events",
                      ["login", "error", "logout"]]
        obj.process_batch(obj.filter_data(data_batsh))
        stata = obj.get_stats()
        print("\nInitializing Event Stream...")
        for key in stata:
            print(key, stata[key])

    def polymorphic_stream_processing(self):

        """
            polymorphic stream processing
        """
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        lst = [[SensorStream(), ["SENSOR_001", "Environmental Data",
                                 ["temp:22.5", "pressure:1013"]]],
               [TransactionStream(), ["TRANS_001", "Financial Data",
                                      ["buy:100", "sell:23", "sell:150",
                                       "buy:75"]]],
               [EventStream(), ["EVENT_001", "System Events",
                                ["login", "error", "logout"]]]]

        print("Batch 1 Results:")
        for obj, data in lst:
            obj.process_batch(obj.filter_data(data))
            splited = (obj.get_stats())[obj.__name__+" analysis:"].split(",")
            print(f"- {obj.__name__} data:", (splited[0]))

        sensor_obj = SensorStream()
        sensor_obj.filter_data([])
        sensor_obj.filter_data([])
        demo_alart = sensor_obj.alerts

        tr_obj = TransactionStream()
        tr_obj.process_batch(tr_obj.filter_data(
            ["TRANS_001", "Financial Data", ["buy:100", "sell:150", "buy:75"]]
            ))
        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {demo_alart} critical sensor alerts, "
              f"{tr_obj.large_transaction} large transaction")


def data_stream() -> None:
    """
        Data stream Program.
    """

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    stream = StreamProcessor()

    stream.sensor_streaming_output()
    stream.transaction_streaming_output()
    stream.event_streaming_output()
    stream.polymorphic_stream_processing()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
