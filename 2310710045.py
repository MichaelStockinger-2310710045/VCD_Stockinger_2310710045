__doc__ = "main method"

#import system libs
import argparse
import sys

#own modules
from plots.plot import exec_sample_plot_

#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("slip", type=int, help="slip argument")
arg_parser_.add_argument("mass", type=int, help="mass argument")
arg_parser_.add_argument("mu", type=float, help="mu argument")
arg_parser_.add_argument("--pdf_file_out", type=str, help="filename to plot")
cmd_call_args_ = arg_parser_.parse_args()
if cmd_call_args_.pdf_file_out != None:
  print (cmd_call_args_.pdf_file_out)
else:
  cmd_call_args_.pdf_file_out = "out.pdf"
if cmd_call_args_.slip != 0:
  print (cmd_call_args_.slip)
if cmd_call_args_.mass != 0:
  print (cmd_call_args_.mass)
if cmd_call_args_.mu != 0:
  print (cmd_call_args_.mu)

#===============
# a method
def main_method():
  main_method.__doc__ = "main method"
  #exec_sample_plot_(cmd_call_args_.pdf_file_out)
  exec_sample_plot_(cmd_call_args_.slip, cmd_call_args_.mass, cmd_call_args_.mu, cmd_call_args_.pdf_file_out)

#===============
# do work and call a methode
main_method()

#terminate program
sys.exit()