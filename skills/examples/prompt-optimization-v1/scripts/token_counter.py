"""Token counting utilities for various LLM models."""

import re
from typing import Dict, List, Optional
from enum import Enum


class ModelType(Enum):
    """Supported LLM models for token counting."""
    GPT3 = "gpt-3.5-turbo"
    GPT4 = "gpt-4"
    CLAUDE = "claude"
    CUSTOM = "custom"


class TokenCounter:
    """Count tokens in prompts for different LLM models."""

    # Approximate token ratios for different models
    TOKEN_RATIOS = {
        ModelType.GPT3: 1.0,  # Base ratio
        ModelType.GPT4: 1.0,
        ModelType.CLAUDE: 0.95,
    }

    # Average characters per token (rough estimate)
    CHARS_PER_TOKEN = 4

    def __init__(self, model: ModelType = ModelType.GPT3):
        """Initialize TokenCounter.

        Args:
            model: The LLM model to use for token counting.
        """
        self.model = model
        self.token_ratio = self.TOKEN_RATIOS.get(model, 1.0)

    def count_tokens(self, text: str) -> int:
        """Count approximate tokens in text.

        Args:
            text: The text to count tokens for.

        Returns:
            Approximate number of tokens.
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Rough estimation: chars / avg_chars_per_token
        token_count = max(1, len(text) // self.CHARS_PER_TOKEN)
        
        # Apply model-specific ratio
        return int(token_count * self.token_ratio)

    def count_tokens_in_messages(self, messages: List[Dict[str, str]]) -> int:
        """Count tokens in a list of messages.

        Args:
            messages: List of message dictionaries with 'role' and 'content'.

        Returns:
            Total token count for all messages.
        """
        total_tokens = 0
        for message in messages:
            content = message.get('content', '')
            total_tokens += self.count_tokens(content)
            # Add overhead for message structure (role, formatting, etc.)
            total_tokens += 4
        return total_tokens

    def estimate_cost(self, tokens: int, input_cost_per_1k: float = 0.0005) -> float:
        """Estimate cost based on token count.

        Args:
            tokens: Number of tokens.
            input_cost_per_1k: Cost per 1000 tokens.

        Returns:
            Estimated cost in dollars.
        """
        return (tokens / 1000) * input_cost_per_1k

    def get_model_info(self) -> Dict[str, any]:
        """Get information about the current model.

        Returns:
            Dictionary with model information.
        """
        return {
            "model": self.model.value,
            "token_ratio": self.token_ratio,
            "chars_per_token": self.CHARS_PER_TOKEN,
        }