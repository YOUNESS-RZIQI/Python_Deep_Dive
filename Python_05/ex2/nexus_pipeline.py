# # 1- super()
# # 2- try/excpt
# # 3- list & dict  comprihensions
# # 4- ABC & abstractmethod
# # 5- Protocol for duck typing
# # 6- collections module is authorized
# # 7- Tye hints from typing module including Protocol

# from typing import Any, Dict, List, Protocol, Union
# from collections import deque
# from abc import ABC, abstractmethod

# class ProcessingStage(Protocol):
#     """
#     Protocol class.
#     """

#     def process(self, data: Any) -> Any:
#         """
#         Protocol method.
#         """
#         pass



# class ProcessingPipeline(ABC):
#     """
#     Abctract class Processing Pipeline.
#     """

#     def __init__(self) -> None:

#         """

#         """
#         self.stages: List[ProcessingStage] = []

#     def add_stage(self) -> None:
#         """

#         """
#         pass

#     @abstractmethod
#     def process(self, data: Any) -> Any:
#         """

#         """
#         return






# class InputStage():
#     """

#     """

#     def process(self, data: Any) -> Dict:
#         """

#         """
#         return {}


# class TransformStage():
#     """

#     """

#     def process(self, data: Any) -> Dict:
#         """

#         """
#         return {}


# class OutputStage():
#     """

#     """

#     def process(self, data: Any) -> str:
#         """

#         """
#         return ""





# class JSONAdapter(ProcessingPipeline):

#     """
    
#     """

#     def __init__(self) -> None:
#         """

#         """
#         self.data: Dict[str, Union[str, float]] = {}

#     def process(self, data: Any) -> Union[str,Any]:
#         """

#         """
#         return ""


# class CSVAdapter(ProcessingPipeline):

#     """
    
#     """

#     def __init__(self) -> None:
#         """

#         """
#         pass

#     def process(self, data: Any) -> Union[str, Any]:
#         """

#         """
#         return ""


# class StreamAdapter(ProcessingPipeline):

#     """
    
#     """

#     def __init__(self) -> None:
#         """

#         """
#         pass

#     def process(self, data: Any) -> Union[str, Any]:
#         """

#         """
#         return ""


# class NexusManager():
#     """

#     """

#     def __init__(self, pipeline_id: str) -> None:
        
#         """

#         """
#         self.pipelines: List[ProcessingPipeline] = []

#     def add_pipeline(self, data: Any) -> None:
#         """

#         """

#         pass

#     def process(self, data: Any) -> Union[str,Any]:
#         """

#         """

#         return ""



# # if __name__ == "__main__":
# #     main()


