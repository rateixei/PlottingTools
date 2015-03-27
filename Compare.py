#!/bin/python
from ROOT import *
import getopt, sys
def CompareTH1F(h_pass, h_total, legend, norm):
	leg = TLegend(0.6,0.7,0.89,0.89)
	leg.SetFillStyle(0)
	leg.SetLineWidth(0)
	leg.SetBorderSize(0)
	leg.AddEntry(h_pass, str(legend.split(':')[0]), "l")
	leg.AddEntry(h_total, str(legend.split(':')[1]), "l")

	h_pass.SetLineWidth(3)
	h_pass.SetLineColor(1)
	h_total.SetLineWidth(3)
	h_total.SetLineColor(2)

	if(norm):
		n_pass = h_pass.Integral()
		h_pass.Scale(1./n_pass)
		n_tot = h_total.Integral()
		h_total.Scale(1./n_tot)

	c = TCanvas("a", "a", 800, 800)
	c.SetFillColor(0)
	c.SetBorderMode(0)
	c.SetFrameFillStyle(0)
	c.SetFrameBorderMode(0)
	c.SetTickx(0)
	c.SetTicky(0)
   	c.SetGrid()

	h_pass.SetStats(0)
	h_pass.Draw()
	h_total.Draw('same')
	if legend is not '':
		leg.Draw('same')
	name = "plots/Compare_" + str(h_pass.GetName()) + "_" + str(h_total.GetName()) + ".pdf"
	c.SaveAs(name)
