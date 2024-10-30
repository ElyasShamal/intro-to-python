

# display a starting messagem, explaining what the program does.
# Ask the user to press the Enter to see the step 1
# Display the instruction for step 1
# Ask the user to press the Enter to see the next step 
# Display the instruction for step 2
# Ask the user to press the Enter to see the next step 
# Display the instruction for step 3
# Ask the user to press the Enter to see the next step 
# Display the instruction for step 4

def main():
    startup_message()
    input('Press Enter to see Step 1.')
    step1()
    input('Press Enter to see Step 2.')
    step2()
    input('Press Enter to see Step 3.')
    step3()
    input('Press Enter to see Step 4:')
    step4()
    print()
    print()

def startup_message():
    print()
    print('This program tells you how to\n'
          'disassemble an ACME laundry dryer.\n'
          'There are 4 steps in the process.')
    print()


def step1():
    print()
    print('Step1: Unplug the dryer and \n'
          'Move it away from the wall.')
    print()


def step2():
    print()
    print('Step 2: Remove the six screws \n'
          'from the back of the dryer.')
    print()


def step3():
    print()
    print('Step 3: Remove the back panel.\n'
          'from the dryer.')
    print()


def step4():
    print()
    print('Step 4: Pull the top of the \n'
          'dryer straight up')



main()    



    