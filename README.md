# 🚀 Live App
[View Live App →](https://graph-visualization.streamlit.app/)
# 🎓 DEBESMSCAT FAQ Chatbot

# Streamlit App

This Streamlit web application provides an intelligent FAQ assistant for DEBESMSCAT (Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology) students, featuring automatic responses and comprehensive campus information.

# 📊 Overview
This application serves as a 24/7 digital assistant for DEBESMSCAT students, providing instant answers to frequently asked questions about academics, campus life, policies, and institutional information.

Key features:
- **Intelligent FAQ System** with automatic response generation
- **Sidebar Navigation** with categorized questions for easy browsing
- **Enhanced Matching Algorithm** for accurate question interpretation
- **Mobile-Responsive Design** optimized for all devices
- **Real-time Chat Interface** with conversation history
- **Comprehensive Database** covering all aspects of campus life

### Key Features Summary

Feature | Description | Status
:---|---|:---
FAQ Categories | 6 main categories with 40+ questions | ✅ Complete
Smart Matching | Handles multiple question variations | ✅ Enhanced
Mobile Support | Fully responsive design | ✅ Optimized
Auto-Response | Click sidebar items for instant answers | ✅ Working
Chat History | Persistent conversation tracking | ✅ Active

💡 The chatbot provides instant, accurate responses to student questions about DEBESMSCAT campus life, academics, and policies.

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Streamlit | Web application framework |
| Python | Core application logic |
| CSS | Custom styling and responsive design |
| Session State | Chat history and user interaction tracking |

# 📈 Features & Functionality

## 1. Intelligent FAQ System
- **Smart Matching Algorithm**: Recognizes multiple ways users phrase the same question
- **Variation Handling**: Maps "founding year", "when established", "colors", etc. to correct answers
- **Fallback System**: Provides helpful responses when exact matches aren't found

## 2. Sidebar Navigation
- **6 Main Categories**:
  - 🧠 Trivia & Culture
  - 📖 Handbook & Conduct  
  - 📍 Locations & Landmarks
  - 🏛️ Institutes & Colleges
  - 📚 Academics & Admissions
  - 🌿 Campus Life & Environment

## 3. Chat Interface
- **Real-time Responses**: Instant answers to user questions
- **Conversation History**: Tracks all Q&A interactions
- **Clear Function**: Reset conversation with one click
- **Professional Styling**: DEBESMSCAT-themed design elements

## 4. Mobile Responsiveness
- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Touch-Friendly**: Large tap targets for mobile interaction
- **Adaptive Layout**: Content scales appropriately for screen size

# 🎨 Design

The app features a professional DEBESMSCAT-themed interface with:
- **School Colors**: Navy blue and gold color scheme
- **Custom CSS**: Tailored styling for all components
- **Responsive Layout**: Adapts seamlessly to different screen sizes
- **Professional Typography**: Clean, readable fonts throughout

# 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── chatbot.py          # Chatbot response logic
├── utils.py            # FAQ matching algorithms
├── faq_data.py         # Comprehensive FAQ database
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation (this file)
```

# 📦 Installation

Prerequisites
- Python 3.8 or higher
- pip

Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/debesmscat-faq-chatbot.git
cd debesmscat-faq-chatbot
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# cmd
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run app.py
```

Open in browser: http://localhost:8501

# 📊 FAQ Database

The `faq_data.py` contains comprehensive information organized by categories:

## Categories Covered

### 🧠 Trivia & Culture
- Founding year and establishment details
- School colors and symbolism
- Namesake and historical context
- School motto, mission, and vision
- School hymn and rodeo team information

### 📖 Handbook & Conduct
- ID requirements and policies
- Uniform schedules and dress codes
- Expected behavior and conduct rules
- Smoking and alcohol policies
- Haircut and grooming guidelines

### 📍 Locations & Landmarks
- Campus locations (Mandaon, Cawayan, Masbate City)
- Key facilities (Library, Cafeteria, Gym, Clinic)
- Security office and emergency services

### 🏛️ Institutes & Colleges
- CCIT (College of Computing and Information Technology)
- Institute of Agriculture
- Institute of Education
- Engineering department

### 📚 Academics & Admissions
- Enrollment procedures and requirements
- Student portal access
- Registrar services and grades
- Clearance processes
- Scholarship opportunities
- OSAS and student organizations

### 🌿 Campus Life & Environment
- Campus atmosphere and environment
- Eco-friendly initiatives
- Nature and land features
- Emergency procedures

# 📚 Data Sources & References

The FAQ database is compiled from official DEBESMSCAT sources and institutional documentation:

## Institutional References

DEBESMSCAT Official Documentation
- Student Handbook and Conduct Guidelines
- Academic Policies and Procedures
- Campus Facilities and Services Information
- Institute and Department Descriptions

## Historical Information
- Republic Act 8548 (Establishment Legislation)
- Masbate School of Arts and Trades (MSAT) Historical Records
- Institutional Development Documentation

## Campus Services
- OSAS (Office of Student Affairs and Services) Guidelines
- Registrar Office Procedures
- Library and Facility Usage Policies

# 🚀 Deployment

To deploy on Streamlit Community Cloud:
1. Push your repository to GitHub
2. Go to https://share.streamlit.io and connect your repo
3. Set the main file to `app.py` and click Deploy

# 📝 Key Features Implementation

This project demonstrates advanced Streamlit capabilities:

- [x] Session state management for chat history
- [x] Custom CSS styling and responsive design
- [x] Intelligent text matching algorithms
- [x] Interactive sidebar navigation
- [x] Real-time chat interface
- [x] Mobile-optimized user experience
- [x] Professional institutional branding

# 🔧 Technical Implementation

## Smart Matching Algorithm
The `utils.py` file contains an advanced matching system that:
- Handles multiple question variations
- Provides fuzzy matching capabilities
- Maps user intent to correct FAQ entries
- Ensures accurate response delivery

## Session State Management
Persistent user interaction tracking:
- Chat history preservation
- Sidebar selection state
- User input prefill functionality
- Conversation continuity

## Responsive Design Implementation
Multi-device optimization:
- Desktop: Full-featured experience
- Tablet: Balanced layout adaptations
- Mobile: Streamlined interface with space efficiency

# 📄 License
This project is open source and available under the 
[MIT](https://github.com/YOUR_USERNAME/debesmscat-faq-chatbot/blob/main/LICENSE) License.

# Course: CS Elective 3
# Institution: Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology
# College: College of Computing and Information Technology (CCIT)

---

**🎓 DEBESMSCAT FAQ Chatbot** - Your 24/7 Digital Campus Assistant
