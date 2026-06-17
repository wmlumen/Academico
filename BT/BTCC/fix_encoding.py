import re

with open('C:/Users/HP 250 G10/Documents/GITHUT/MEC/BT/BTCC/2_Curso/Resistencia_Materiales/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'â€”': '—',
    'Â·': '·',
    'Ã±': 'ñ',
    'AÃ±o': 'Año',
    'Ã³': 'ó',
    'Ã©': 'é',
    'Ã¡': 'á',
    'Ã­': 'í',
    'Ãº': 'ú',
    'Ã‘': 'Ñ',
    'â–¼': '▼',
    'â–²': '▲',
    'ðŸ“‹': '📋',
    'ðŸ“š': '📚',
    'ðŸ“': '📝',
    'ðŸ“Š': '📊',
    'ðŸ“–': '📖',
    'ðŸŽ¨': '🎨',
    'ðŸ”§': '🛠',
    'ðŸ“„': '📄',
    'ðŸ“¦': '📦',
    'ðŸ‘¨â€ðŸ«': '👨‍🏫',
    'ðŸ‘¨â€ðŸŽ“': '👨‍🎓',
    'ðŸ‘': '👍',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('C:/Users/HP 250 G10/Documents/GITHUT/MEC/BT/BTCC/2_Curso/Resistencia_Materiales/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')