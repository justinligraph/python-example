
def foo(**kwargs):
  for key, value in kwargs.iteritems():
    print '\t', key, ':', value
  print '\tType of kwargs is:' , type(kwargs)

if __name__ == '__main__':
  print '**Use named parameter**'
  foo(first_name="Justin", last_name="Li")

  print
  print '**Use dict**'
  params = {'first_name': 'Justin', 'last_name': 'Li'}
  foo(**params)
