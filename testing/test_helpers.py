def printTestHeader(testHeader):
  print("\n\n")
  print("### " + testHeader)


def printPassingMessage(message):
  print(f"\033[92mPassed: {message}\033[0m")


def printFailingMessage(message):
  print(f"\033[91mFailed: {message} \033[0m")

