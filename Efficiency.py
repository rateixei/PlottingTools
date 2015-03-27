#!/bin/python
from ROOT import *
import getopt, sys
def EfficiencyTH1F(h_pass, h_total, legend):
#	hist = TEfficiency(TH1F(h_pass),TH1F(h_total))
#	hist = TEfficiency(AddressOf(h_pass),AddressOf(h_total))
	hist = TEfficiency(h_pass,h_total)

	leg = TLegend(0.6,0.7,0.89,0.89);
	leg.SetFillStyle(0);
	leg.SetLineWidth(0);
	leg.SetBorderSize(0);
	leg.AddEntry(hist, legend, "p")

	c = TCanvas("a", "a", 800, 800)
	c.SetFillColor(0);
	c.SetBorderMode(0);
	c.SetFrameFillStyle(0);
	c.SetFrameBorderMode(0);
	c.SetTickx(0);
	c.SetTicky(0);
   	c.SetGrid();

#	hist.SetStats(0);
	hist.SetLineWidth(2)
	hist.Draw()
	if legend is not '':
		leg.Draw('same')
	name = "plots/Efficiency_" + str(h_pass.GetName()) + "_" + str(h_total.GetName()) + ".pdf"
	c.SaveAs(name)
