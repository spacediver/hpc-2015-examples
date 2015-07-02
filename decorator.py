def print_args(fn):
  def printing_args(*args):
    print ('args: ', args)
    return fn(*args)
  return printing_args
    
