# Dry-run one new recipe file: runs build_recipes.py with FILE exec'd after the batches, writes nothing to site/data.
# Usage: python3 try_recipe.py recipes_v5_xxx.py  -> prints the new recipes' ids and node counts, raises on lookup errors.
import sys, json
f = sys.argv[1]
src = open('/home/claude/poe2data/scripts/build_recipes.py').read()
src = src.replace("exec(open('/home/claude/poe2data/scripts/recipes_batch4.py').read())",
                  "exec(open('/home/claude/poe2data/scripts/recipes_batch4.py').read())\n__n0=len(R)\nexec(open(%r).read())" % f)
src = src.replace("json.dump({'v':2,'recipes':R},open(D+'recipes.json','w'),ensure_ascii=False)", "")
ns = {}
exec(compile(src, 'build_recipes.py', 'exec'), ns)
new = ns['R'][ns['__n0']:]
for r in new: print(r['id'], r['cls'], len(r['nodes']), 'nodes')
json.dump(new, open('/tmp/try_'+f.replace('/','_')+'.json','w'), ensure_ascii=False)
