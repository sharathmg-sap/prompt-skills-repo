# Prompt Optimization Skill

**Version**: 1.0  
**Author**: Sharath M G  
**Date**: 2026-08-24  
**Status**: Stable  
**Tags**: prompt-optimization, token-efficiency, nlp, prompt-engineering

## Overview

The Prompt Optimization skill enables agents to automatically optimize, analyze, and validate prompts for better efficiency, lower token costs, and improved quality. This skill leverages the `prompt-token-optimizer` Python package to provide comprehensive prompt analysis and optimization capabilities.

## Purpose

This skill addresses the critical need to:
- Reduce token consumption and associated costs
- Maintain semantic meaning while improving efficiency
- Validate prompt quality and safety
- Provide actionable optimization suggestions
- Analyze prompt structure and intent

## Use Cases

1. **Cost Optimization** - Reduce LLM API costs by minimizing token usage
2. **Quality Assurance** - Validate prompts before deployment
3. **Performance Analysis** - Understand prompt structure and effectiveness
4. **Prompt Engineering** - Get data-driven suggestions for improvement
5. **Batch Processing** - Optimize multiple prompts efficiently
6. **Token Budgeting** - Estimate and manage token allocation

## Key Capabilities

### 1. Token Counting
- Count approximate tokens for various LLM models (GPT-3, GPT-4, Claude)
- Estimate costs based on token consumption
- Analyze token usage patterns

### 2. Prompt Optimization
- Compress prompts while maintaining semantic meaning
- Remove redundant and filler words
- Optimize message conversations
- Target-based token reduction

### 3. Semantic Analysis
- Extract keywords and key phrases
- Calculate vocabulary diversity
- Analyze prompt structure
- Detect intent and purpose

### 4. Validation
- Validate prompt length and structure
- Check encoding and special characters
- Verify word count requirements
- Generate validation reports

### 5. Optimization Suggestions
- Identify redundancy issues
- Detect filler words
- Suggest length optimizations
- Provide actionable recommendations

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

```bash
# Clone the prompt-token-optimizer repository
git clone https://github.com/sharathmg-sap/prompt-token-optimizer.git
cd prompt-token-optimizer

# Install the package
pip install -e .

# Verify installation
promptopt --help
```

### Quick Start

```python
from promptopt import PromptOptimizer, TokenCounter
from promptopt.token_counter import ModelType

# Initialize components
optimizer = PromptOptimizer(ModelType.GPT3)
counter = TokenCounter(ModelType.GPT3)
```

## Implementation Details

### Available Python Modules

The skill uses these core modules:

1. **`token_counter.py`** - Token counting and cost estimation
2. **`optimizer.py`** - Prompt compression and optimization
3. **`semantic.py`** - Semantic analysis and structure analysis
4. **`validators.py`** - Comprehensive validation
5. **`cli.py`** - Command-line interface

### Input Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| prompt | string | Yes | The prompt text to optimize |
| model | ModelType | No | LLM model (default: GPT3) |
| target_reduction | float | No | Target token reduction percentage (0-1, default: 0.2) |
| output_format | string | No | Format for results (json/text, default: json) |

### Output Format

```json
{
  "status": "success",
  "original_tokens": 150,
  "optimized_tokens": 120,
  "reduction_percentage": 20.0,
  "optimized_prompt": "Optimized text here...",
  "suggestions": [
    {
      "type": "redundancy",
      "message": "Some words appear frequently",
      "impact": "medium"
    }
  ],
  "metadata": {
    "model": "gpt-3.5-turbo",
    "duration_ms": 45
  }
}
```

## Workflow & Step-by-Step Process

### Step 1: Validate Input
```python
from promptopt.validators import PromptValidator

validator = PromptValidator()
is_valid, errors = validator.validate_all(prompt)

if not is_valid:
    print("Validation errors:", errors)
    return
```

### Step 2: Count Original Tokens
```python
from promptopt.token_counter import TokenCounter, ModelType

counter = TokenCounter(ModelType.GPT3)
original_tokens = counter.count_tokens(prompt)
print(f"Original tokens: {original_tokens}")
```

### Step 3: Analyze Semantics
```python
from promptopt.semantic import SemanticAnalyzer

analyzer = SemanticAnalyzer()
analysis = analyzer.get_semantic_analysis(prompt)
print("Keywords:", analysis['keywords'])
print("Intent:", analysis['intent']['primary_intent'])
```

### Step 4: Optimize Prompt
```python
from promptopt.optimizer import PromptOptimizer

optimizer = PromptOptimizer(ModelType.GPT3)
optimized = optimizer.compress_prompt(prompt, target_token_reduction=0.2)
optimized_tokens = counter.count_tokens(optimized)

print(f"Optimized tokens: {optimized_tokens}")
print(f"Reduction: {((original_tokens - optimized_tokens) / original_tokens) * 100}%")
```

### Step 5: Get Suggestions
```python
suggestions = optimizer.get_optimization_suggestions(prompt)
for suggestion in suggestions:
    print(f"[{suggestion['impact']}] {suggestion['message']}")
```

## Usage Examples

### Example 1: Basic Token Counting

**Objective**: Count tokens in a prompt for cost estimation

```python
from promptopt.token_counter import TokenCounter, ModelType

prompt = """You are a helpful assistant. Please analyze this document 
and provide a comprehensive summary with key points."""

counter = TokenCounter(ModelType.GPT3)
tokens = counter.count_tokens(prompt)
cost = counter.estimate_cost(tokens, input_cost_per_1k=0.0005)

print(f"Tokens: {tokens}")
print(f"Estimated cost: ${cost:.4f}")
```

### Example 2: Optimize a Long Prompt

**Objective**: Reduce token usage while maintaining meaning

```python
from promptopt.optimizer import PromptOptimizer
from promptopt.token_counter import TokenCounter, ModelType

original_prompt = """Please, I am really requesting you to very carefully 
and thoroughly analyze and evaluate this important document. I need you to 
be very detailed and very specific in your analysis and provide very helpful 
and constructive suggestions."""

optimizer = PromptOptimizer(ModelType.GPT3)
optimized = optimizer.compress_prompt(original_prompt, target_token_reduction=0.25)

counter = TokenCounter(ModelType.GPT3)
original_tokens = counter.count_tokens(original_prompt)
optimized_tokens = counter.count_tokens(optimized)

print(f"Original: {original_tokens} tokens")
print(f"Optimized: {optimized_tokens} tokens")
print(f"Reduction: {((original_tokens - optimized_tokens) / original_tokens) * 100:.1f}%")
print(f"\nOptimized prompt:\n{optimized}")
```

### Example 3: Validate Multiple Prompts

**Objective**: Batch validate prompts before deployment

```python
from promptopt.validators import PromptValidator

validator = PromptValidator()

prompts = [
    "Valid prompt with sufficient content and structure.",
    "Short",  # Too short
    "!!!###@@@",  # Invalid characters
]

for prompt in prompts:
    report = validator.get_validation_report(prompt)
    status = "✓ Valid" if report['is_valid'] else "✗ Invalid"
    print(f"{status}: {prompt[:40]}")
    if report['errors']:
        for error in report['errors']:
            print(f"  - {error}")
```

### Example 4: Semantic Analysis

**Objective**: Understand prompt structure and intent

```python
from promptopt.semantic import SemanticAnalyzer

analyzer = SemanticAnalyzer()
prompt = "What are the benefits of machine learning and how does it differ from traditional programming?"

analysis = analyzer.get_semantic_analysis(prompt)

print("Keywords:", analysis['keywords'][:5])
print("Diversity:", f"{analysis['diversity']:.2%}")
print("Intent:", analysis['intent']['primary_intent'])
print("Structure:", analysis['structure'])
```

### Example 5: Optimize Conversations

**Objective**: Optimize multi-turn conversations

```python
from promptopt.optimizer import PromptOptimizer

optimizer = PromptOptimizer()

messages = [
    {
        "role": "user",
        "content": "I really need your help with understanding machine learning concepts very thoroughly."
    },
    {
        "role": "assistant",
        "content": "Machine learning is a very important and crucial field in artificial intelligence."
    }
]

optimized_messages, stats = optimizer.optimize_messages(messages)

print(f"Original tokens: {stats['original_tokens']}")
print(f"Optimized tokens: {stats['optimized_tokens']}")
print(f"Reduction: {stats['reduction_percentage']:.1f}%")
```

## Command-Line Interface

The skill provides CLI commands for quick operations:

```bash
# Count tokens
promptopt count "Your prompt here" --model gpt-3.5-turbo

# Optimize prompt
promptopt optimize "Your long prompt" --reduction 0.2 --output optimized.txt

# Validate prompt
promptopt validate "Your prompt here"

# Analyze semantics
promptopt analyze "Your prompt here"

# Get suggestions
promptopt suggest "Your prompt here"
```

## Error Handling

```python
from promptopt.validators import PromptValidator
from promptopt.optimizer import PromptOptimizer

try:
    validator = PromptValidator()
    is_valid, errors = validator.validate_all(prompt)
    
    if not is_valid:
        raise ValueError(f"Validation failed: {errors}")
    
    optimizer = PromptOptimizer()
    result = optimizer.compress_prompt(prompt)
    
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"Optimization error: {e}")
```

## Configuration Options

### Customize Validation Rules

```python
from promptopt.validators import PromptValidator

custom_rules = {
    'min_length': 20,
    'max_length': 50000,
    'min_words': 5,
    'max_special_chars_ratio': 0.25,
}

validator = PromptValidator(rules=custom_rules)
```

### Select Different Models

```python
from promptopt.token_counter import TokenCounter, ModelType

# Different model options
counter_gpt3 = TokenCounter(ModelType.GPT3)
counter_gpt4 = TokenCounter(ModelType.GPT4)
counter_claude = TokenCounter(ModelType.CLAUDE)
```

## Performance Characteristics

- **Token Counting**: O(n) where n is text length, ~5ms per 1000 tokens
- **Optimization**: O(n) for compression, ~50ms for typical prompts
- **Validation**: O(n) for all checks, ~10ms per prompt
- **Semantic Analysis**: O(n) for keyword extraction, ~30ms per prompt

## Supported LLM Models

| Model | Identifier | Token Ratio |
|-------|-----------|------------|
| GPT-3.5 Turbo | GPT3 | 1.0 |
| GPT-4 | GPT4 | 1.0 |
| Claude | CLAUDE | 0.95 |
| Custom | CUSTOM | 1.0 |

## Best Practices

1. **Always Validate First**
   ```python
   is_valid, errors = validator.validate_all(prompt)
   if not is_valid:
       return errors
   ```

2. **Incremental Optimization**
   - Start with 10-20% reduction target
   - Test output quality before increasing reduction

3. **Monitor Token Changes**
   - Always compare before/after token counts
   - Ensure semantic meaning is preserved

4. **Use Intent Detection**
   - Understand prompt purpose before optimizing
   - Preserve intent-critical phrases

5. **Batch Processing**
   - For multiple prompts, use batch optimization
   - Calculate savings and costs in aggregate

## Testing

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest --cov=promptopt tests/

# Run specific test
pytest tests/test_optimizer.py::TestPromptOptimizer::test_compress_prompt
```

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Token count too high | Verbose prompt | Use `compress_prompt()` with higher reduction |
| Meaning lost after optimization | Too aggressive reduction | Lower target_token_reduction (e.g., 0.1) |
| Validation fails | Invalid characters | Use `validate_special_characters()` first |
| Cost estimation inaccurate | Model mismatch | Select correct ModelType for your LLM |

## Limitations

- Token counts are approximate (±5-10% variance)
- Optimization preserves semantic meaning but may change style
- Special characters in structured data may be preserved
- Some domain-specific terminology may not be optimized

## Future Enhancements

- Integration with actual tokenizers (tiktoken)
- Multi-language support
- Custom semantic preservation rules
- Advanced compression algorithms
- Real-time optimization dashboard

## Related Resources

- [Prompt Skills Repo](../../../README.md)
- [Token Counter Module](https://github.com/sharathmg-sap/prompt-token-optimizer/blob/main/promptopt/token_counter.py)
- [Optimizer Module](https://github.com/sharathmg-sap/prompt-token-optimizer/blob/main/promptopt/optimizer.py)
- [Semantic Analysis Module](https://github.com/sharathmg-sap/prompt-token-optimizer/blob/main/promptopt/semantic.py)

## Troubleshooting

### Installation Issues

```bash
# Ensure Python 3.8+
python --version

# Upgrade pip
pip install --upgrade pip

# Install with verbose output
pip install -e . -v
```

### Import Errors

```python
# Verify package installation
pip show prompt-token-optimizer

# Check Python path
import sys
print(sys.path)

# Try direct import
from promptopt import PromptOptimizer
```

## Support & Feedback

- Report issues: [GitHub Issues](https://github.com/sharathmg-sap/prompt-token-optimizer/issues)
- Contribute: [GitHub Repository](https://github.com/sharathmg-sap/prompt-token-optimizer)
- Questions: Check [documentation](https://github.com/sharathmg-sap/prompt-token-optimizer/blob/main/README.md)

---

**Status**: Production Ready  
**Last Updated**: 2026-08-24  
**Maintenance**: Active Development