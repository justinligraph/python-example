
def foo(**kwargs):
  for key, value in kwargs.iteritems():
    print key, ':', value
  print type(kwargs)

if __name__ == '__main__':
  foo(first_name="Justin", last_name="Li")
