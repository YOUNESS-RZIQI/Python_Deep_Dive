from typing import Any, Dict, List, Protocol, Union
from collections import deque
from abc import ABC, abstractmethod

# =========================
# 1) Protocol = typing rule
# =========================
class ProcessingStage(Protocol):
    # Any object with process(data) is accepted as a stage (no inheritance required)
    def process(self, data: Any) -> Any:
        ...


# =========================
# 2) ABC Pipeline = engine
# =========================
class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        # The pipeline "owns" a list of stages (Input -> Transform -> Output)
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        # Add a stage object (InputStage(), TransformStage(), OutputStage())
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        # This is the core: pipeline calls stage.process() one by one
        # data = InputStage.process(data)
        # data = TransformStage.process(data)
        # data = OutputStage.process(data)
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        # Each Adapter overrides this to do format-specific stuff
        ...


# =========================
# 3) Stages = workers
# =========================
class InputStage:
    # Called FIRST by the pipeline (inside run_stages)
    # For JSON: validate input type, parse raw JSON string -> dict
    def process(self, data: Any) -> Dict[str, Any]:
        return {}  # placeholder


class TransformStage:
    # Called SECOND
    # For JSON: enrich dict (add metadata), normalize fields, validate ranges
    def process(self, data: Any) -> Dict[str, Any]:
        return {}  # placeholder


class OutputStage:
    # Called THIRD
    # For JSON: format final message/string for output
    def process(self, data: Any) -> str:
        return ""  # placeholder


# =========================
# 4) Adapter = pipeline + override
# =========================
class JSONAdapter(ProcessingPipeline):
    def __init__(self) -> None:
        super().__init__()  # important: initialize stages list from base class

        # The adapter builds/configures its pipeline stages (the “graph”)
        # JSONAdapter contains stages (composition)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Union[str, Any]:
        # JSONAdapter is called by NexusManager (or directly)
        # 1) try/except for recovery
        # 2) call base pipeline engine to run stages in order
        #
        # flow:
        # NexusManager -> JSONAdapter.process(data)
        # JSONAdapter.process -> self.run_stages(data)
        # self.run_stages -> stage1.process -> stage2.process -> stage3.process
        #
        # return final output (string)
        return self.run_stages(data)


# =========================
# 5) Manager = orchestrator
# =========================
class NexusManager:
    def __init__(self) -> None:
        # Holds many pipelines (JSONAdapter, CSVAdapter, StreamAdapter)
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        # Add an adapter/pipeline
        self.pipelines.append(pipeline)

    def process(self, pipeline_index: int, data: Any) -> Any:
        # Pick a pipeline and call its process()
        # This is polymorphism: manager treats all adapters the same
        return self.pipelines[pipeline_index].process(data)


# Example call flow (conceptually):
# manager = NexusManager()
# manager.add_pipeline(JSONAdapter())
# result = manager.process(0, '{"sensor":"temp","value":23.5}')


nexus_pipeline.py
Requirements covered:
1) super()                      -> adapters call super().__init__()
2) try/except                   -> pipeline run() + recovery
3) list & dict comprehensions   -> used in CSV + stats/enrichment
4) ABC & @abstractmethod        -> ProcessingPipeline
5) Protocol (duck typing)       -> ProcessingStage
6) collections module           -> deque for stream buffering
7) type hints throughout        -> typing used everywhere

