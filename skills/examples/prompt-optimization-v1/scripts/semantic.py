"""Semantic analysis for prompts."""

from typing import Dict, List, Tuple
import re
from collections import Counter


class SemanticAnalyzer:
    """Analyze semantic properties of prompts."""

    def __init__(self):
        """Initialize SemanticAnalyzer."""
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be', 'been',
            'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
            'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
        }

    def extract_keywords(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """Extract keywords from text.

        Args:
            text: The text to analyze.
            top_n: Number of top keywords to return.

        Returns:
            List of (keyword, frequency) tuples.
        """
        # Convert to lowercase and split into words
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Filter out stop words
        filtered_words = [w for w in words if w not in self.stop_words and len(w) > 2]
        
        # Count frequencies
        word_freq = Counter(filtered_words)
        
        return word_freq.most_common(top_n)

    def calculate_diversity(self, text: str) -> float:
        """Calculate vocabulary diversity (Type-Token Ratio).

        Args:
            text: The text to analyze.

        Returns:
            Diversity score between 0 and 1.
        """
        words = re.findall(r'\b\w+\b', text.lower())
        
        if not words:
            return 0.0
        
        unique_words = len(set(words))
        total_words = len(words)
        
        return unique_words / total_words

    def analyze_prompt_structure(self, prompt: str) -> Dict:
        """Analyze the structure of a prompt.

        Args:
            prompt: The prompt to analyze.

        Returns:
            Dictionary with structural analysis.
        """
        lines = prompt.split('\n')
        sentences = re.split(r'[.!?]+', prompt)
        words = prompt.split()
        
        return {
            'line_count': len([l for l in lines if l.strip()]),
            'sentence_count': len([s for s in sentences if s.strip()]),
            'word_count': len(words),
            'avg_words_per_line': len(words) / max(1, len([l for l in lines if l.strip()])),
            'avg_words_per_sentence': len(words) / max(1, len([s for s in sentences if s.strip()])),
        }

    def detect_intent(self, prompt: str) -> Dict[str, any]:
        """Detect the primary intent of a prompt.

        Args:
            prompt: The prompt to analyze.

        Returns:
            Dictionary with detected intent information.
        """
        intent_keywords = {
            'question': ['what', 'how', 'why', 'when', 'where', 'who', 'is', '?'],
            'instruction': ['please', 'help', 'show', 'create', 'write', 'generate', 'make', 'do'],
            'analysis': ['analyze', 'explain', 'describe', 'discuss', 'evaluate', 'compare'],
            'creative': ['imagine', 'create', 'story', 'poem', 'idea', 'brainstorm'],
        }
        
        prompt_lower = prompt.lower()
        intent_scores = {}
        
        for intent, keywords in intent_keywords.items():
            score = sum(prompt_lower.count(kw) for kw in keywords)
            intent_scores[intent] = score
        
        primary_intent = max(intent_scores, key=intent_scores.get)
        
        return {
            'primary_intent': primary_intent,
            'scores': intent_scores,
            'confidence': intent_scores[primary_intent] / max(1, sum(intent_scores.values())),
        }

    def get_semantic_analysis(self, prompt: str) -> Dict:
        """Get comprehensive semantic analysis.

        Args:
            prompt: The prompt to analyze.

        Returns:
            Dictionary with complete semantic analysis.
        """
        return {
            'keywords': self.extract_keywords(prompt),
            'diversity': self.calculate_diversity(prompt),
            'structure': self.analyze_prompt_structure(prompt),
            'intent': self.detect_intent(prompt),
        }