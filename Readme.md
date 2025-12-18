# Intelligent Answer Evaluation System

## Problem Statement
Manual evaluation of descriptive answers is time-consuming and subjective.  
This project proposes an explainable system that evaluates student answers
using semantic similarity and concept coverage analysis.

## Scope (Version 1)
- Text-based answers only
- Semantic similarity evaluation
- Keyword / concept coverage analysis
- Not creativity-based grading

## Evaluation Pipeline
1. Input collection
2. Reference answer selection
3. Text preprocessing
4. Semantic similarity computation
5. Concept / keyword coverage analysis
6. Score calculation
7. Feedback generation

## Mark Distribution
- Semantic similarity: 4 marks
- Keyword coverage: 4 marks
- Structure & grammar: 2 marks

## Design Philosophy
LLMs are probabilistic and non-deterministic.  
For academic evaluation, explainability and consistency are critical.
Hence, rule-based scoring and ML similarity are used, while LLMs act
only as a support layer.

## Future Enhancements
- Handwritten answer evaluation using OCR
- Multilingual support
- Instructor-defined rubrics
