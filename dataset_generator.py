#!/usr/bin/env python3
"""
Dataset Generator for Python Programming Topics

This script generates educational programming prompts datasets that can be used
for training purposes or educational platforms. It supports both JSON and CSV
output formats and allows customization of the dataset size.
"""

import random
import json
import csv
from typing import List, Dict, Any
from datetime import datetime
from categories_data import CATEGORIES, PROMPT_TEMPLATES, DESCRIPTIONS

class DatasetGenerator:
    """
    Handles the generation of programming topic datasets with customizable size
    and output formats.
    """
    
    def __init__(self):
        """Initialize the dataset generator with predefined categories and templates."""
        self.categories = CATEGORIES
        self.prompt_templates = PROMPT_TEMPLATES
        self.descriptions = DESCRIPTIONS

    def generate_single_entry(self) -> Dict[str, str]:
        """
        Generate a single dataset entry with random category and prompt.
        
        Returns:
            Dict containing prompt, category, and description
        """
        category = random.choice(self.categories)
        prompt = random.choice(self.prompt_templates[category])
        
        return {
            "prompt": prompt,
            "category": category,
            "description": self.descriptions[category]
        }

    def generate_dataset(self, num_entries: int = 100) -> List[Dict[str, str]]:
        """
        Generate a dataset with the specified number of entries.
        
        Args:
            num_entries: Number of entries to generate (default: 100)
            
        Returns:
            List of dictionaries containing the generated dataset
        """
        if num_entries <= 0:
            raise ValueError("Number of entries must be positive")
            
        return [self.generate_single_entry() for _ in range(num_entries)]

    def save_json(self, dataset: List[Dict[str, str]], filename: str = None) -> str:
        """
        Save the dataset in JSON format.
        
        Args:
            dataset: The dataset to save
            filename: Optional custom filename
            
        Returns:
            The filename used for saving
        """
        if filename is None:
            filename = f"python_prompts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump({"prompts": dataset, 
                      "metadata": {
                          "generated_at": datetime.now().isoformat(),
                          "entry_count": len(dataset)
                      }}, 
                     json_file, 
                     indent=2)
        return filename

    def save_csv(self, dataset: List[Dict[str, str]], filename: str = None) -> str:
        """
        Save the dataset in CSV format.
        
        Args:
            dataset: The dataset to save
            filename: Optional custom filename
            
        Returns:
            The filename used for saving
        """
        if filename is None:
            filename = f"python_prompts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["prompt", "category", "description"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
        return filename

def main():
    """Main function to demonstrate dataset generation and saving."""
    try:
        # Initialize generator
        generator = DatasetGenerator()
        
        # Generate dataset
        print("Generating dataset...")
        dataset = generator.generate_dataset(100)
        
        # Save in both formats
        json_file = generator.save_json(dataset)
        csv_file = generator.save_csv(dataset)
        
        print(f"Dataset generated successfully!")
        print(f"Files saved:")
        print(f"- JSON: {json_file}")
        print(f"- CSV: {csv_file}")
        
    except Exception as e:
        print(f"Error generating dataset: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
