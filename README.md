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

## 📊 Evaluation & Performance

The enhanced version of Open Your Eyes includes a quantitative evaluation framework to measure the reliability and quality of its core accessibility, NLP, and AI components.

Component	Evaluation Metric	Score
⠃ Braille Conversion	Braille Accuracy	94.50%
📄 Document Processing	Processing Success	100.00%
📝 AI Smart Summary	ROUGE-based Quality	55.53%
🎓 AI Tutor	Semantic Similarity	66.26%
🔊 Audio Generation	Generation Success	100.00%
🏆 Overall System	Aggregated System Score	86.07%
🔬 Detailed Evaluation
⠃ Braille Conversion
Braille Accuracy: 94.50%
Evaluates the correctness of generated Unicode Braille against the expected Braille representation.
📝 AI Smart Summary
ROUGE-1: 0.6339
ROUGE-2: 0.4270
ROUGE-L: 0.6049
Summary Quality: 55.53%
ROUGE metrics measure lexical overlap between generated summaries and reference summaries.
🎓 AI Tutor
Semantic Similarity: 0.6626
AI Tutor Quality: 66.26%
Measures the semantic alignment between AI-generated explanations and expected/reference responses.
📄 Document Processing
Processing Success: 100.00%
Measures successful extraction, cleaning, and processing of supported documents.
🔊 Audio Generation
Generation Success: 100.00%
Measures successful conversion of processed content into playable audio narration.
🏆 Overall Evaluation

Overall System Score: 86.07%

The evaluation demonstrates strong reliability across the platform's core document processing, Braille conversion, and audio generation components, while the AI-powered summarization and tutoring modules provide measurable content-quality and semantic-performance results.



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
