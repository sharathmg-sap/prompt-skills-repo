#!/usr/bin/env python3
"""CLI interface for prompt optimization skill."""

import sys
import json
import argparse
from integration import PromptOptimizationSkill


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Prompt Optimization Skill - Optimize and analyze prompts"
    )
    
    parser.add_argument(
        "--model",
        choices=["gpt-3.5-turbo", "gpt-4", "claude"],
        default="gpt-3.5-turbo",
        help="LLM model to use"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Count command
    count_parser = subparsers.add_parser("count", help="Count tokens")
    count_parser.add_argument("prompt", help="Prompt text")
    
    # Optimize command
    optimize_parser = subparsers.add_parser("optimize", help="Optimize prompt")
    optimize_parser.add_argument("prompt", help="Prompt text")
    optimize_parser.add_argument(
        "--reduction",
        type=float,
        default=0.2,
        help="Target reduction percentage (0-1)"
    )
    
    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate prompt")
    validate_parser.add_argument("prompt", help="Prompt text")
    
    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze prompt")
    analyze_parser.add_argument("prompt", help="Prompt text")
    
    # Suggest command
    suggest_parser = subparsers.add_parser("suggest", help="Get suggestions")
    suggest_parser.add_argument("prompt", help="Prompt text")
    
    # Full analysis command
    full_parser = subparsers.add_parser("full", help="Complete analysis")
    full_parser.add_argument("prompt", help="Prompt text")
    full_parser.add_argument(
        "--reduction",
        type=float,
        default=0.2,
        help="Target reduction percentage (0-1)"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        skill = PromptOptimizationSkill(model=args.model)
        result = None
        
        if args.command == "count":
            result = skill.count_tokens(args.prompt)
        elif args.command == "optimize":
            result = skill.optimize(args.prompt, args.reduction)
        elif args.command == "validate":
            result = skill.validate(args.prompt)
        elif args.command == "analyze":
            result = skill.analyze(args.prompt)
        elif args.command == "suggest":
            result = skill.suggest(args.prompt)
        elif args.command == "full":
            result = skill.full_analysis(args.prompt, args.reduction)
        
        if result:
            print(json.dumps(result, indent=2, default=str))
            return 0
    
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())