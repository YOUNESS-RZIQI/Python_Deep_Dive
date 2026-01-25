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

    def __init__(self, stream_id: str = "", type: str = "",
                 sensor_process_list: Dict[str, Union[int, float]] = {},
                 readings_processed: int = 0, avg_temp: float = 0.0,
                 criteria: str = "°C"):
        """    """
        self.__name__ = "Sensor"
        self.data_batch = []
        self.stream_id = stream_id
        self.type = type
        self.sensor_process_list = sensor_process_list
        self.criteria = criteria

        self.readings_processed = readings_processed
        self.avg_temp = avg_temp
        self.alerts = 0

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:

        """
        Filter data based on criteria
        """
        try:
            if len(data_batch) != 4 and len(data_batch) != 3:
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

#           [ 0, 1, [temp:22.5, humidity:65, pressure:1013], ?]

            self.stream_id, self.type, self.sensor_process_list, criteria = data_batch

            if criteria is not None:
                self.criteria = criteria
            temps_str_vals = self.sensor_process_list[0].split(":")

            del temps_str_vals[0]

            temps = [float(val) for val in temps_str_vals]

            if data_batch[-1] is not None:
                self.criteria = data_batch[-1]
            else:
                del data_batch[-1]

            self.data_batch = data_batch

            self.readings_processed = len(self.sensor_process_list)

            self.avg_temp = sum(temps)/len(temps)
            readings = "readings" if self.readings_processed > 1 else "reading"
            return (f"{self.readings_processed} {readings} processed, avg temp: {self.avg_temp}"
                    f"{self.criteria}")
        except Exception as e:
            print(e)
            return "Fail"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        """
        return a format depentding on process
        """
        print("\nInitializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")
        print(f"Processing sensor batch: {self.sensor_process_list}")
        print("Sensor analysis:", self.process_batch(self.filter_data(self.data_batch)))
       

        return 




class TransactionStream(DataStream):

    """
    TransactionStream processes buy/sell operations with net flow calculations
    """

    pass


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
data = ["SENSOR_001", "Environmental Data", ["temp:22.5", "humidity:65", "pressure:1013"]]
obj = SensorStream()
obj.process_batch(obj.filter_data(data))
obj.get_stats()
