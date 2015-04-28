#!/bin/python

from ROOT import *
from doPull import *
import getopt, sys

def main(argv):
	ROOT.gROOT.SetBatch()
	st_dataF = ''
	st_dataN = 'Data'
	st_mcF = ''
	st_mcN = 'MC'
	st_hist = ''
	st_var = ''
	is_norm = 1
	try:
		opts, args = getopt.getopt(argv,"d:m:n:",["data=","mc=", "histName=", "help", "dataName=", "mcName=", "varName=", "drawNormOff"])
	except getopt.GetoptError:
		print 'PullPlotter.py -data <inputfile> -mc <inputfile> -histName <name>'
		sys.exit(2)
	if len(opts) == 0:
		print 'PullPlotter.py -data <inputfile> -mc <inputfile> -histName <name>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'PullPlotter.py -data <inputfile> -mc <inputfile> -histName <name>'
			sys.exit()
		elif opt in ("-d", "--data"):
			st_dataF = arg
		elif opt in ("-m", "--mc"):
			st_mcF = arg
		elif opt in ("-n", "--histName"):
			st_hist = arg
		elif opt in ("--dataName"):
			st_dataN = arg
		elif opt in ("--mcName"):
			st_mcN = arg
		elif opt in ("--varName"):
			st_var = arg
		elif opt in ("--drawNormOff"):
			is_norm = 0
			
	if st_dataF == '' or st_mcF == '' or st_hist == '':
		print 'PullPlotter.py -data <inputfile> -mc <inputfile> -histName <name>'
		sys.exit(2)
		
	dataF = TFile.Open(str(st_dataF), 'READ')
	dataHist = dataF.Get(str(st_hist))
	mcF = TFile.Open(str(st_mcF), 'READ')
	mcHist = mcF.Get(str(st_hist))
	
	doPull(dataHist, st_dataN, mcHist, st_mcN, 'minus', st_var, is_norm, st_hist)

if __name__ == "__main__":
	main(sys.argv[1:])
