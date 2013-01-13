return silent(join)(keep(f.data for f in fields))
select_values(bool, {...}

# f.error = some(chain(
#     [f.required if f.required and not raw[f.name] else None],
#     (r['text'] or 'internal' for r in f.rules if r['type'] == 'raw' and not r['test'](raw)),
#     [f.required if f.required and not getattr(self, f.name) else None],
#     (r['text'] or 'internal' for r in f.rules if r['type'] == 'rule' and not r['test'](self)),
# ))

value.value = walk_values(prepare, value.value)

json_field = partial(field, json=True)

key_matches = lambda key: key == '*' or category in key.split(',')
selected = select_keys(key_matches, _categorized.value)
# or re_tester()

return map(second, sorted(selected.items()))

places = re_iter(r'\b(\w+)(?:\.(\w+))?(?:\.(\d+))?\b', show) if show else []
places = ((place, {'section': section, 'pos': int(pos) if pos else 1000000})
          for place, section, pos in places)
return defaultdict(lambda: defaultdict(str), places)

re = lambda pattern: lambda value: re_test(pattern, value)

ops = node.ops
operands = [node.left] + node.comparators
pairs = partition(2, 1, operands)
node.js = ' && '.join('(%s %s %s)' % (l.js, op.js, r.js)  for op, (l, r) in zip(ops, pairs))

def translate_dict(d):
    lines = ('%s: %s' % (k, v) for k, v in walk_values(translate, d).items())
    return '{%s}' % ','.join(lines)

names = func.__code__.co_freevars
values = [cell.cell_contents for cell in func.__closure__]
return zipdict(names, values)

names = _code_names(code)
return merge(project(__builtins__, names), project(func.__globals__, names))

def closure(func):
    return merge(_globals(func), _locals(func))


class namespace_meta(type):
    def __new__(cls, name, bases, attrs):
        attrs = walk_values(iffy(callable, staticmethod), attrs)
        return super(namespace_meta, cls).__new__(cls, name, bases, attrs)

class namespace(object):
    __metaclass__ = namespace_meta


names = chain.from_iterable(get_all_names(color))
try:
    return ifilter(None, imap(COLOR_BY_NAME.get, names)).next()
except StopIteration:
    return unknown()

etags = map(etag_from_response, responses)
etags = filter(None, etags)

phones = filter(None, map(stub_to_phone, _extract_stubs(text)))