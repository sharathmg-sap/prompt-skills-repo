"""Prompt optimization utilities."""

from typing import Dict, List, Optional, Tuple
from enum import Enum
import re


class ModelType(Enum):
    """Supported LLM models for token counting."""
    GPT3 = "gpt-3.5-turbo"
    GPT4 = "gpt-4"
    CLAUDE = "claude"
    CUSTOM = "custom"


class TokenCounter:
    """Count tokens in prompts for different LLM models."""

    TOKEN_RATIOS = {
        ModelType.GPT3: 1.0,
        ModelType.GPT4: 1.0,
        ModelType.CLAUDE: 0.95,
    }
    CHARS_PER_TOKEN = 4

    def __init__(self, model: ModelType = ModelType.GPT3):
        self.model = model
        self.token_ratio = self.TOKEN_RATIOS.get(model, 1.0)

    def count_tokens(self, text: str) -> int:
        text = re.sub(r'\s+', ' ', text.strip())
        token_count = max(1, len(text) // self.CHARS_PER_TOKEN)
        return int(token_count * self.token_ratio)

    def count_tokens_in_messages(self, messages: List[Dict[str, str]]) -> int:
        total_tokens = 0
        for message in messages:
            content = message.get('content', '')
            total_tokens += self.count_tokens(content)
            total_tokens += 4
        return total_tokens


class PromptOptimizer:
    """Optimize prompts for token efficiency."""

    def __init__(self, model: ModelType = ModelType.GPT3):
        """Initialize PromptOptimizer.

        Args:
            model: The LLM model to optimize for.
        """
        self.token_counter = TokenCounter(model)
        self.model = model

    def compress_prompt(self, prompt: str, target_token_reduction: float = 0.2) -> str:
        """Compress prompt while maintaining meaning.

        Args:
            prompt: The prompt to compress.
            target_token_reduction: Target reduction percentage (0-1).

        Returns:
            Compressed prompt.
        """
        original_tokens = self.token_counter.count_tokens(prompt)
        target_tokens = int(original_tokens * (1 - target_token_reduction))
        
        # Simple compression strategy: remove common filler words
        filler_words = {'very', 'really', 'quite', 'basically', 'essentially', 'just'}
        
        words = prompt.split()
        compressed = [w for w in words if w.lower() not in filler_words]
        
        compressed_text = ' '.join(compressed)
        
        # Verify we hit target
        compressed_tokens = self.token_counter.count_tokens(compressed_text)
        
        return compressed_text

    def optimize_messages(self, messages: List[Dict[str, str]]) -> Tuple[List[Dict[str, str]], Dict]:
        """Optimize a list of messages.

        Args:
            messages: List of message dictionaries.

        Returns:
            Tuple of (optimized_messages, optimization_stats).
        """
        original_tokens = self.token_counter.count_tokens_in_messages(messages)
        optimized_messages = []
        
        for message in messages:
            optimized_msg = message.copy()
            optimized_msg['content'] = self.compress_prompt(message['content'], target_token_reduction=0.1)
            optimized_messages.append(optimized_msg)
        
        optimized_tokens = self.token_counter.count_tokens_in_messages(optimized_messages)
        
        stats = {
            'original_tokens': original_tokens,
            'optimized_tokens': optimized_tokens,
            'reduction_percentage': ((original_tokens - optimized_tokens) / original_tokens) * 100,
            'savings': original_tokens - optimized_tokens,
        }
        
        return optimized_messages, stats

    def get_optimization_suggestions(self, prompt: str) -> List[Dict[str, str]]:
        """Get suggestions for optimizing a prompt.

        Args:
            prompt: The prompt to analyze.

        Returns:
            List of optimization suggestions.
        """
        suggestions = []
        
        # Check for redundancy
        words = prompt.split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        if max(word_freq.values()) > 3:
            suggestions.append({
                'type': 'redundancy',
                'message': 'Some words appear frequently. Consider using synonyms or removing repetition.',
                'impact': 'medium',
            })
        
        # Check for common filler words
        filler_words = {'very', 'really', 'quite', 'basically', 'essentially', 'just'}
        filler_count = sum(1 for w in words if w.lower() in filler_words)
        
        if filler_count > 0:
            suggestions.append({
                'type': 'filler_words',
                'message': f'Found {filler_count} filler words. Removing them can reduce tokens.',
                'impact': 'low',
            })
        
        # Check length
        tokens = self.token_counter.count_tokens(prompt)
        if tokens > 1000:
            suggestions.append({
                'type': 'length',
                'message': 'Prompt is quite long. Consider breaking it into smaller prompts.',
                'impact': 'high',
            })
        
        return suggestions