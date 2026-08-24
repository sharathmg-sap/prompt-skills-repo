"""Integration module for prompt optimization skill."""

import json
from typing import Dict, Any

from token_counter import TokenCounter, ModelType
from optimizer import PromptOptimizer
from semantic import SemanticAnalyzer
from validators import PromptValidator


class PromptOptimizationSkill:
    """Complete prompt optimization skill integrating all modules."""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """Initialize the skill with all components.
        
        Args:
            model: LLM model to use (gpt-3.5-turbo, gpt-4, claude)
        """
        model_map = {
            "gpt-3.5-turbo": ModelType.GPT3,
            "gpt-4": ModelType.GPT4,
            "claude": ModelType.CLAUDE,
        }
        self.model = model_map.get(model, ModelType.GPT3)
        
        self.token_counter = TokenCounter(self.model)
        self.optimizer = PromptOptimizer(self.model)
        self.analyzer = SemanticAnalyzer()
        self.validator = PromptValidator()
    
    def count_tokens(self, prompt: str) -> Dict[str, Any]:
        """Count tokens in a prompt.
        
        Args:
            prompt: The prompt text
            
        Returns:
            Dictionary with token count and cost estimation
        """
        is_valid, errors = self.validator.validate_all(prompt)
        if not is_valid:
            return {"status": "error", "errors": errors}
        
        tokens = self.token_counter.count_tokens(prompt)
        cost = self.token_counter.estimate_cost(tokens)
        
        return {
            "status": "success",
            "tokens": tokens,
            "estimated_cost": f"${cost:.4f}",
            "model": self.model.value,
        }
    
    def optimize(self, prompt: str, target_reduction: float = 0.2) -> Dict[str, Any]:
        """Optimize a prompt.
        
        Args:
            prompt: The prompt to optimize
            target_reduction: Target token reduction (0-1)
            
        Returns:
            Dictionary with optimization results
        """
        is_valid, errors = self.validator.validate_all(prompt)
        if not is_valid:
            return {"status": "error", "errors": errors}
        
        original_tokens = self.token_counter.count_tokens(prompt)
        optimized_prompt = self.optimizer.compress_prompt(prompt, target_reduction)
        optimized_tokens = self.token_counter.count_tokens(optimized_prompt)
        
        reduction_pct = ((original_tokens - optimized_tokens) / original_tokens) * 100
        
        return {
            "status": "success",
            "original_tokens": original_tokens,
            "optimized_tokens": optimized_tokens,
            "reduction_percentage": round(reduction_pct, 2),
            "optimized_prompt": optimized_prompt,
            "model": self.model.value,
        }
    
    def validate(self, prompt: str) -> Dict[str, Any]:
        """Validate a prompt.
        
        Args:
            prompt: The prompt to validate
            
        Returns:
            Dictionary with validation report
        """
        report = self.validator.get_validation_report(prompt)
        return {
            "status": "success" if report['is_valid'] else "error",
            "is_valid": report['is_valid'],
            "errors": report['errors'],
            "checks": {k: v[0] for k, v in report['checks'].items()}
        }
    
    def analyze(self, prompt: str) -> Dict[str, Any]:
        """Analyze prompt semantics.
        
        Args:
            prompt: The prompt to analyze
            
        Returns:
            Dictionary with semantic analysis
        """
        is_valid, errors = self.validator.validate_all(prompt)
        if not is_valid:
            return {"status": "error", "errors": errors}
        
        analysis = self.analyzer.get_semantic_analysis(prompt)
        
        return {
            "status": "success",
            "keywords": analysis['keywords'],
            "diversity": round(analysis['diversity'], 3),
            "intent": analysis['intent']['primary_intent'],
            "intent_confidence": round(analysis['intent']['confidence'], 3),
            "structure": analysis['structure'],
        }
    
    def suggest(self, prompt: str) -> Dict[str, Any]:
        """Get optimization suggestions.
        
        Args:
            prompt: The prompt to analyze
            
        Returns:
            Dictionary with suggestions
        """
        is_valid, errors = self.validator.validate_all(prompt)
        if not is_valid:
            return {"status": "error", "errors": errors}
        
        suggestions = self.optimizer.get_optimization_suggestions(prompt)
        
        return {
            "status": "success",
            "suggestions": suggestions,
            "suggestion_count": len(suggestions),
        }
    
    def full_analysis(self, prompt: str, target_reduction: float = 0.2) -> Dict[str, Any]:
        """Perform complete analysis and optimization.
        
        Args:
            prompt: The prompt to analyze
            target_reduction: Target token reduction
            
        Returns:
            Dictionary with complete results
        """
        # Validate first
        validation = self.validate(prompt)
        if validation["status"] == "error":
            return validation
        
        return {
            "status": "success",
            "token_count": self.count_tokens(prompt),
            "optimization": self.optimize(prompt, target_reduction),
            "analysis": self.analyze(prompt),
            "suggestions": self.suggest(prompt)["suggestions"],
        }


if __name__ == "__main__":
    # Example usage
    skill = PromptOptimizationSkill(model="gpt-3.5-turbo")
    
    prompt = """Please, I am really requesting you to very carefully 
    and thoroughly analyze and evaluate this important document. 
    I need you to be very detailed and very specific in your analysis."""
    
    print("Token Count:")
    print(json.dumps(skill.count_tokens(prompt), indent=2))
    
    print("\nOptimization:")
    print(json.dumps(skill.optimize(prompt, target_reduction=0.2), indent=2))
    
    print("\nAnalysis:")
    print(json.dumps(skill.analyze(prompt), indent=2, default=str))
    
    print("\nSuggestions:")
    print(json.dumps(skill.suggest(prompt), indent=2))