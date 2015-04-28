from ROOT import *

def doPull(data, dataName, mc, mcName, Type, varName, norm, histName):
	ROOT.gROOT.SetBatch()
	data_nbins = data.GetNbinsX()
	mc_nbins = mc.GetNbinsX()
	
	data.SetLineWidth(3)
	data.SetLineColor(1)
	mc.SetLineWidth(3)
	mc.SetLineColor(kAzure-3)
	mc.SetFillColor(kAzure-3)
	mc.SetFillStyle(3251)
	
	if norm:
		tot_data = data.Integral()
		data.Scale(1./tot_data)
		tot_mc = mc.Integral()
		mc.Scale(1./tot_mc)
	if( data_nbins != mc_nbins ):
		print 'Number of bins of histograms being compared are not the same!'
		return 0
	
	Type = 'minus'
	if Type is not 'minus':
		if Type is not 'over':
			print 'Type must be either minus or over'
			return 0
			
	pull = data.Clone()
	pull.SetNameTitle("", "")
	pull.Reset()
	pull.SetMarkerStyle(20)
	
	for x in xrange(0,data_nbins):
		n_data = data.GetBinContent(x+1)
		n_mc = mc.GetBinContent(x+1)
#		if n_mc == 0:
#			continue 
		diff = n_data - n_mc
		print diff
		pull.SetBinContent(x+1, diff)
		pull.SetBinError(x+1, 0)
		
	
	max_data = data.GetMaximum()
	max_mc = mc.GetMaximum()
	if(max_mc < max_data):
		mc.GetYaxis().SetRangeUser(0, max_data*1.1)
		
	leg = TLegend(0.6,0.8,0.89,0.89)
	leg.SetFillStyle(0)
	leg.SetLineWidth(0)
	leg.SetBorderSize(0)
	if not dataName:
		leg.AddEntry(data, "Data", "l")
		leg.AddEntry(mc, "MC", "f")
	if dataName:
		leg.AddEntry(data, str(dataName), "l")
		leg.AddEntry(mc, str(mcName), "f")

	data.GetYaxis().SetTitleOffset(1.5)
	mc.GetYaxis().SetTitleOffset(1.5)

	c0 = TCanvas("c0", "c0", 1000, 800)
	c0.cd()
	mc.Draw()
	data.Draw("same")
	leg.Draw("same")
	compare_name = str(histName) + "_compare.pdf"
	c0.SaveAs(compare_name)
	
	ratio = 0.3
	epsilon = 0.10
	c1 = TCanvas("c1", "c1", 800, 800)
	SetOwnership(c1,False) #If I don't put this, I get memory leak problems...
	p1 = TPad("pad1","pad1", 0, float(ratio - epsilon), 1, 1)
	SetOwnership(p1,False)
	p1.SetBottomMargin(epsilon)
#	p1.SetBottomMargin(0.000)
	p2 = TPad("pad2","pad2",0,0,1,float(ratio*(1-epsilon)) )
	p2.SetFillColor(0)
	p2.SetFillStyle(0)
	p2.SetTopMargin(0.000)
	SetOwnership(p2,False)
	p2.SetBottomMargin(0.35)
	p2.SetGridx()
	p2.SetGridy()
		
#	data.GetYaxis().SetLabelSize(0.025)
	data.GetXaxis().SetLabelSize(0.0)
#	data.GetYaxis().SetTitleOffset(1.5)
	data.GetYaxis().SetTitleSize(0.03)
#	mc.GetYaxis().SetLabelSize(0.025)
	mc.GetXaxis().SetLabelSize(0.0)
	mc.GetYaxis().SetTitleOffset(1.5)
	mc.GetYaxis().SetTitleSize(0.03)

	mc.SetMinimum(0.0001)
	
	pull.GetYaxis().SetNdivisions(8)
	
	if not dataName:
		pull.GetYaxis().SetTitle("Data - MC")
	if dataName:
		st_ypull = str(dataName[0:4]) + ' - ' + str(mcName[0:4]) 
		pull.GetYaxis().SetTitle(str(st_ypull))
	pull.GetYaxis().SetTitleSize(0.08)
	pull.GetYaxis().SetTitleOffset(0.5)
			
	if not varName:
		pull.GetXaxis().SetTitle("")
	if varName:
		pull.GetXaxis().SetTitle(str(varName))
		pull.GetXaxis().SetTitleSize(0.12)
		pull.GetXaxis().SetTitleOffset(0.95)
		data.SetTitle(varName)
		mc.SetTitle(varName)

	pull.GetXaxis().SetLabelSize(0.12)
	pull.GetYaxis().SetLabelSize(0.05)		
#	pull.GetYaxis().SetLimits(1.2, -1.2)	
	pull.SetMaximum(0.007)
	pull.SetMinimum(-0.007)

	p1.cd()
	mc.Draw()
	data.Draw("same")
	leg.Draw("same")
	p2.cd()
	pull.Draw("p0")
	c1.cd()
	p1.Draw()
	p2.Draw()
	c1.Update()
	pull_name = str(histName) + "_pull.pdf"
	c1.SaveAs(pull_name)
