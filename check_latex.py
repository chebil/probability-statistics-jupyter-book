#!/usr/bin/env python3
"""
Check for common LaTeX formatting issues in Markdown files.
"""

import re
import sys
from pathlib import Path

def check_file(filepath):
    """Check a single file for LaTeX issues."""
    issues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for inline math with brackets on same line as text
        # Pattern: text\[formula\]text or text\(formula\)text
        if re.search(r'\w\\\[|\\\]\w', line):
            issues.append((i, 'Display math \\[ \\] should be on separate lines', line.strip()))
        
        # Check for missing spaces around display math
        if re.search(r'[a-zA-Z]\\\[|\\\][a-zA-Z]', line):
            issues.append((i, 'Missing space around display math', line.strip()))
        
        # Check for incorrect bracket usage [ ] instead of \[ \]
        # This is tricky as [ ] is also used for links
        if re.search(r'^\s*\[\s*\\', line) and not re.search(r'\[.*\]\(.*\)', line):
            issues.append((i, 'Possible incorrect bracket - should be \\[ not [', line.strip()))
    
    return issues

def main():
    """Check all markdown files in part2 and part3."""
    base_path = Path('.')
    
    # Check part2 and part3
    for part in ['part2', 'part3']:
        part_path = base_path / part
        if not part_path.exists():
            print(f"Warning: {part} directory not found")
            continue
        
        print(f"\nChecking {part}/")
        print("=" * 70)
        
        md_files = sorted(part_path.glob('*.md'))
        
        for md_file in md_files:
            issues = check_file(md_file)
            
            if issues:
                print(f"\n{md_file.name}:")
                for line_num, issue, line_content in issues:
                    print(f"  Line {line_num}: {issue}")
                    print(f"    {line_content[:80]}..." if len(line_content) > 80 else f"    {line_content}")
    
    print("\n" + "=" * 70)
    print("Check complete!")
    print("\nNote: Jupyter Book LaTeX guidelines:")
    print("  - Use \\( \\) for inline math: \\(x^2\\)")
    print("  - Use \\[ \\] for display math (on separate lines):")
    print("    \\[")
    print("    x^2 + y^2 = z^2")
    print("    \\]")
    print("  - DO NOT use $ or $$ (even though they work in some renderers)")

if __name__ == '__main__':
    main()
