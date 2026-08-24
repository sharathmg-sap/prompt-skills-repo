# Skill Template

Use this template as a starting point when creating new skills.

---

# [Skill Name]

**Version**: 1.0  
**Author**: [Your Name]  
**Date**: [Date Created]  
**Last Updated**: [Date]  
**Status**: [Development/Beta/Stable]  
**Tags**: [tag1, tag2, tag3]

## Overview

Brief description of the skill and what it enables.

## Skill Definition

### Purpose
Clear statement of what this skill accomplishes.

### Use Cases
When and why would an agent use this skill?

- Use case 1
- Use case 2
- Use case 3

### Capabilities
What specific capabilities does this skill provide?

- Capability 1
- Capability 2
- Capability 3

## Input Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| param1 | string | Yes | Description |
| param2 | number | No | Description |
| param3 | boolean | No | Default: false |

## Output Format

Describe the expected output structure.

```json
{
  "status": "success",
  "result": {
    "key1": "value1",
    "key2": "value2"
  },
  "metadata": {
    "duration_ms": 100,
    "version": "1.0"
  }
}
```

## Dependencies

List any external dependencies:

- Dependency 1 (version X.X)
- Dependency 2 (version X.X)
- System requirement

## Implementation

### Algorithm/Logic

Step-by-step explanation of how the skill works:

1. Step 1: Description
2. Step 2: Description
3. Step 3: Description

### Code Example (Python)

```python
def skill_function(param1, param2=None):
    """
    Description of what the function does.
    
    Args:
        param1 (str): Description
        param2 (str, optional): Description
    
    Returns:
        dict: Result with status and data
    """
    # Implementation here
    result = {
        "status": "success",
        "result": {},
        "metadata": {}
    }
    return result
```

### Configuration

Any configuration options or settings:

```python
CONFIG = {
    "timeout": 30,
    "retry_attempts": 3,
    "debug": False
}
```

## Error Handling

How the skill handles errors:

| Error Type | Cause | Solution |
|-----------|-------|----------|
| ValueError | Invalid input | Validate parameters |
| TimeoutError | Slow response | Increase timeout |
| RuntimeError | Processing failure | Check dependencies |

## Usage Examples

### Example 1: Basic Usage

**Input**:
```python
result = skill_function("param1_value")
```

**Output**:
```json
{
  "status": "success",
  "result": {}
}
```

### Example 2: With Optional Parameters

**Input**:
```python
result = skill_function("param1_value", param2="param2_value")
```

**Output**:
```json
{
  "status": "success",
  "result": {}
}
```

### Example 3: Error Handling

**Input**:
```python
try:
    result = skill_function("")  # Invalid input
except ValueError as e:
    print(f"Error: {e}")
```

## Performance Characteristics

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Typical Duration**: ~100ms
- **Throughput**: X requests/second

## Testing

### Unit Tests

```python
def test_basic_functionality():
    result = skill_function("test_input")
    assert result["status"] == "success"

def test_error_handling():
    with pytest.raises(ValueError):
        skill_function("")
```

### Test Coverage
- Happy path: ✓
- Edge cases: ✓
- Error conditions: ✓

## Known Limitations

- Limitation 1
- Limitation 2
- Known issue and workaround

## Best Practices

When using this skill:

1. Best practice 1
2. Best practice 2
3. Best practice 3

## Security Considerations

- Security consideration 1
- Input validation requirements
- Output sanitization

## Related Resources

Links to related skills and documentation:

- [Related Skill 1](../skill-name)
- [Related Prompt](../../prompts/related-prompt-v1.md)
- [Documentation](../../docs/ARCHITECTURE.md)

## Troubleshooting

**Issue**: [Problem]  
**Symptom**: [What you observe]  
**Solution**: [How to fix]

---

**Example with Details**:

**Issue**: Function returns timeout error  
**Symptom**: Always fails after 30 seconds  
**Solution**: Increase timeout in CONFIG or optimize input

## Changelog

### v1.0
- Initial skill implementation

### v1.1
- Performance improvement description

## Future Enhancements

Potential improvements or extensions:

- Enhancement 1
- Enhancement 2

## Feedback

For feedback or improvements:
1. Open an issue
2. Submit a pull request
3. Contact the maintainer

---

**Status**: Ready for use  
**Last Reviewed**: [Date]  
**Maintenance**: [Who maintains this]
