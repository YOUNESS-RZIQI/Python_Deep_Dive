from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """
    An abstract base class defining the common processing interface
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the data and return result string.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the output string.
        """
        return result


class NumericProcessor(DataProcessor):
    """
    Specialized processor for numeric data.
    """

    def __init__(self, size: int = 0,
                 sum: int = 0,
                 avg: float = 0) -> None:
        """
        Initialize numeric statistics.
        """
        self.sum: Union[int, float] = sum
        self.list_size: int = size
        self.avg: float = avg
        self.data: List[int] = []

    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.
        """
        try:
            for d in data:
                if not isinstance(d, int):
                    raise ValueError()
            self.data = data
            print(f"Processing data: {data}")
            print("Validation: Numeric data verified")
            return True
        except Exception as e:
            print("Validation: Numeric data Not verified")
            print("Error:", e)
            return False

    def process(self, data: Any) -> str:
        """
        Process the data and return result string.
        """
        try:
            if (data is True):
                self.sum = sum(self.data)
                self.list_size = len(self.data)
                self.avg = sum(self.data) / len(self.data)
                return "Success"
            else:
                return "Fail"
        except Exception:
            return "Fail"

    def format_output(self, result: str) -> str:
        """
        Format the output string.
        """
        if self.list_size > 1:
            values = "values"
        else:
            values = "value"
        if result == "Success":
            return (
                super().format_output(f"{self.list_size} numeric {values}, "
                                      f"sum={self.sum}, avg={self.avg}"))
        return super().format_output("Processing failed")

    def proccessing_demo(self, data: List[int]) -> str:

        if len(data) > 1:
            values = "values"
        else:
            values = "value"

        return (f"Processed {len(data)} numeric {values}, sum={sum(data)},"
                f" avg={sum(data)/len(data)}")


class TextProcessor(DataProcessor):
    """
    Specialized processor for Text data.
    """

    def __init__(self, len: int = 0,
                 words: int = 0) -> None:
        """
        Initialize Text statistics.
        """
        self.str_len = len
        self.str_words = words
        self.data = ""

    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.
        """
        try:
            if not isinstance(data, str):
                raise ValueError()
            self.data = data
            print(f'Processing data: "{data}"')
            print("Validation: Text data verified")
            return True
        except Exception as e:
            print("Validation: Text data Not verified")
            print("Error:", e)
            return False

    def process(self, data: Any) -> str:
        """
        Process the data and return result string.
        """
        try:
            if (data is True):
                self.str_words = len(self.data.split())
                self.str_len = len(self.data)
                return "Success"
            else:
                return "Fail"
        except Exception:
            return "Fail"

    def format_output(self, result: str) -> str:
        """
        Format the output string.
        """
        if self.str_len > 1:
            characters = "characters"
        else:
            characters = "character"
        if self.str_words > 1:
            words = "words"
        else:
            words = "word"
        if result == "Success":
            return (
                super().format_output(f"text: {self.str_len} {characters},"
                                      f" {self.str_words} {words}")
            )
        return super().format_output("Processing failed")

    def proccessing_demo(self, data: str) -> str:
        data_len = len(data)
        data_words = len(data.split())

        if data_len > 1:
            characters = "characters"
        else:
            characters = "character"

        if data_words > 1:
            words = "words"
        else:
            words = "word"

        return (f"Processed text: {data_len} {characters}, "
                f"{data_words} {words}")


class LogProcessor(DataProcessor):
    """
    Specialized processor for Text data.
    """

    def __init__(self, string: str = "") -> None:
        """
        Initialize Text statistics.
        """
        self.data: str = string

    def validate(self, data: Any) -> bool:
        """
        Validate if data is appropriate for this processor.
        """
        try:
            if "Connection timeout" in data:
                self.data = data
                print(f'Processing data: "ERROR: {data}"')
                print("Validation: Log entry verified")
                return False
            else:
                self.data = data
                print(f'Processing data: "{data}"')
                print("Validation: Log entry verified")
                return True
        except Exception as e:
            print(e)
            return False

    def process(self, data: Any) -> str:
        """
        Process the data and return result string.
        """
        try:
            if not isinstance(self.data, str):
                raise ValueError()
            if data is False:
                return "Fail"
            else:
                return "Success"
        except Exception:
            return "Fail"

    def format_output(self, result: str) -> str:
        """
        Format the output string.
        """
        if result == "Success":
            return super().format_output("[INFO] INFO level "
                                         f"detected: {self.data}")
        return super().format_output("[ALERT] ERROR level detected:"
                                     f" {self.data}")

    def proccessing_demo(self, data: str) -> str:
        if "Connection timeout" in data:
            return f"[ALERT] ERROR level detected: {data}"
        else:
            return f"[INFO] INFO level detected: {data}"


def initializing_numeric_processor(data: Optional[List] = None) -> None:
    """
    initializing numeric processor
    """

    print("\nInitializing Numeric Processor...")
    if data is None:
        data = [1, 2, 3, 4, 5]
    num_p_obj = NumericProcessor()

    print("Output: Processed",
          num_p_obj.format_output(num_p_obj.process(num_p_obj.validate(data))))


def initializing_text_processor(data: Optional[str] = None) -> None:
    """
    initializing text processor
    """

    print("\nInitializing Text Processor...")
    if data is None:
        data = "Hello Nexus World"
    txt_p_obj = TextProcessor()

    print("Output: Processed",
          txt_p_obj.format_output(txt_p_obj.process(txt_p_obj.validate(data))))


def initializing_log_processor(data: Optional[str] = None) -> None:
    """
    initializing log processor
    """

    print("\nInitializing Log Processor...")
    if data is None:
        data = "Connection timeout"
    log_p_obj = LogProcessor()
    print("Output:",
          log_p_obj.format_output(log_p_obj.process(log_p_obj.validate(data))))


def polymorphic_processing_demo() -> None:

    """
    polymorphic processing demo
    """

    print("\n=== Polymorphic Processing Demo ===")

    processors: Dict[int, List] = {
        1: [NumericProcessor(), [1, 2, 3]],
        2: [TextProcessor(), "123456 89111"],
        3: [LogProcessor(), "System ready"],
    }

    if len(processors) > 1:
        print("\nProcessing multiple data types through same interface...")

    else:
        print("\nProcessing one data type...")

    i = 1
    for key in processors:
        obj, data = processors[key]
        print(f"Result {i}:", obj.proccessing_demo(data))
        i += 1


def stream_processor() -> None:

    """
    stream processor program
    """

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    try:
        initializing_numeric_processor()
    except Exception as e:
        print("Error:", e)

    try:
        initializing_text_processor()
    except Exception as e:
        print("Error:", e)

    try:
        initializing_log_processor()
    except Exception as e:
        print("Error:", e)

    try:
        polymorphic_processing_demo()
    except Exception as e:
        print("Error:", e)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
