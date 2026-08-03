"""
Unified AI Pipeline

This module provides a single interface to initialize
all AI models used in the Smart Retail platform.
"""

from app.startup import load_models


class SmartRetailPipeline:

    def __init__(self):
        self.models_loaded = False

    def initialize(self):
        """
        Load every AI model once.
        """

        if not self.models_loaded:
            load_models()
            self.models_loaded = True
            print("✅ Smart Retail Pipeline Initialized Successfully")

    def status(self):
        return {
            "pipeline": "Running",
            "models_loaded": self.models_loaded
        }


pipeline = SmartRetailPipeline()