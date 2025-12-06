#!/usr/bin/env python3
"""
Fix ALL LaTeX formatting issues in Part 3 markdown files.
Converts [ formula ] to \\[ formula \\]
"""

import re
from pathlib import Path

def fix_latex_brackets(content):
    """Fix LaTeX bracket formatting in content."""
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Pattern: Line that starts with [ and contains LaTeX (backslash or math symbols)
        # and ends with ]
        # Examples:
        # [ p(x \mid \mu) = ... ]
        # [ \sum_{i=1}^{n} x_i ]
        
        # Match standalone equation lines with [ ]
        if re.match(r'^\s*\[\s*.+\\.*\s*\]\s*$', line):
            # Extract the formula
            match = re.match(r'^\s*\[\s*(.+)\s*\]\s*$', line)
            if match:
                formula = match.group(1).strip()
                # Replace with proper LaTeX display math
                fixed_lines.append('\\[')
                fixed_lines.append(formula)
                fixed_lines.append('\\]')
                i += 1
                continue
        
        fixed_lines.append(line)
        i += 1
    
    return '\n'.join(fixed_lines)

def process_file(filepath):
    """Process a single markdown file."""
    print(f"Processing {filepath.name}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    fixed = fix_latex_brackets(content)
    
    if fixed != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        
        # Count changes
        changes = sum(1 for a, b in zip(original.split('\n'), fixed.split('\n')) if a != b)
        print(f"  ✓ Fixed {changes} lines")
        return True
    else:
        print(f"  - No changes needed")
        return False

def main():
    """Fix all markdown files in part3."""
    part3_path = Path('part3')
    
    if not part3_path.exists():
        print("Error: part3/ directory not found")
        return
    
    print("="*70)
    print("Fixing LaTeX formatting in Part 3")
    print("="*70)
    print()
    
    md_files = sorted(part3_path.glob('*.md'))
    fixed_count = 0
    
    for md_file in md_files:
        if process_file(md_file):
            fixed_count += 1
    
    print()
    print("="*70)
    print(f"Summary: Fixed {fixed_count} out of {len(md_files)} files")
    print("="*70)

if __name__ == '__main__':
    main()
