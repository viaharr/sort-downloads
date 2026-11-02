```markdown
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# Sort Downloads

Скрипт, который автоматически раскладывает файлы из папки `Downloads` по подпапкам в зависимости от расширения.

## Что делает

- Создаёт папку `Downloads/Sorted/`, если её нет.
- Раскладывает файлы по категориям: `Documents`, `Images`, `Archives`, `Installers`, `Torrents`.
- Не трогает папки и файлы с неизвестными расширениями.
- Если файл с таким именем уже есть — добавляет `_1` к имени, не затирает.

## Требования

- Python 3.10+
- Только стандартная библиотека (`shutil`, `pathlib`) — ничего ставить не надо.

## Установка

```bash
git clone https://github.com/ТВОЙ_НИК/sort-downloads.git
cd sort-downloads
```

## Использование

### Разовый запуск

```bash
python sort_downloads.py
```

Скрипт разложит файлы в `Downloads/Sorted/`.

### Автозапуск

#### Windows — Планировщик заданий

1. `Win + R` → `taskschd.msc` → `Enter`.
2. Справа — «Создать задачу» (не «простую»).
3. Вкладка «Общие»:
   - Имя: `Sort Downloads`
   - Галочка **«Скрытая»** (чтобы окно не мигало).
4. Вкладка «Триггеры» → «Создать»:
   - «Повторять задачу каждые» → 15 минут
   - «В течение» → неограниченного срока
5. Вкладка «Действия» → «Создать»:
   - Программа: `pythonw.exe` (полный путь, см. ниже)
   - Аргументы: `C:\путь\до\sort_downloads.py`
   - Рабочая папка: `C:\путь\до\`
6. **ОК**, ввести пароль Windows.

Где взять путь к `pythonw.exe`:

```cmd
where python
```

Выдаст что-то вроде `C:\Users\Ты\AppData\Local\Programs\Python\Python312\python.exe`. Замени в конце `python.exe` на `pythonw.exe` — это то же самое, но без окна консоли.

#### macOS / Linux — cron

```bash
crontab -e
```

Добавь строку:

```
*/15 * * * * /usr/bin/python3 /полный/путь/до/sort_downloads.py
```

Сохрани (`:wq` в vim). Скрипт будет запускаться каждые 15 минут без окон.

## Настройка

Правила раскладки — в словаре `RULES` в `sort_downloads.py`.

Пример добавления нового расширения:

```python
".mp4": "Video",
```