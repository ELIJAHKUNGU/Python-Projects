import  argparse

if __name__ == 'main':
   #initialize the parser
  parser = argparse.ArgumentParser(
      description="My math script"
  )
  #Add The Parameter / optional
  parser.add_argument('n', help='Number 1')
  parser.add_argument('-i', help = 'Number ')
  parser.add_argument('-o', help = 'Operational ')

  #parse Argument
  args= parser.parse_args()
  print(args)
  result = None
  if args.Operation == '+':
       result = args.num1 + args.num2
  if args.Operation == '-':
        result = args.num1 - args.num2
  if args.Operation == '*':
    result = args.num1 - args.num2
  if args.Operation == '-':
    result = args.num1 * args.num2
  if args.Operation == 'pow':
    result = pow(args.num1  ,args.num2)


    print('Results : ' , result)


