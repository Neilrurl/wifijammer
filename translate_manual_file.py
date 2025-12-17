#!/usr/bin/env python3
"""
Translation script for ManualTransFile.json
Translates Japanese text to Russian while keeping Japanese keys on the left.

This script requires manual translation input due to network restrictions.
Use web_search or external translation tools to translate batches, then
add the translations to the TRANSLATIONS dictionary below.

Usage:
    1. Run script to see next batch of untranslated entries
    2. Translate the batch using web_search or external tools
    3. Add translations to TRANSLATIONS dictionary
    4. Run script again to apply translations
    5. Repeat until all entries are translated
"""
import json
import re
import os

# Add your translations here in format: "Japanese text": "Russian translation"
# You can add translations in batches as you obtain them
TRANSLATIONS = {
    # Batch 1 (already translated via web_search)
    "山形遊具内": "Внутри ямагатских игровых конструкций",
    "パララ＿下地": "Парара_основа",
    "パララ＿ゴミ": "Парара_мусор",
    "パララ＿上": "Парара_верх",
    "パララ＿予備": "Парара_запасной",
    "移動時に自動実行＿ＴＥ": "Автоматический запуск при перемещении_ТЕ",
    "BGMを鳴らす": "Воспроизвести фоновую музыку",
    "自撮り用の背景を決定": "Выбрать фон для селфи",
    "現在のマップを指定": "Указать текущую карту",
    "歩数イベントの条件分岐で使用": "Используется в условиях события по шагам",
    "ゴミストッパー": "Стоппер для мусора",
    "出口": "Выход",
    "マップ移動開始から次のマップの自動実行が完了するまでタップ禁止": "Запрет на нажатие до завершения автоматического запуска на следующей карте после начала перехода",
    "モブの段階変数等をリセット": "Сброс промежуточных переменных моба и других параметров",
    "めくり箇所Lv1": "Место переворачивания Уровень 1",
    "29恥ずかし疑い＿瞳ジト＿眉困り＿口むにゅぅ": "29 Подозрение на стеснение_глаза в полуприкрытом_брови с беспокойством_рот «муню»",
    "非表示ページ": "Скрытая страница",
    "めくれない服の時/場所探し中": "Поиск места/одежды, которую нельзя перевернуть",
    "めくりレベルが３以上になったらイベント消去": "При достижении уровня переворачивания 3 и выше событие удаляется",
    "めくりLv2場所探しイベント": "Событие поиска места для переворачивания Уровень 2",
    
    # Add more translations here as you obtain them...
    # To add a batch, use format:
    # "Japanese": "Russian",
}

def contains_japanese(text):
    """Check if text contains Japanese characters."""
    japanese_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]')
    return bool(japanese_pattern.search(text))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, 'ManualTransFile.json')
    output_file = os.path.join(script_dir, 'ManualTransFile.json')
    
    print("="*70)
    print("Japanese to Russian Translation Script")
    print("="*70)
    
    # Load JSON file
    print("\nLoading JSON file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Total entries in file: {len(data)}")
    
    # Collect all entries with Japanese text
    japanese_entries = {}
    for key, value in data.items():
        if contains_japanese(value):
            japanese_entries[value] = key
    
    print(f"Entries with Japanese text: {len(japanese_entries)}")
    print(f"Translations available: {len(TRANSLATIONS)}")
    
    # Find untranslated entries
    untranslated = [jp for jp in japanese_entries.keys() if jp not in TRANSLATIONS]
    print(f"Remaining untranslated: {len(untranslated)}")
    
    # Apply translations
    translated_data = {}
    translations_applied = 0
    
    for key, value in data.items():
        if value in TRANSLATIONS:
            translated_data[key] = TRANSLATIONS[value]
            translations_applied += 1
        else:
            translated_data[key] = value
    
    print(f"\nTranslations applied in this run: {translations_applied}")
    
    # Save translated file
    print("\nSaving translated file...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=4)
    
    print(f"✓ File saved to: {output_file}")
    
    # Show some examples of translations
    if translations_applied > 0:
        print("\n" + "="*70)
        print("Sample translations applied:")
        print("="*70)
        count = 0
        for key, value in translated_data.items():
            if key in TRANSLATIONS:
                print(f"\nJapanese key: {key}")
                print(f"Russian value: {value}")
                count += 1
                if count >= 5:
                    break
    
    # Show next batch to translate
    if untranslated:
        print("\n" + "="*70)
        print(f"Next batch to translate (showing first 20 of {len(untranslated)}):")
        print("="*70)
        batch_size = 20
        next_batch = untranslated[:batch_size]
        
        print("\nCopy these entries for translation:")
        print("-"*70)
        for i, text in enumerate(next_batch, 1):
            # Truncate very long texts for display
            display_text = text if len(text) <= 100 else text[:97] + "..."
            print(f"{i}. {display_text}")
        
        print("\n" + "="*70)
        print("INSTRUCTIONS:")
        print("1. Copy the Japanese texts above")
        print("2. Use web_search or translation tool to translate to Russian")
        print("3. Add translations to TRANSLATIONS dictionary in this script")
        print("4. Run script again to apply translations")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("✓ ALL TRANSLATIONS COMPLETE!")
        print("="*70)

if __name__ == "__main__":
    main()
