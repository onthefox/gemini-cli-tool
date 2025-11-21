# 🚀 Gemini CLI Tool

> Advanced AI-powered CLI tool for intelligent code analysis, generation, and optimization using Google's Gemini API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/onthefox/gemini-cli-tool?style=social)](https://github.com/onthefox/gemini-cli-tool)

---

## 📋 Table of Contents

- [About](#about)
- [Origin & Attribution](#origin--attribution)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Advanced Features](#advanced-features)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 About

**Gemini CLI Tool** is a production-ready, standalone command-line utility that leverages Google's Gemini AI models to provide intelligent code analysis, generation, refactoring, and optimization capabilities. Unlike traditional code analysis tools, this CLI tool uses advanced AI reasoning to understand context, suggest improvements, and generate production-quality code.

### Key Highlights

✨ **AI-Powered Analysis** - Deep code understanding using Gemini's advanced reasoning  
⚡ **Production Ready** - Enterprise-grade error handling and stability  
🔧 **Versatile** - Code generation, analysis, optimization, refactoring, testing, documentation  
🌐 **Cross-Platform** - Works on Windows, macOS, Linux  
📦 **Easy Installation** - Install via pip and use immediately  
🔐 **Secure** - API keys handled safely with environment variables  

---

## 🔗 Origin & Attribution

> This project was **inspired by and significantly improves upon** the excellent work in [**ast-grep/claude-skill**](https://github.com/ast-grep/claude-skill)

### What's Different

| Aspect | Original | This Project |
|--------|----------|---------------|
| **Environment** | Claude Code IDE | Standalone CLI |
| **Core Tech** | AST-based text search | Gemini AI reasoning |
| **Focus** | Structural code search | AI-driven code analysis & generation |
| **Distribution** | IDE skill | PyPI package + Docker |
| **Use Cases** | Pattern finding | Code generation, refactoring, optimization |

### Key Improvements

✅ **Standalone CLI Tool** - Works in any terminal, no IDE required  
✅ **Gemini AI Integration** - Direct Gemini API with Function Calling  
✅ **Production Features** - Configuration management, batch processing, multiple output formats  
✅ **Enhanced Capabilities** - Test generation, performance optimization, security analysis  
✅ **Better UX** - Professional error messages, progress indicators, JSON output  
✅ **Full Documentation** - Examples, API reference, troubleshooting guide  

---

## ✨ Features

### Core Commands

| Command | Description | Example |
|---------|-------------|----------|
| **analyze** | Review code for quality/security/performance issues | `gemini analyze app.py --focus security` |
| **generate** | Create code from natural language description | `gemini generate --description "async iterator"` |
| **refactor** | Suggest intelligent refactoring improvements | `gemini refactor legacy.py --style modern` |
| **optimize** | Improve code for performance or memory | `gemini optimize algorithm.py --target performance` |
| **explain** | Generate detailed code documentation | `gemini explain complex.py --detail detailed` |
| **bugs** | Find potential bugs and security issues | `gemini bugs module.py` |
| **test** | Automatically generate comprehensive tests | `gemini test service.py --framework pytest` |
| **config** | Manage API keys and settings | `gemini config set api_key YOUR_KEY` |

### Advanced Capabilities

🔹 **Batch Processing** - Analyze multiple files at once  
🔹 **Custom Output Formats** - JSON, Markdown, Plain Text  
🔹 **Streaming Responses** - Real-time output for long-running tasks  
🔹 **Caching** - Intelligent result caching to reduce API calls  
🔹 **CI/CD Integration** - Export results for pipeline integration  
🔹 **Docker Support** - Containerized deployment  

---

## 📦 Installation

### System Requirements

- **Python** 3.8 or higher
- **pip** or **conda**
- **Google Gemini API Key** ([Get one here](https://ai.google.dev))

### Option 1: Install from PyPI (Recommended)

```bash
pip install gemini-cli-tool
```

### Option 2: Install from Source

```bash
git clone https://github.com/onthefox/gemini-cli-tool.git
cd gemini-cli-tool
pip install -e .
```

### Option 3: Docker

```bash
docker build -t gemini-cli-tool .
docker run -e GEMINI_API_KEY=your_key gemini-cli-tool analyze file.py
```

---

## 🚀 Quick Start

### 1. Set Your API Key

```bash
# Option A: Environment variable
export GEMINI_API_KEY="your-api-key-here"

# Option B: Store in config
gemini config set api_key "your-api-key-here"
```

### 2. Analyze Code

```bash
gemini analyze main.py --focus quality
```

### 3. Generate Code

```bash
gemini generate --description "A function that validates email addresses" \
  --requirements "Use regex" "Raise ValueError on invalid input" "Include type hints"
```

### 4. View Results

```bash
gemini analyze app.py --output results.json --focus security
cat results.json
```

---

## 📖 Usage Guide

### Analyzing Code

```bash
# Quality analysis (default)
gemini analyze code.py

# Security-focused analysis
gemini analyze code.py --focus security

# Performance analysis
gemini analyze code.py --focus performance

# Save to file
gemini analyze code.py --output analysis.md
```

### Generating Code

```bash
# Generate with description
gemini generate --description "Sort algorithm implementation" \
  --language python

# With specific requirements
gemini generate --description "API client" \
  --requirements "Use async/await" "Implement retry logic" "Add logging"

# Save output
gemini generate --description "..." --output generated.py
```

### Refactoring

```bash
# General refactoring
gemini refactor old_code.py

# Follow specific style guide
gemini refactor code.py --style "PEP8"

# Output to new file
gemini refactor code.py --output refactored.py
```

### Optimization

```bash
# Performance optimization
gemini optimize slow.py --target performance

# Memory optimization
gemini optimize large_data.py --target memory

# Output with explanations
gemini optimize code.py --output optimized.py
```

### Finding Bugs

```bash
# Find all issues
gemini bugs application.py

# Detailed security report
gemini bugs api.py --focus security

# JSON output for CI/CD
gemini bugs code.py --output bugs.json
```

### Generating Tests

```bash
# Generate pytest tests (default)
gemini test module.py

# Generate unittest
gemini test module.py --framework unittest

# Generate Jest for JavaScript
gemini test app.js --language javascript --framework jest
```

---

## ⚙️ Configuration

### Configuration File

Configuration is stored at `~/.gemini-cli/config.ini`:

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

- `gemini-3.0-pro` 🏆 (Most powerful, best reasoning - Nov 2025 release)
- `gemini-2.5-pro` 🧠 (Advanced reasoning, multimodal, coding)
- `gemini-2.5-flash` ⚡ (Fast & efficient, ideal for everyday tasks - default)


## 💡 Examples

### Example 1: Code Quality Review

```bash
# Analyze a Python module
gemini analyze myapp/utils.py --focus quality

# Output includes:
# - Code smells detected
# - Complexity issues
# - Best practice violations
# - Refactoring suggestions
```

### Example 2: Generate Production Code

```bash
gemini generate \
  --description "Async database connection pool with retry logic" \
  --language python \
  --requirements \
    "Use asyncpg for PostgreSQL" \
    "Implement exponential backoff" \
    "Add comprehensive logging" \
    "Include type hints" \
    "Write docstrings"
```

### Example 3: Security Audit

```bash
# Find security vulnerabilities
gemini bugs api/handlers.py --focus security

# Output identifies:
# - SQL injection risks
# - XSS vulnerabilities
# - Unsafe cryptography
# - Authentication issues
```

### Example 4: Batch Analysis

```bash
# Analyze multiple files
for file in src/*.py; do
  gemini analyze "$file" >> results.md
done
```

---

## 🔧 Advanced Features

### Streaming Output

```bash
gemini analyze code.py --stream
```

### JSON Output for Automation

```bash
gemini analyze code.py --output-format json --output results.json
cat results.json | jq '.issues[] | select(.severity=="critical")'
```

### CI/CD Integration

```yaml
# GitHub Actions Example
name: Code Analysis
on: [push]
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Gemini CLI
        run: pip install gemini-cli-tool
      - name: Analyze Code
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: gemini analyze src/ --output-format json
```

---

## 🐛 Troubleshooting

### API Key Issues

```bash
# Verify API key is set
echo $GEMINI_API_KEY

# Check config file
cat ~/.gemini-cli/config.ini

# Update API key
gemini config set api_key "new-key-here"
```

### Connection Issues

```bash
# Test connectivity
gemini --version

# Enable verbose logging
gemini analyze code.py --verbose

# Check API status
curl https://ai.google.dev/
```

### Out of Memory

```bash
# Analyze smaller files
gemini analyze small_file.py

# Use streaming mode
gemini analyze large_file.py --stream
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
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

### Attribution

This project builds upon the excellent foundation of [ast-grep/claude-skill](https://github.com/ast-grep/claude-skill) (also MIT licensed).

---

## 📞 Support

- **Documentation**: [Full Docs](https://github.com/onthefox/gemini-cli-tool/wiki)
- **Issues**: [GitHub Issues](https://github.com/onthefox/gemini-cli-tool/issues)
- **Discussions**: [GitHub Discussions](https://github.com/onthefox/gemini-cli-tool/discussions)
- **Gemini API Help**: [Google AI Documentation](https://ai.google.dev/)

---

## 🌟 Show Your Support

If you find this tool useful, please consider:

- ⭐ Starring the repository
- 🔗 Sharing with colleagues
- 💬 Providing feedback
- 🐛 Reporting issues
- 🤝 Contributing improvements

---

**Made with ❤️ by the community**
