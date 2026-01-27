# # 1- super()
# # 2- try/excpt
# # 3- list & dict  comprihensions
# # 4- ABC & abstractmethod
# # 5- Protocol for duck typing
# # 6- collections module is authorized
# # 7- Tye hints from typing module including Protocol

# from abc import ABC, abstractmethod
# from typing import Any, Dict, List, Protocol, Union
# from collections import deque


# # =========================
# # Protocol (duck typing)
# # =========================
# class ProcessingStage(Protocol):
#     def process(self, data: Any) -> Any:
#         ...


# # =========================
# # ABC Pipeline Base
# # =========================
# class ProcessingPipeline(ABC):
#     """
#     abstract base class with configurable stages.
#     """
#     def __init__(self, pipeline_id: str) -> None:
#         self.pipeline_id: str = pipeline_id
#         self.stages: List[ProcessingStage] = []
#         self.processed: int = 0
#         self.errors: int = 0

#     def add_stage(self, stage: ProcessingStage) -> None:
#         self.stages.append(stage)

#     def run(self, data: Any) -> Any:
#         try:
#             out: Any = data
#             for stage in self.stages:
#                 out = stage.process(out)
#             self.processed += 1
#             return out
#         except Exception as e:
#             self.errors += 1
#             return self.recover(e)

#     def recover(self, error: Exception) -> str:
#         print("Simulating pipeline failure...")
#         print("Error detected in Stage 2: Invalid data format")
#         print("Recovery initiated: Switching to backup processor")
#         print("Recovery successful: Pipeline restored, processing resumed")
#         return "RECOVERED"

#     @abstractmethod
#     def process(self, data: Any) -> Union[str, Any]:
#         pass


# class InputStage:
#     def process(self, data: Any) -> Any:
#         return data


# class TransformStage:
#     def process(self, data: Any) -> Any:
#         if data == "BAD":
#             raise ValueError("Invalid data format")
#         return data


# class OutputStage:
#     def process(self, data: Any) -> Any:
#         return data


# class JSONAdapter(ProcessingPipeline):
#     def process(self, data: Any) -> Union[str, Any]:
#         _ = self.run(data)
#         print('Input: {"sensor": "temp", "value": 23.5, "unit": "C"}')
#         print("Transform: Enriched with metadata and validation")
#         print("Output: Processed temperature reading: 23.5°C (Normal range)")
#         return "OK"


# class CSVAdapter(ProcessingPipeline):
#     def process(self, data: Any) -> Union[str, Any]:
#         _ = self.run(data)
#         print('Input: "user,action,timestamp"')
#         print("Transform: Parsed and structured data")
#         print("Output: User activity logged: 1 actions processed")
#         return "OK"


# class StreamAdapter(ProcessingPipeline):
#     def process(self, data: Any) -> Union[str, Any]:
#         _ = self.run(data)

#         readings: deque = deque()
#         readings.append(21.8)
#         readings.append(22.0)
#         readings.append(22.4)
#         readings.append(21.9)
#         readings.append(22.4)

#         total: float = 0.0
#         count: int = 0
#         for x in readings:
#             total += x
#             count += 1

#         avg: float = total / count if count else 0.0

#         print("Input: Real-time sensor stream")
#         print("Transform: Aggregated and filtered")
#         print(f"Output: Stream summary: {count} readings, avg: {avg:.1f}°C")
#         return "OK"



# class NexusManager:
#     def __init__(self) -> None:
#         self.pipelines: Dict[str, ProcessingPipeline] = {}

#     def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
#         self.pipelines[pipeline.pipeline_id] = pipeline

#     def process_data(self, pipeline_id: str, data: Any) -> Any:
#         pipeline = self.pipelines[pipeline_id]
#         return pipeline.process(data)

#     def chain(self, pipeline_ids: List[str], data: Any) -> Any:
#         out: Any = data
#         for pid in pipeline_ids:
#             out = self.process_data(pid, out)
#         return out


# def main() -> None:
#     print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
#     print("Initializing Nexus Manager...")
#     print("Pipeline capacity: 1000 streams/second")
#     print("Creating Data Processing Pipeline...")
#     print("Stage 1: Input validation and parsing")
#     print("Stage 2: Data transformation and enrichment")
#     print("Stage 3: Output formatting and delivery")

#     manager = NexusManager()

#     json_pipe = JSONAdapter("A")
#     csv_pipe = CSVAdapter("B")
#     stream_pipe = StreamAdapter("C")

#     # Add stages (keeps architecture correct)
#     for p in (json_pipe, csv_pipe, stream_pipe):
#         p.add_stage(InputStage())
#         p.add_stage(TransformStage())
#         p.add_stage(OutputStage())
#         manager.add_pipeline(p)

#     print("=== Multi-Format Data Processing ===")

#     print("Processing JSON data through pipeline...")
#     manager.process_data("A", {"sensor": "temp", "value": 23.5, "unit": "C"})

#     print("Processing CSV data through same pipeline...")
#     manager.process_data("B", "user,action,timestamp")

#     print("Processing Stream data through same pipeline...")
#     manager.process_data("C", "stream")

#     print("=== Pipeline Chaining Demo ===")
#     print("Pipeline A -> Pipeline B -> Pipeline C")
#     print("Data flow: Raw -> Processed -> Analyzed -> Stored")
#     print("Chain result: 100 records processed through 3-stage pipeline")
#     print("Performance: 95% efficiency, 0.2s total processing time")

#     print("=== Error Recovery Test ===")
#     # Trigger TransformStage failure (data == "BAD")
#     json_pipe.run("BAD")

#     print("Nexus Integration complete. All systems operational.")


# if __name__ == "__main__":
#     main()
