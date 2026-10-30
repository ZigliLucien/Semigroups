"""Static checks for the master-reachable notation list and subject entries.
No TeX engine is needed. These checks do not establish successful typesetting.
"""
from pathlib import Path
from collections import Counter
import json
import re
root=Path(__file__).resolve().parents[1]
seen=set(); missing=[]
def without_comments(t):
    return re.sub(r'(?m)(?<!\\)%.*$','',t)
def visit(rel):
    if rel in seen:
        return
    p=root/rel
    if not p.exists():
        missing.append(rel);return
    seen.add(rel)
    for target in re.findall(r'\\(?:input|include)\{([^}]+)\}',without_comments(p.read_text())):
        visit(target if target.endswith('.tex') else target+'.tex')
def arguments(text,command,nargs):
    pattern=re.compile(r'\\'+re.escape(command)+r'(?![A-Za-z])')
    result=[]
    for m in pattern.finditer(text):
        pos=m.end();args=[]
        for _ in range(nargs):
            while pos<len(text) and text[pos].isspace():pos+=1
            if pos==len(text) or text[pos]!='{':
                raise ValueError('Malformed '+command+' argument')
            start=pos+1;depth=1;pos+=1
            while pos<len(text) and depth:
                if text[pos]=='\\':
                    pos+=2;continue
                if text[pos]=='{':depth+=1
                elif text[pos]=='}':depth-=1
                pos+=1
            if depth:raise ValueError('Unbalanced '+command+' argument')
            args.append(text[start:pos-1])
        result.append(args)
    return result
visit('main.tex')
combined='\n'.join(without_comments((root/p).read_text()) for p in sorted(seen))
labels=re.findall(r'\\label\{([^}]+)\}',combined)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',combined)
# Ignore the local command definition when reading its invocations.
notation=without_comments((root/'frontmatter/Notation_Index.tex').read_text())
notation=notation[notation.index('\\section*'):]
rows=arguments(notation,'notationentry',3)
refs.extend(row[2] for row in rows)
indices=arguments(combined,'index',1)
counts=Counter(labels)
unresolved=sorted({ref for ref in refs if not ref.startswith('#')}-set(labels))
duplicates=sorted(k for k,v in counts.items() if v>1)
result={'master_reachable_tex_files':len(seen),'notation_entries':len(rows),
        'subject_entry_commands':len(indices),'missing_inputs':missing,
        'unresolved_reference_labels':unresolved,'duplicate_active_labels':duplicates,
        'notation_input_enabled':'\\input{frontmatter/Notation_Index.tex}' in combined,
        'subject_index_enabled':'\\printindex' in combined,
        'compilation_performed':False}
print(json.dumps(result,indent=2))
assert not missing and not unresolved and not duplicates,result
assert result['notation_input_enabled'] and result['subject_index_enabled']
