"""Install notation/subject indexing without replacing mathematical source files.
Run from any directory: python3 scripts/add_book_indices.py
Use --check for a dry run. Edits are idempotent and all anchors are checked
before any manuscript file is written.
"""
from pathlib import Path
import argparse
import json

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check',action='store_true',help='validate anchors and report edits without writing')
args=parser.parse_args()
plan=json.loads((root/'scripts/index_plan.json').read_text())
texts={}
def read(rel):
    if rel not in texts:
        texts[rel]=(root/rel).read_text()
    return texts[rel]
def replace_once(rel,needle,replacement):
    text=read(rel)
    if text.count(needle)!=1:
        raise RuntimeError(f'{rel}: expected exactly one anchor {needle!r}, found {text.count(needle)}')
    texts[rel]=text.replace(needle,replacement,1)
def insert_subjects(rel,label,terms):
    if not terms:
        return
    marker='% BEGIN SUBJECT INDEX: '+label
    text=read(rel)
    if marker in text:
        return
    anchor='\\label{'+label+'}'
    block='\n'+marker+'\n'+'\n'.join('\\index{'+term+'}' for term in terms)+'\n% END SUBJECT INDEX\n'
    replace_once(rel,anchor,anchor+block)
# First add definition anchors where the existing manuscript has no label.
for row in plan['anchors']:
    rel=row['path']; anchor='\\label{'+row['label']+'}'
    if anchor not in read(rel):
        replace_once(rel,row['needle'],row['needle']+'\n'+anchor)
    insert_subjects(rel,row['label'],row['terms'])
for row in plan['entries']:
    insert_subjects(row['path'],row['label'],row['terms'])
# Keep main.tex changes small, independent of the Chapters 7--8 notation patch.
main=read('main.tex')
notation='\\input{frontmatter/Notation_Index.tex}'
if notation not in main:
    replace_once('main.tex','\\tableofcontents','\\tableofcontents\n'+notation)
main=read('main.tex')
if '\\printindex' not in main:
    block=r"""% Subject index: svmono supplies the heading and table-of-contents entry.
\renewcommand{\indexname}{Subject Index}
\index{synchronization|see{coloring, synchronizing}}
\index{coloring!synchronizing|see{kernel, minimum rank}}
\index{kernel of a matrix|see{nullspace}}
\printindex
"""
    # Do not add an unhelpful nullspace cross-reference without an indexed treatment.
    block=block.replace('\\index{kernel of a matrix|see{nullspace}}\n','')
    replace_once('main.tex','\\end{document}',block+'\\end{document}')
changed=[rel for rel,text in texts.items() if text!=(root/rel).read_text()]
print(('Would update' if args.check else 'Updating'),len(changed),'source files:')
for rel in changed:
    print('  '+rel)
if not args.check:
    for rel in changed:
        (root/rel).write_text(texts[rel])
    print('Indexing installed. Re-run safely after another source patch if needed.')
