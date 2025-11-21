# Publishing Guide for gemini-cli-tool

This document provides comprehensive instructions for publishing the gemini-cli-tool package to PyPI (Python Package Index) using GitHub Actions and trusted publishers.

## 📋 Overview

The project is configured with a modern, secure CI/CD pipeline using:
- **GitHub Actions**: Automated workflow triggers on release
- **Trusted Publishers (OIDC)**: No need for API keys or passwords
- **PyPI Integration**: Seamless package distribution

## ✅ Current Setup Status

### PyPI Account Configuration
- ✅ Account created and verified with 2FA enabled
- ✅ Recovery codes generated and securely stored
- ✅ API tokens configured (backup method)
- ✅ Trusted publisher registered for GitHub Actions

### GitHub Repository Configuration
- ✅ Publish workflow configured (`.github/workflows/publish.yml`)
- ✅ PyPI environment created with proper protection rules
- ✅ Trusted Publisher linked to onthefox/gemini-cli-tool
- ✅ OpenID Connect (OIDC) trust relationship established

## 🚀 Publishing a Release

To publish a new version to PyPI:

### Step 1: Create a Release on GitHub
1. Go to the repository's Releases page
2. Click "Create a new release"
3. Enter version tag (e.g., `v1.2.0`)
4. Add release title and description
5. Click "Publish release"

### Step 2: Workflow Automatically Executes
The `Publish to PyPI` workflow will automatically:
1. Trigger on release event
2. Check out the code
3. Setup Python 3.11
4. Install build dependencies (`pip install build`)
5. Build distribution packages (`python -m build`)
6. Authenticate using trusted publisher (OIDC)
7. Upload to PyPI using `pypa/gh-action-pypi-publish`

### Step 3: Monitor the Workflow
1. Go to Actions tab
2. Select "Publish to PyPI" workflow
3. View the latest run
4. Check logs for any issues

## 🔐 Security Features

### Trusted Publishers (OIDC)
- No long-lived credentials stored
- No API tokens needed in environment
- GitHub cryptographically signs each publish request
- PyPI verifies the signature and GitHub metadata
- Automatic token generation per workflow run

### Workflow Configuration
```yaml
environment:
  name: pypi
  url: https://pypi.org/p/gemini-cli-tool

permissions:
  id-token: write  # Required for OIDC
```

### PyPI Environment Protection
- Environment name: `pypi`
- Deployment protection: Enabled
- Custom rules: Allow administrators to bypass
- No branch restrictions: Works from any branch during releases

## 📦 Package Information

- **Project Name**: gemini-cli-tool
- **PyPI URL**: https://pypi.org/project/gemini-cli-tool/
- **Repository**: https://github.com/onthefox/gemini-cli-tool
- **License**: MIT
- **Python**: 3.8+

## 🔍 Verification

After publishing, verify the package:

```bash
# Install the published package
pip install gemini-cli-tool

# Verify installation
python -c "import gemini_cli_tool; print(gemini_cli_tool.__version__)"

# Check PyPI listing
curl https://pypi.org/pypi/gemini-cli-tool/json
```

## 🛠️ Troubleshooting

### Workflow Fails
1. Check the workflow logs in Actions tab
2. Common issues:
   - Trusted publisher not linked correctly → Re-verify PyPI account settings
   - Build errors → Check `pyproject.toml` configuration
   - Version already exists → Use a new version number

### Package Not Found on PyPI
1. Wait a few minutes for PyPI to index
2. Check PyPI project page for the version
3. Try `pip search gemini-cli-tool` (may take time to appear)

### Authentication Issues
1. Verify OIDC trust relationship in PyPI account settings
2. Ensure environment name in workflow matches PyPI configuration (should be `pypi`)
3. Check GitHub Actions has `id-token: write` permission

## 📖 Build and Version Management

### Version Format
Follow semantic versioning: `MAJOR.MINOR.PATCH`
- Example: `v1.0.0`, `v1.2.3`

### Building Locally
```bash
# Install build tools
pip install build

# Build distribution
python -m build

# Check contents
ls dist/
```

## 🎯 Workflow File Reference

Location: `.github/workflows/publish.yml`

Key sections:
- **Trigger**: `on: release: types: [published]`
- **Environment**: PyPI environment with OIDC
- **Build**: Python 3.11 with build module
- **Publish**: Uses `pypa/gh-action-pypi-publish@release/v1`

## 🔗 Related Documentation

- [PyPI Help - API Tokens](https://pypi.org/help/#apitoken)
- [GitHub - Using OIDC with PyPI](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [Python Packaging Guide](https://packaging.python.org/)
- [Trusted Publishers on PyPI](https://docs.pypi.org/trusted-publishers/)

## 📝 Release Checklist

Before publishing a new release:
- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md` with changes
- [ ] Run tests locally: `python -m pytest`
- [ ] Build locally: `python -m build`
- [ ] Commit changes with meaningful message
- [ ] Create git tag: `git tag v<version>`
- [ ] Push changes and tags: `git push origin main --tags`
- [ ] Create release on GitHub UI
- [ ] Monitor workflow execution in Actions
- [ ] Verify package on PyPI

## 👤 Author Notes

- PyPI Account: `catt` (onthefox)
- Trusted Publisher: Active and linked
- 2FA: Enabled with recovery codes secured
- Last verified: November 21, 2025

---

**For questions or issues, refer to the main README.md or open an issue on GitHub.**
