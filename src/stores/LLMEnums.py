from enum import Enum

class LLMEnums(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenIAEnums(Enum) : 
    SYSTEM = "system"
    USER="user"
    ASSISTANT = "assistant" 