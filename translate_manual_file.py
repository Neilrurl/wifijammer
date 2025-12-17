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
    
    # Batch 2
    "めくりLv2習得イベント中の場所探し": "Поиск места для получения навыка переворота Lv2",
    "ここでイベントを開始": "Начать событие здесь",
    "縞ぱん好きの男(めくり2習得イベント用)": "Мужчина, любящий полосатые трусы (для события получения навыка переворота 2)",
    "クエストクリア判定_Lv2": "Проверка завершения квеста_Lv2",
    "呼び出しコピペ": "Вызов скопирован",
    "初期設定イベント": "Событие начальной настройки",
    "マップ切り替え時にマップ名を非表示": "Скрыть название карты при переключении карты",
    "ニューゲーム時には共有データのロード": "При новой игре загрузить общие данные",
    "★★★★★★注意★★★★★": "★★★★★★Внимание★★★★★",
    "※このプラグインコマンドが入っているので、共有データを混ぜてデプロイしないように注意": "※ В этот плагин добавлена эта команда, поэтому будьте внимательны и не смешивайте общие данные при деплое.",
    "最初に歩行グラが見切れるので黒屋根の下に隠していたのを見える位置に移動": "Сначала спрайт ходьбы был скрыт под черной крышей, теперь перемещен в видимое место",
    "通常立ち": "Обычная стойка",
    "06微笑み＿瞳通常＿眉通常＿口にこ": "06 Улыбка _ Глаза обычные _ Брови обычные _ Рот улыбка",
    "CG(破瓜時)の血液描画あり": "CG (при дефлорации) с отображением крови",
    "CG(破瓜時)の血液描画なし": "CG (при дефлорации) без отображения крови",
    "選択肢ヘルプ": "Помощь по выбору",
    "初めての挿入時に血液が描画されます。": "При первом проникновении будет отображаться кровь",
    "※オプションでいつでも変更可能。": "※ Можно изменить в любое время через опции.",
    "※この体験版に破瓜シーンは未実装です。": "※ В этой демо-версии сцена дефлорации не реализована.",
    "初めての挿入時の血液が非表示になります。": "При первом проникновении кровь не будет отображаться.",
    
    # Batch 3
    "OPをスキップしない": "Не пропускать вступление (OP)",
    "OP中のえっちシーンまでスキップする": "Пропустить до эротической сцены во вступлении",
    "行動可能なとこまでスキップする": "Пропустить до момента, когда возможны действия",
    "スキップせずにスタートします。": "Начать без пропуска",
    "少しえっちなシーンまでOPイベントをスキップします。": "Пропустить вступительные события до небольшой эротической сцены",
    "※簡単なあらすじ付き。": "※ С кратким изложением сюжета.",
    "OPイベントを全てスキップします。　※簡単なあらすじ付き。": "Пропустить все вступительные события. ※ С кратким изложением сюжета.",
    "途中のえっちシーンは回想へ登録されます。": "Промежуточные эротические сцены будут добавлены в воспоминания.",
    "本屋": "Книжный магазин",
    "パララ＿えっちな光": "Паралла — эротический свет",
    "カウンター扉": "Дверь у стойки",
    "MAP移動＿ＴＥ(公園へ)": "Перемещение по карте: ТЕ (в парк)",
    "移動先の設定": "Настройка места перемещения",
    "【Ｈイベント】本屋盗撮": "【H-событие】Вуайеризм в книжном магазине",
    "発生させるイベントを判定": "Проверить событие для активации",
    "普段着＋パンツ": "Повседневная одежда + трусы",
    "普段着＋ノーパン": "Повседневная одежда + без трусов",
    "１段階目の初回→０": "Первый этап, первый раз → 0",
    "１段階目の２回目以降→１２": "Первый этап, с второго раза и далее → 12",
    "段階１初回": "Первый раз на первом этапе",
    
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
