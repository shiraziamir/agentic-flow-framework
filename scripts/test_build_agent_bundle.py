#!/usr/bin/env python3
from pathlib import Path
import tempfile, zipfile
from build_agent_bundle import build

def put(root, rel, text='x'):
    p=root/rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text)

def main():
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        for rel in ['VERSION','ARCHITECTURE.md','docs/agent/START_HERE.md','schemas/X.md','verification/X.md','production/X.md','skills/x/SKILL.md','prompts/bootstrap/X.md','templates/X.yaml','scripts/verification_lint.py']:
            put(root,rel)
        for rel in ['docs/operator/SECRET.md','research/R.md','agentic-flow-framework.fa.html']:
            put(root,rel)
        out=root/'bundle.zip'; m=build(root,out)
        names={x['path'] for x in m['files']}
        assert 'docs/agent/START_HERE.md' in names
        assert 'docs/operator/SECRET.md' not in names
        assert 'research/R.md' not in names
        with zipfile.ZipFile(out) as z:
            zn=set(z.namelist())
            assert 'agentic-flow/BUNDLE_MANIFEST.json' in zn
            assert 'agentic-flow/ARCHITECTURE.md' in zn
            assert not any('/docs/operator/' in x for x in zn)
        print('bundle builder self-test: PASS')

if __name__=='__main__': main()
