#!/usr/bin/env python3
"""
Fix LaTeX formatting in markdown files.
Converts [ formula ] to \[ formula \] (display math)
and fixes other common LaTeX issues.
"""

import re
import sys
from pathlib import Path

def fix_latex_in_file(filepath):
    """Fix LaTeX formatting in a single file."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Pattern 1: Fix display math brackets
    # Match lines that start with [ and contain math (LaTeX commands like \, \theta, etc.)
    # and end with ]
    pattern1 = r'^\s*\[\s*(.+?)\s*\]\s*$'
    
    lines = content.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines, 1):
        original_line = line
        
        # Check if this looks like a LaTeX equation (contains backslash commands)
        # and is wrapped in [ ] instead of \[ \]
        if re.match(pattern1, line) and ('\\' in line or '\sum' in line or '\prod' in line):
            # Skip if it's a markdown link reference [text]: url
            if not re.match(r'^\s*\[.+?\]\s*:\s*', line):
                # This is likely display math with wrong brackets
                match = re.match(pattern1, line)
                if match:
                    formula = match.group(1)
                    # Don't convert if it looks like a markdown reference or citation
                    if not re.match(r'^\d+$', formula) and not re.match(r'^[a-z]+:\d+', formula):
                        new_line = f'\\[\n{formula}\n\\]'
                        if original_line != new_line:
                            changes.append((i, 'Display math brackets', original_line[:60]))
                            line = new_line
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Pattern 2: Fix inline math that might be broken
    # Nothing to do here - inline math should use \( \) which is already correct
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    """Fix LaTeX formatting in all markdown files."""
    
    base_path = Path('.')
    total_fixes = 0
    fixed_files = []
    
    # Check part2 and part3
    for part in ['part2', 'part3']:
        part_path = base_path / part
        if not part_path.exists():
            print(f"Warning: {part} directory not found")
            continue
        
        print(f"\nProcessing {part}/")
        print("=" * 70)
        
        md_files = sorted(part_path.glob('*.md'))
        
        for md_file in md_files:
            modified, changes = fix_latex_in_file(md_file)
            
            if modified:
                fixed_files.append(md_file.name)
                total_fixes += len(changes)
                print(f"\n✓ Fixed {md_file.name}:")
                for line_num, issue, preview in changes:
                    print(f"  Line {line_num}: {issue}")
                    print(f"    {preview}...")
    
    print("\n" + "=" * 70)
    print(f"\nSummary:")
    print(f"  Files modified: {len(fixed_files)}")
    print(f"  Total changes: {total_fixes}")
    
    if fixed_files:
        print(f"\nModified files:")
        for f in fixed_files:
            print(f"  - {f}")
    else:
        print("\nNo LaTeX formatting issues found!")
    
    print("\nDone!")

if __name__ == '__main__':
    main()
