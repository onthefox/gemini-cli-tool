# 🚀 Gemini CLI Tool | AI-Powered Code Analysis & Generation

> **Advanced AI-powered CLI tool for intelligent code analysis, generation, and optimization using Google's Gemini AI API**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/onthefox/gemini-cli-tool?style=social)](https://github.com/onthefox/gemini-cli-tool)
![PyPI - Downloads](https://img.shields.io/badge/PyPI-gemini--cli--tool-blue)

## 📋 Table of Contents

- [About](#-about)
- [Features](#-key-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Advanced Features](#️-advanced-features)
- [Configuration](#️-configuration)
- [Examples](#-examples)
- [Origin & Attribution](#-origin--attribution)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

## 🎯 About

**Gemini CLI Tool** is a production-ready, enterprise-grade command-line utility that leverages Google's cutting-edge **Gemini AI models** to provide intelligent code analysis, generation, refactoring, and optimization capabilities.

Unlike traditional static analysis tools, this CLI uses **advanced AI reasoning** to:

✨ **Deep Code Understanding** - Understand code context, patterns, and intent  
🔬 **Intelligent Analysis** - Detect complex issues and suggest improvements  
⚡ **Code Generation** - Generate production-ready code from natural language descriptions  
🎯 **Smart Refactoring** - Suggest and apply modern best practices  
🛡️ **Security Auditing** - Find vulnerabilities, security risks, and anti-patterns  
📚 **Documentation** - Auto-generate comprehensive API docs and docstrings  
🧪 **Test Generation** - Create comprehensive test suites automatically  
🚀 **Performance Optimization** - Identify bottlenecks and suggest optimizations  

### Why Gemini CLI Tool?

| Feature | Traditional Tools | Gemini CLI Tool |
|---------|-------------------|------------------|
| **Analysis Type** | Static/Pattern-based | AI-powered reasoning |
| **Code Generation** | ❌ Limited | ✅ Full production code |
| **Context Understanding** | ❌ Basic | ✅ Advanced semantic analysis |
| **Refactoring** | ❌ Template-based | ✅ Intelligent suggestions |
| **Security Audit** | ⚠️ Signature-based | ✅ Behavioral analysis |
| **Test Generation** | ❌ None | ✅ Comprehensive coverage |
| **Ease of Use** | 📝 Complex config | 🎯 One command |

### Key Highlights

🔹 **Standalone CLI** - No IDE required, works in any terminal  
🔹 **Enterprise-Ready** - Comprehensive error handling and stability  
🔹 **Multi-Language Support** - Python, JavaScript, TypeScript, Java, Go, Rust  
🔹 **Cross-Platform** - Windows, macOS, Linux  
🔹 **Production-Grade** - Used in real-world projects and CI/CD pipelines  
🔹 **Secure** - API keys managed safely, never stored in plain text  
🔹 **Fast Installation** - `pip install gemini-cli-tool`  
🔹 **Active Development** - Regular updates with latest AI capabilities  

---

## ✨ Key Features

### Core Commands

| Command | Purpose | Use Case |
|---------|---------|----------|
| **analyze** | AI-powered code review | Find issues, bugs, anti-patterns |
| **generate** | Create code from description | Bootstrap, scaffolding, utilities |
| **refactor** | Intelligent code improvement | Modernize, optimize, clean up |
| **optimize** | Performance & memory tuning | Speed up, reduce memory footprint |
| **explain** | Auto-generate documentation | API docs, function explanations |
| **bugs** | Security & quality audit | Vulnerabilities, code smells |
| **test** | Auto-generate comprehensive tests | Unit, integration, edge cases |
| **config** | Manage settings & credentials | API keys, models, preferences |

### Advanced Capabilities

🔹 **Batch Processing** - Analyze multiple files simultaneously  
🔹 **Multiple Output Formats** - JSON, Markdown, Plain text, HTML  
🔹 **Streaming Responses** - Real-time output for long-running tasks  
🔹 **Intelligent Caching** - Reduce API calls with smart caching  
🔹 **CI/CD Integration** - GitHub Actions, GitLab CI, Jenkins ready  
🔹 **Docker Support** - Pre-built container for easy deployment  
🔹 **Authentication Flexibility** - API keys, OAuth, Vertex AI credentials  

---

## 📦 Installation

### System Requirements

- **Python** 3.8 or higher
- **pip** or **conda**
- **Google Gemini API Key** ([Get free API key here](https://ai.google.dev/))

### Option 1: Install from PyPI (Recommended)

```bash
pip install gemini-cli-tool
```

### Option 2: Install from Source

```bash
git clone https://github.com/onthefox/gemini-cli-tool.git
cd gemini-cli-tool
pip install -e .[dev]
```

### Option 3: Docker

```bash
docker build -t gemini-cli-tool .
docker run -e GEMINI_API_KEY=your_key gemini-cli-tool analyze file.py
```

---

## 🚀 Quick Start

### Step 1: Authenticate

**Option A: Browser OAuth (Recommended - No API key needed)**
```bash
gemini-cli
# Opens browser for authentication
```

**Option B: API Key**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Option C: Store in config**
```bash
gemini config set api_key "your-api-key-here"
```

### Step 2: Analyze Code

```bash
# Quick analysis
gemini analyze main.py

# Security-focused
gemini analyze app.py --focus security

# Performance audit
gemini analyze module.py --focus performance
```

### Step 3: Generate Code

```bash
gemini generate --description "async function to fetch data from API" \
  --language python \
  --requirements "use aiohttp" "add retry logic" "include logging"
```

### Step 4: View Results

```bash
gemini analyze code.py --output-format json --output results.json
cat results.json | jq '.issues[] | select(.severity=="critical")'
```

---

## 📖 Usage Guide

### Code Analysis

```bash
# Quality review
gemini analyze code.py --focus quality

# Security audit
gemini analyze api.py --focus security

# Performance analysis
gemini analyze algorithms.py --focus performance

# Save to file
gemini analyze code.py --output report.md

# JSON output for automation
gemini analyze code.py --output-format json --output analysis.json
```

### Code Generation

```bash
# Generate from description
gemini generate --description "Email validator using regex"

# With specific requirements
gemini generate \
  --description "Database connection pool" \
  --language python \
  --requirements "use asyncpg" "implement exponential backoff" "add logging"

# Save generated code
gemini generate --description "..." --output generated.py
```

### Refactoring

```bash
# General refactoring
gemini refactor old_code.py

# Specific style
gemini refactor code.py --style "PEP8"

# Save refactored version
gemini refactor code.py --output refactored.py
```

### Bug Detection

```bash
# Find all issues
gemini bugs application.py

# Security focus
gemini bugs api.py --focus security

# JSON for CI/CD
gemini bugs code.py --output bugs.json
```

### Test Generation

```bash
# Generate pytest tests
gemini test module.py

# Generate unittest
gemini test module.py --framework unittest

# JavaScript with Jest
gemini test app.js --language javascript --framework jest
```

---

## ⚙️ Configuration

### Configuration File

Location: `~/.gemini-cli/config.ini`

```ini
[gemini]
api_key = your-api-key-here
model = gemini-2.0-flash
temperature = 0.7
timeout = 30
```

### Environment Variables

```bash
# API Key (required)
export GEMINI_API_KEY="your-api-key"

# Model selection (optional)
export GEMINI_MODEL="gemini-2.0-pro"

# Temperature control (optional)
export GEMINI_TEMPERATURE="0.5"
```

### Available Models

- 🏆 `gemini-3.0-pro` - Most powerful, best reasoning (Nov 2025)
- 🧠 `gemini-2.5-pro` - Advanced reasoning, multimodal, coding
- ⚡ `gemini-2.5-flash` - Fast & efficient (default, recommended)

---

## 💡 Examples

### Example 1: Security Audit

```bash
gemini bugs api/handlers.py --focus security --output-format json
```

Finds:
- SQL injection risks
- XSS vulnerabilities
- Unsafe cryptography
- Authentication issues

### Example 2: Generate Production Code

```bash
gemini generate \
  --description "Async database pool with retry" \
  --language python \
  --requirements "asyncpg" "exponential backoff" "logging" "type hints"
```

### Example 3: Batch Analysis

```bash
for file in src/*.py; do
  gemini analyze "$file" >> analysis.md
done
```

### Example 4: CI/CD Integration

```bash
gemini analyze src/ --output-format json > code_analysis.json
if grep -q '"severity": "critical"' code_analysis.json; then
  echo "Critical issues found!"
  exit 1
fi
```

---

## 🔧 Advanced Features

### Streaming Output

```bash
gemini analyze code.py --stream
```

### Batch Processing

```bash
gemini analyze src/ --recursive
```

### JSON Export for Automation

```bash
gemini analyze code.py --output-format json | jq '.issues[] | select(.severity=="critical")'
```

### CI/CD Integration (GitHub Actions)

```yaml
name: Code Analysis
on: [push]
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: pip install gemini-cli-tool
      - env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: gemini analyze src/ --output-format json
```

---

## 🔗 Origin & Attribution

This project **improves upon** the excellent work in [**ast-grep/claude-skill**](https://github.com/ast-grep/claude-skill):

### Key Improvements

✅ **Standalone CLI** - Works in any terminal  
✅ **Gemini AI Integration** - Latest AI models with function calling  
✅ **Production Features** - Batch processing, multiple formats, CI/CD ready  
✅ **Enhanced Capabilities** - Test generation, performance optimization, security analysis  
✅ **Better UX** - Progress indicators, JSON output, error handling  
✅ **Full Documentation** - API reference, examples, troubleshooting  

---

## 🐛 Troubleshooting

### API Key Issues

```bash
# Verify API key
echo $GEMINI_API_KEY

# Update API key
gemini config set api_key "new-key"
```

### Connection Issues

```bash
# Test connectivity
gemini --version

# Enable verbose logging
gemini analyze code.py --verbose
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/onthefox/gemini-cli-tool.git
cd gemini-cli-tool
pip install -e ".[dev]"
pytest
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 📞 Support

- 📖 **Documentation**: [Full Docs](https://github.com/onthefox/gemini-cli-tool/wiki)
- 🐛 **Issues**: [GitHub Issues](https://github.com/onthefox/gemini-cli-tool/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/onthefox/gemini-cli-tool/discussions)
- 🤖 **Gemini API**: [Google AI Documentation](https://ai.google.dev/)

---

## 🌟 Show Your Support

- ⭐ Star the repository
- 🔗 Share with colleagues  
- 💬 Provide feedback
- 🐛 Report issues
- 🤝 Contribute improvements

**Made with ❤️ by the community**
