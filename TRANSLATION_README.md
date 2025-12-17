# Translation Guide for ManualTransFile.json

## Overview

This document explains the translation process for converting Japanese text to Russian in `ManualTransFile.json`.

### Translation Format

The JSON file follows this structure:
- **Left side (Key)**: Japanese text (unchanged)
- **Right side (Value)**: Russian translation

Example:
```json
{
    "山形遊具内": "Внутри ямагатских игровых конструкций",
    "BGMを鳴らす": "Воспроизвести фоновую музыку",
    "出口": "Выход"
}
```

## Current Status

- **Total entries in file**: 17,091
- **Entries with Japanese text**: 11,203
- **Currently translated**: 60 (as of last update)
- **Remaining**: 11,143

## Translation Tool

The `translate_manual_file.py` script manages the translation process:

### Features:
1. Loads the ManualTransFile.json
2. Applies translations from the TRANSLATIONS dictionary
3. Preserves JSON structure and formatting
4. Shows progress and next batch to translate
5. Maintains Japanese keys while translating values

### Usage:

```bash
python3 translate_manual_file.py
```

The script will:
- Apply any new translations added to the TRANSLATIONS dictionary
- Display the number of translations applied
- Show the next 20 entries that need translation
- Save the updated file

## Adding New Translations

To add translations to the script:

1. Open `translate_manual_file.py`
2. Find the `TRANSLATIONS` dictionary
3. Add new entries in the format: `"Japanese text": "Russian translation",`
4. Run the script to apply the translations

### Example:

```python
TRANSLATIONS = {
    # Existing translations...
    
    # New batch
    "新しいテキスト": "Новый текст",
    "別のテキスト": "Другой текст",
}
```

## Translation Process

### Method 1: Web Search (Recommended)

Use web_search to translate batches of 20 items:

```
Query: "Translate these 20 Japanese game UI texts to Russian, numbered list only:
1. [Japanese text 1]
2. [Japanese text 2]
...
20. [Japanese text 20]"
```

### Method 2: External Translation Tools

- Google Translate
- DeepL
- Professional translation services

### Method 3: Offline Translation

If network access becomes available:
- Install argostranslate with Japanese→English and English→Russian models
- Run automated batch translation

## Batch Progress Tracking

The translation is organized in batches of 20 entries each:

| Batch | Status | Entries |
|-------|--------|---------|
| 1     | ✅ Complete | 20 |
| 2     | ✅ Complete | 20 |
| 3     | ✅ Complete | 20 |
| 4-561 | ⏳ Pending | 11,143 |

**Total batches needed**: ~560

## Quality Guidelines

When translating:

1. **Context matters**: Consider the game UI context
2. **Consistency**: Use consistent terminology for repeated concepts
3. **Length**: Keep translations reasonably similar in length to originals
4. **Special characters**: Preserve special characters like ＿, ★, ※, 【】
5. **Numbers and codes**: Keep alphanumeric codes and technical identifiers

## Examples of Good Translations

| Japanese | Russian | Notes |
|----------|---------|-------|
| BGMを鳴らす | Воспроизвести фоновую музыку | Clear and concise |
| 出口 | Выход | Simple, direct |
| 非表示ページ | Скрытая страница | Accurate meaning |
| マップ移動 | Перемещение по карте | Game-appropriate terminology |

## Technical Notes

- File encoding: UTF-8
- JSON format: Indented with 4 spaces
- ensure_ascii: False (preserves Cyrillic and Japanese characters)
- Line endings: Unix style (LF)

## Automation Considerations

For completing the remaining 11,000+ translations:

1. **Batch processing**: Process 20-50 translations at a time
2. **API integration**: If translation API access becomes available
3. **Incremental commits**: Commit after every 100-200 translations
4. **Validation**: Regular JSON validation to prevent syntax errors

## Contributing

When adding translations:
1. Test the script after adding new batches
2. Verify JSON validity
3. Check for duplicate entries
4. Ensure Russian translations are appropriate for game context
5. Commit with clear messages indicating which batches were added

## Verification

To verify translations:

```python
import json

with open('ManualTransFile.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
# Check specific translations
print(data['山形遊具内'])  # Should print Russian translation
```

## Notes

- This is a large-scale translation project requiring ~560 batch operations
- The infrastructure is in place for incremental completion
- Each batch takes approximately 2-3 minutes to translate and apply
- Estimated total time for completion: 20-30 hours of active translation work
