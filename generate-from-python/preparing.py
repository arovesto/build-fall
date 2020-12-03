import sys

if __name__ == '__main__':
  with open(sys.argv[1], 'w') as fp:
    fp.write('int arr[] = {1,2,3};')
  sys.stdout.write(' '.join(sys.argv))
