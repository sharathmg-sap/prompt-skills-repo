"""Prompt validation utilities."""

from typing import Dict, List
import re


class PromptValidator:
    """Validate prompts for quality and best practices."""

    # Validation rules
    RULES = {
        'min_length': 10,
        'max_length': 100000,
        'min_words': 1,
        'max_special_chars_ratio': 0.3,
    }

    def __init__(self, rules: Dict = None):
        """Initialize PromptValidator.

        Args:
            rules: Custom validation rules.
        """
        if rules:
            self.RULES.update(rules)

    def validate_length(self, text: str) -> tuple[bool, str]:
        """Validate text length.

        Args:
            text: The text to validate.

        Returns:
            Tuple of (is_valid, message).
        """
        length = len(text)
        if length < self.RULES['min_length']:
            return False, f"Text too short. Minimum {self.RULES['min_length']} characters."
        if length > self.RULES['max_length']:
            return False, f"Text too long. Maximum {self.RULES['max_length']} characters."
        return True, "Length is valid."

    def validate_word_count(self, text: str) -> tuple[bool, str]:
        """Validate word count.

        Args:
            text: The text to validate.

        Returns:
            Tuple of (is_valid, message).
        """
        words = text.split()
        if len(words) < self.RULES['min_words']:
            return False, f"Too few words. Minimum {self.RULES['min_words']} word(s)."
        return True, "Word count is valid."

    def validate_special_characters(self, text: str) -> tuple[bool, str]:
        """Validate special character ratio.

        Args:
            text: The text to validate.

        Returns:
            Tuple of (is_valid, message).
        """
        if not text:
            return False, "Text is empty."
        
        special_chars = len(re.findall(r'[^a-zA-Z0-9\s]', text))
        ratio = special_chars / len(text)
        
        max_ratio = self.RULES['max_special_chars_ratio']
        if ratio > max_ratio:
            return False, f"Too many special characters. Ratio: {ratio:.2%}. Maximum: {max_ratio:.2%}"
        return True, "Special character ratio is valid."

    def validate_encoding(self, text: str) -> tuple[bool, str]:
        """Validate text encoding.

        Args:
            text: The text to validate.

        Returns:
            Tuple of (is_valid, message).
        """
        try:
            text.encode('utf-8')
            return True, "Encoding is valid."
        except UnicodeEncodeError:
            return False, "Text contains invalid UTF-8 characters."

    def validate_no_empty_lines(self, text: str) -> tuple[bool, str]:
        """Validate that text doesn't have excessive empty lines.

        Args:
            text: The text to validate.

        Returns:
            Tuple of (is_valid, message).
        """
        lines = text.split('\n')
        empty_lines = len([l for l in lines if not l.strip()])
        ratio = empty_lines / len(lines) if lines else 0
        
        if ratio > 0.5:
            return False, f"Too many empty lines. Ratio: {ratio:.2%}"
        return True, "Line structure is valid."

    def validate_all(self, text: str) -> tuple[bool, List[str]]:
        """Run all validations.

        Args:
            text: The text to validate.

        Returns:
            Tuple of (all_valid, list_of_error_messages).
        """
        errors = []
        
        validators = [
            self.validate_length,
            self.validate_word_count,
            self.validate_special_characters,
            self.validate_encoding,
            self.validate_no_empty_lines,
        ]
        
        for validator in validators:
            is_valid, message = validator(text)
            if not is_valid:
                errors.append(message)
        
        return len(errors) == 0, errors

    def get_validation_report(self, text: str) -> Dict:
        """Get detailed validation report.

        Args:
            text: The text to validate.

        Returns:
            Dictionary with validation report.
        """
        all_valid, errors = self.validate_all(text)
        
        return {
            'is_valid': all_valid,
            'errors': errors,
            'checks': {
                'length': self.validate_length(text),
                'word_count': self.validate_word_count(text),
                'special_characters': self.validate_special_characters(text),
                'encoding': self.validate_encoding(text),
                'line_structure': self.validate_no_empty_lines(text),
            }
        }