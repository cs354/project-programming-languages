#!/usr/bin/python3

import os
import sys
import random
import subprocess


def run():
  langs = ["c", "ruby", "shell", "mysql"]
  langs = ["mysql","c","shell"]

  if len(sys.argv) > 1:
    newlangs = []
    for lang in sys.argv[1:]:
      if lang in langs:
        newlangs.append(lang)
      else:
        print("Ignoring language {}".format(lang))
    langs = newlangs

  total_passed = 0
  total_tests = 0
  cwd = os.getcwd()

  for lang in langs:
    print("Testing {}...\n{}".format(lang, "-"*70))

    os.chdir("{}/{}".format(os.path.dirname(__file__), lang))
    print('Building...')
    p = os.popen('./build')
    print(p.read())
    status = p.close()

    testcount = 4
    successcount = 0
    linecount = 0

    if status is not None:
      print('Failed to build.')

    else:
      if lang == 'c': testcount = 3
      if lang == 'mysql': testcount = 5
      if lang == 'shell': testcount = 8
      command = os.popen('./testrig', 'r')

      while True:
        line = command.readline()
        if not line: break
        linecount += 1
        if linecount > testcount:
          print('Error: saw too many lines. Make sure you aren\'t printing anything.')
          successcount = 0
          break

        if lang == 'python':
          if (line.strip() == 'True'): successcount += 1
        else:
          if (line.strip() == 'correct'): successcount += 1

      command.close()

    os.chdir(cwd)
    print("Passed {} out of {} tests.\n".format(successcount, testcount))
    total_passed += successcount
    total_tests += testcount

  os.chdir(cwd)
  return total_passed, total_tests

if __name__ == '__main__':
  run()
