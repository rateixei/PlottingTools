#!/bin/python
from ROOT import *
import getopt, sys
def PrintTH1F(hist, legend):
	leg = TLegend(0.6,0.7,0.89,0.89)
	leg.SetFillStyle(0)
	leg.SetLineWidth(0)
	leg.SetBorderSize(0)
	leg.AddEntry(hist, legend, "l")

	c = TCanvas("a", "a", 900, 600)
	c.SetFillColor(0)
	c.SetBorderMode(0)
	c.SetFrameFillStyle(0)
	c.SetFrameBorderMode(0)
	c.SetTickx(0)
	c.SetTicky(0)
   	c.SetGrid()

	histname = hist.GetName()
	if 'chiso' in histname or 'phiso' in histname or 'nhiso' in histname or 'hoe' in histname:
		c.SetLogy()

	hist.SetStats(0)
	hist.SetLineWidth(3)
	hist.Draw()
	if legend is not '':
		leg.Draw('same')
	name = "plots/" + str(hist.GetName()) + ".pdf"
	c.SaveAs(name)
