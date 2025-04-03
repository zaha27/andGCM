# gcm-enhance

A CLI tool that transforms boring Git commit messages into professional, conventional-style messages.

## Example

```bash
python gcm_enhance.py --message "fix login" --style conventional
# Output: fix: resolve login
```

## Installation

```bash
git clone https://github.com/yourname/gcm-enhance.git
cd gcm-enhance
python3 gcm_enhance.py --message "add user form"
```

## Arguments

- `--message`: Original commit message (required)
- `--style`: Message style: conventional | friendly | corporate
- `--dry-run`: Preview only
- `--auto-commit`: Automatically commit with enhanced message

## License

MIT