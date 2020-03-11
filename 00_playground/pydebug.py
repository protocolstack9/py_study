import inspect

def PrintFrame(sel):
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  if sel == "file":
    print(info.filename)                      # __FILE__     -> Test.py
  elif sel == "func":
    print(info.function)                      # __FUNCTION__ -> Main
  elif sel == "line":
    print(info.lineno)                        # __LINE__     -> 13

def GetFrame(sel):
  callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
  frame = callerframerecord[0]
  info = inspect.getframeinfo(frame)
  if sel == "file":
    return info.filename                      # __FILE__     -> Test.py
  elif sel == "func":
    return info.function                      # __FUNCTION__ -> Main
  elif sel == "line":
    return info.lineno                        # __LINE__     -> 13