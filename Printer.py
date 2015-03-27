#!/bin/python

from ROOT import *
from PrintTH1F import *
import getopt, sys

def main(argv):
	ROOT.gROOT.SetBatch()
	inputfile = ''
	outputfile = ''
	legend = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:l:",["input=","output=", "legend="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--input"):
			inputfile = arg
		elif opt in ("-o", "--output"):
			outputfile = arg
		elif opt in ("-l", "--legend"):
			legend = arg

	if inputfile == '':
		print "Specify input file: test.py -i <inputfile>"
		sys.exit()

	if outputfile == '':
		outputfile = 'output.root'

	print 'Input file is ', inputfile
	print 'Output file is ', outputfile
	print 'Legend for all histograms is ', legend	

	file = TFile(inputfile, 'READ')
	list = file.GetListOfKeys()
	for i in xrange(0,list.GetEntries()):
		obj = list[i]
		hist = file.Get(obj.GetName())
		cname =  obj.GetClassName()
		if str(cname) == 'TH1F':
			PrintTH1F(hist,legend)
		

if __name__ == "__main__":
	main(sys.argv[1:])

'''
def PrintTH1F(hist, legend):
	leg = TLegend(0.6,0.7,0.89,0.89);
	leg.SetFillStyle(0);
	leg.SetLineWidth(0);
	leg.SetBorderSize(0);
	leg.AddEntry(hist, legend, "l")

	c = TCanvas("a", "a", 800, 800)
	c.SetFillColor(0);
	c.SetBorderMode(0);
	c.SetFrameFillStyle(0);
	c.SetFrameBorderMode(0);
	c.SetTickx(0);
	c.SetTicky(0);
   	c.SetGrid();

	hist.SetStats(0);
	hist.SetLineWidth(2)
	hist.Draw()
	if legend is not '':
		leg.Draw('same')
	name = str(hist.GetName()) + ".pdf"
	hist.SaveAs(name)
'''
