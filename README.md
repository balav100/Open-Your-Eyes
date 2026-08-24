# 👁️ Open Your Eyes

### AI-Powered Braille Accessibility & Learning Platform

Open Your Eyes is an NLP-driven accessibility platform designed to help visually impaired users access digital books more effectively. The application converts uploaded PDF/TXT books into Braille text, generates audio narration, provides AI-powered summaries, evaluates readability, and offers an AI Tutor that explains book content in both plain text and Braille format.

---

## 🚀 Features

### 📚 Document Upload
- Upload PDF books
- Upload TXT files
- Automatic text extraction

### 🌍 Language Detection
- Detects the language of uploaded content
- Supports multilingual documents

### 📝 Text Preview
- Displays extracted and cleaned text
- Enables users to verify content before conversion

### ⠃ Braille Conversion
- Converts text into Unicode Braille representation
- Real-time Braille preview panel

### 📖 Accessibility Score Meter
- Evaluates readability level
- Classifies content as:
  - Easy
  - Medium
  - Advanced

### 🤖 AI Smart Summary
- Generates concise summaries of lengthy books
- Helps users quickly understand key concepts

### 🎓 AI Tutor
- Answers user questions about uploaded books
- Explains difficult concepts in simple language
- Generates explanations in Braille format

### 🔊 Audio Narration
- Converts book content into speech
- Accessible audio playback directly in the application

### 📥 Export Options
- Download Braille book as TXT
- Download Braille book as PDF

---

## 🏗️ System Architecture

```text
User Upload
      │
      ▼
Text Extraction
      │
      ▼
Text Cleaning
      │
      ▼
Language Detection
      │
      ▼
Braille Conversion
      │
      ├────────► Braille Preview
      │
      ├────────► PDF Export
      │
      └────────► TXT Export

      ▼
Readability Analysis
      ▼
Smart Summary
      ▼
AI Tutor
      ▼
Audio Narration
```

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Natural Language Processing
- Transformers
- Hugging Face Models

### OCR & Document Processing
- EasyOCR
- PDFPlumber
- PyMuPDF

### Audio Generation
- gTTS

### Accessibility Processing
- Unicode Braille Mapping

### Utilities
- Python
- TextStat
- LangDetect

---

## 📂 Project Structure

```text
open-your-eyes/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── modules/
│   ├── ai_tutor.py
│   ├── audio_generator.py
│   ├── braille_converter.py
│   ├── language_detector.py
│   ├── pdf_extractor.py
│   ├── pdf_generator.py
│   ├── readability.py
│   ├── summarizer.py
│   ├── text_cleaner.py
│   └── utils.py
│___ evaluation/
├── assets/
│   └── DejaVuSans.ttf
│
├── uploads/
└── outputs/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/open-your-eyes.git
cd open-your-eyes
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🎯 Target Users

- Visually impaired readers
- Students requiring accessible learning materials
- Educational institutions
- Accessibility researchers
- NGOs supporting inclusive education

---

## 💡 Real-World Impact

Millions of visually impaired individuals face challenges accessing digital educational content. Open Your Eyes can bridge this gap by transforming conventional digital books into accessible Braille and audio formats while leveraging AI to enhance comprehension and learning.

---

## ## 📊 Evaluation & Performance

**Open Your Eyes** includes a quantitative evaluation framework to assess the accuracy, reliability, and quality of its core **Braille, document processing, NLP, summarization, AI tutoring, and audio generation** components.

### 🏆 Overall Evaluation Results

| System Component           | Evaluation Method           | Performance |
| :------------------------- | :-------------------------- | ----------: |
| ⠃ **Braille Conversion**   | Braille Accuracy            |  **94.50%** |
| 📄 **Document Processing** | Processing Success Rate     | **100.00%** |
| 📝 **AI Smart Summary**    | ROUGE-based Evaluation      |  **55.53%** |
| 🎓 **AI Tutor**            | Semantic Similarity         |  **66.26%** |
| 🔊 **Audio Generation**    | Generation Success Rate     | **100.00%** |
| 🏆 **Overall System**      | Aggregated Evaluation Score |  **86.07%** |

### 🔬 Detailed Evaluation Metrics

#### ⠃ Braille Conversion

**Braille Accuracy: 94.50%**

Measures the correctness of the generated Unicode Braille representation against the expected Braille output. The high accuracy demonstrates reliable text-to-Braille conversion for accessibility-focused content.

#### 📝 AI Smart Summary

The summarization module was evaluated using standard **ROUGE metrics** to measure the overlap between generated summaries and reference summaries.

| Metric              |      Score |
| :------------------ | ---------: |
| **ROUGE-1**         | **0.6339** |
| **ROUGE-2**         | **0.4270** |
| **ROUGE-L**         | **0.6049** |
| **Summary Quality** | **55.53%** |

* **ROUGE-1** measures unigram overlap.
* **ROUGE-2** measures bigram overlap.
* **ROUGE-L** evaluates the longest common subsequence between generated and reference summaries.

#### 🎓 AI Tutor

**Semantic Similarity: 0.6626**
**AI Tutor Quality: 66.26%**

Evaluates how closely the AI Tutor's generated explanations align semantically with expected/reference responses. This provides a quantitative measure of the tutor's ability to produce contextually relevant explanations.

#### 📄 Document Processing

**Processing Success Rate: 100.00%**

Measures the successful extraction, cleaning, and processing of supported PDF and TXT documents through the document-processing pipeline.

#### 🔊 Audio Generation

**Generation Success Rate: 100.00%**

Measures the successful conversion of processed textual content into playable audio narration, supporting an additional accessibility pathway for users.

### 📈 Performance Summary

| Evaluation Area                 |      Result |
| :------------------------------ | ----------: |
| Braille Conversion Reliability  |  **94.50%** |
| Document Processing Reliability | **100.00%** |
| Audio Generation Reliability    | **100.00%** |
| Summary Evaluation              |  **55.53%** |
| AI Tutor Evaluation             |  **66.26%** |
| **Overall System Score**        |  **86.07%** |

> **Overall System Score: 86.07%**

The evaluation demonstrates strong reliability in the platform's core accessibility pipeline, particularly **document processing, audio generation, and Braille conversion**. The NLP-based **summarization and AI Tutor modules** are additionally evaluated using quantitative quality metrics, providing measurable evidence of their content and semantic performance.



## 🔮 Future Enhancements

- Multi-language Braille support
- OCR-based image-to-Braille conversion
- Personalized learning analytics
- Braille authentication system
- Voice-controlled navigation
- Graph-RAG powered knowledge exploration
- Cloud storage integration

---

## 📊 Key Highlights

- Accessibility-Focused AI Solution
- NLP-Based Educational Assistant
- Braille Conversion Engine
- AI Tutor Integration
- Audio Narration Support
- Downloadable Braille Documents
- Inclusive Learning Platform

---

## 👨‍💻 Author

**Balasubramaniam V**

B.Tech Computer Science Engineering

GitHub: https://github.com/balav100

LinkedIn: https://linkedin.com/in/Balasubramaniam V
