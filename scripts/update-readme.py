#!/usr/bin/env python3
"""Update README.md with content from config files."""

import re
from pathlib import Path

CONFIG_FILES = {
    'GITCONFIG_EXAMPLE': '.gitconfig.example',
    'GITCONFIG_GITHUB': '.gitconfig-github',
    'GITCONFIG_GITLAB': '.gitconfig-gitlab',
}

def update_readme():
    readme_path = Path('README.md')
    content = readme_path.read_text()
    
    for marker, config_file in CONFIG_FILES.items():
        config_content = Path(config_file).read_text()
        
        # Replace section between markers with config file content
        pattern = f'(<!-- {marker}_START -->)\n\n```ini\n.*?\n```\n\n(<!-- {marker}_END -->)'
        replacement = f'\\1\n\n```ini\n{config_content}```\n\n\\2'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    readme_path.write_text(content)

if __name__ == '__main__':
    update_readme()
