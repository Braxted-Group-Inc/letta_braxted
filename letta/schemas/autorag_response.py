import html
import json
import re
from typing import List, Union, Dict, Optional

from pydantic import BaseModel, Field

from letta.schemas.enums import MessageStreamStatus
from letta.schemas.letta_message import LettaMessage, LettaMessageUnion
from letta.schemas.usage import LettaUsageStatistics
from letta.utils import json_dumps

class RetrievedPassage(BaseModel):
	content: str
	doc_id: str
	metadata: Dict
	filepath: Optional[str] = None
	start_idx: Optional[int] = None
	end_idx: Optional[int] = None

class AutoragResponse(BaseModel):
    result: Union[str, List[str]]
    retrieved_passage: List[RetrievedPassage]


