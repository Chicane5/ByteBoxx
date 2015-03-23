<!DOCTYPE html>
<html lang="en" dir="ltr" class="client-nojs">
<head>
<meta charset="UTF-8" />
<title>Export Individual Orthophotos.py - Agisoft</title>
<meta name="generator" content="MediaWiki 1.24.1" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Agisoft (en)" />
<link rel="EditURI" type="application/rsd+xml" href="http://wiki.agisoft.com/w/api.php?action=rsd" />
<link rel="alternate" hreflang="x-default" href="/wiki/Export_Individual_Orthophotos.py" />
<link rel="alternate" type="application/atom+xml" title="Agisoft Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom" />
<link rel="stylesheet" href="http://wiki.agisoft.com/w/load.php?debug=false&amp;lang=en&amp;modules=mediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.skinning.interface%7Cmediawiki.ui.button%7Cskins.vector.styles&amp;only=styles&amp;skin=vector&amp;*" />
<meta name="ResourceLoaderDynamicStyles" content="" />
<style>a:lang(ar),a:lang(kk-arab),a:lang(mzn),a:lang(ps),a:lang(ur){text-decoration:none}
/* cache key: db1042778_wiki:resourceloader:filter:minify-css:7:82a81660b69ce378658bf6344ae2f5fa */</style>
<script src="http://wiki.agisoft.com/w/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector&amp;*"></script>
<script>if(window.mw){
mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Export_Individual_Orthophotos.py","wgTitle":"Export Individual Orthophotos.py","wgCurRevisionId":97,"wgRevisionId":97,"wgArticleId":70,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Export_Individual_Orthophotos.py","wgIsProbablyEditable":false,"wgRestrictionEdit":[],"wgRestrictionMove":[]});
}</script><script>if(window.mw){
mw.loader.implement("user.options",function($,jQuery){mw.user.options.set({"ccmeonemails":0,"cols":80,"date":"default","diffonly":0,"disablemail":0,"editfont":"default","editondblclick":0,"editsectiononrightclick":0,"enotifminoredits":0,"enotifrevealaddr":0,"enotifusertalkpages":1,"enotifwatchlistpages":1,"extendwatchlist":0,"fancysig":0,"forceeditsummary":0,"gender":"unknown","hideminor":0,"hidepatrolled":0,"imagesize":2,"math":1,"minordefault":0,"newpageshidepatrolled":0,"nickname":"","norollbackdiff":0,"numberheadings":0,"previewonfirst":0,"previewontop":1,"rcdays":7,"rclimit":50,"rows":25,"showhiddencats":0,"shownumberswatching":1,"showtoolbar":1,"skin":"vector","stubthreshold":0,"thumbsize":5,"underline":2,"uselivepreview":0,"usenewrc":0,"watchcreations":1,"watchdefault":1,"watchdeletion":0,"watchlistdays":3,"watchlisthideanons":0,"watchlisthidebots":0,"watchlisthideliu":0,"watchlisthideminor":0,"watchlisthideown":0,"watchlisthidepatrolled":0,"watchmoves":0,"watchrollback":0,
"wllimit":250,"useeditwarning":1,"prefershttps":1,"language":"en","variant-gan":"gan","variant-iu":"iu","variant-kk":"kk","variant-ku":"ku","variant-shi":"shi","variant-sr":"sr","variant-tg":"tg","variant-uz":"uz","variant-zh":"zh","searchNs0":true,"searchNs1":false,"searchNs2":false,"searchNs3":false,"searchNs4":false,"searchNs5":false,"searchNs6":false,"searchNs7":false,"searchNs8":false,"searchNs9":false,"searchNs10":false,"searchNs11":false,"searchNs12":false,"searchNs13":false,"searchNs14":false,"searchNs15":false,"variant":"en"});},{},{});mw.loader.implement("user.tokens",function($,jQuery){mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\"});},{},{});
/* cache key: db1042778_wiki:resourceloader:filter:minify-js:7:2ffb09fddb30ef53a64cefb237597916 */
}</script>
<script>if(window.mw){
mw.loader.load(["mediawiki.page.startup","mediawiki.legacy.wikibits","mediawiki.legacy.ajax","skins.vector.js"]);
}</script>
<!--[if lt IE 7]><style type="text/css">body{behavior:url("/w/skins/Vector/csshover.min.htc")}</style><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr ns-0 ns-subject page-Export_Individual_Orthophotos_py skin-vector action-view vector-animateLayout">
		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<div id="content" class="mw-body" role="main">
			<a id="top"></a>

						<h1 id="firstHeading" class="firstHeading" lang="en"><span dir="auto">Export Individual Orthophotos.py</span></h1>
						<div id="bodyContent" class="mw-body-content">
									<div id="siteSub">From Agisoft</div>
								<div id="contentSub"></div>
												<div id="jump-to-nav" class="mw-jump">
					Jump to:					<a href="#mw-navigation">navigation</a>, 					<a href="#p-search">search</a>
				</div>
				<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><pre>
#Batch export of orthophotos based on individual cameras or user selected cameras
#creates custom menu item

#compatibility Agisoft PhotoScan Pro 1.1.0 
#no arguments required

import os
import time
import random
import PhotoScan
from PySide import QtCore, QtGui


def intersect(p0, pn, l0, l):
	d = ((p0 - l0) * pn) / (l * pn)
	return d * l + l0
	
	
class ExportOrthoDlg(QtGui.QDialog):

	def __init__(self, parent):
	
		QtGui.QDialog.__init__(self, parent)
		
		self.blend_types = {&quot;Average&quot;: PhotoScan.BlendingMode.AverageBlending, &quot;Mosaic&quot;: PhotoScan.BlendingMode.MosaicBlending, &quot;Min intensity&quot;: PhotoScan.BlendingMode.MinBlending, &quot;Max Intensity&quot;: PhotoScan.BlendingMode.MaxBlending}

		self.setWindowTitle(&quot;Export individual orthophotos&quot;)
		
		self.btnQuit = QtGui.QPushButton(&quot;Quit&quot;)
		self.btnQuit.setFixedSize(130,50)
		
		self.btnP1 = QtGui.QPushButton(&quot;Export&quot;)
		self.btnP1.setFixedSize(130,50)
		
		self.pBar = QtGui.QProgressBar()
		self.pBar.setTextVisible(False)
		self.pBar.setFixedSize(150, 50)
		
		
		self.resTxt = QtGui.QLabel()
		self.resTxt.setText(&quot;Export resolution (m/pix):&quot;)
		self.resTxt.setFixedSize(130, 25)	
		
		self.blendTxt = QtGui.QLabel()
		self.blendTxt.setText(&quot;Blending mode:&quot;)
		self.blendTxt.setFixedSize(130, 25)	
		
		self.blendCmb = QtGui.QComboBox()  #texture type values
		self.blendCmb.setFixedSize(100, 25)
		for type in self.blend_types.keys():
			self.blendCmb.addItem(type)
		
		self.resEdt = QtGui.QLineEdit()
		self.resEdt.setPlaceholderText(&quot;export resolution (m/pix), e.g 0.01&quot;)
		self.resEdt.setFixedSize(100, 25)
		
		self.selTxt = QtGui.QLabel()
		self.selTxt.setText(&quot;Export for:&quot;)
		self.selTxt.setFixedSize(100, 25)	
		
		self.radioBtn_all = QtGui.QRadioButton(&quot;all cameras&quot;)
		self.radioBtn_sel = QtGui.QRadioButton(&quot;selected cameras&quot;)
		self.radioBtn_rnd = QtGui.QRadioButton(&quot;random 10 cameras&quot;)
	
		self.radioBtn_all.setChecked(True)
		self.radioBtn_rnd.setChecked(False)
		self.radioBtn_sel.setChecked(False)
		
		layout = QtGui.QGridLayout()   #creating layout
		layout.addWidget(self.resTxt, 0, 1)
		layout.addWidget(self.resEdt, 0, 2)
		layout.addWidget(self.blendTxt, 1, 1)
		layout.addWidget(self.blendCmb, 1, 2)
		layout.addWidget(self.selTxt, 0, 0)
		layout.addWidget(self.radioBtn_all, 1, 0)
		layout.addWidget(self.radioBtn_sel, 2, 0)
		layout.addWidget(self.radioBtn_rnd, 3, 0)
		layout.addWidget(self.btnP1, 4, 1)
		layout.addWidget(self.btnQuit, 4, 2)
		layout.addWidget(self.pBar, 3, 0, 5, 1)
		self.setLayout(layout)  
	
		proc_exp = lambda&#160;: self.exp_ortho()
		
		QtCore.QObject.connect(self.btnP1, QtCore.SIGNAL(&quot;clicked()&quot;), proc_exp)
		QtCore.QObject.connect(self.btnQuit, QtCore.SIGNAL(&quot;clicked()&quot;), self, QtCore.SLOT(&quot;reject()&quot;))	

		self.exec()
	
	def surf_height(self, chunk, photo):
	
		points_h = list()
		point_cloud = chunk.point_cloud
		points = point_cloud.points
		npoints = len(points)
		num_valid = 0
		
		point_index = 0
		for proj in point_cloud.projections[photo]: 
			
			track_id = proj.track_id
			while point_index &lt; npoints and points[point_index].track_id &lt; track_id:
				point_index += 1
			if point_index &lt; npoints and points[point_index].track_id == track_id:
				if not points[point_index].valid: 
					continue
			
			v = points[point_index].coord
			vt = chunk.transform.matrix.mulp(v)
			if chunk.crs:
				vt = chunk.crs.project(vt)
			points_h.append(vt[2])
			num_valid += 1
		
		points_h.sort()
		height = points_h[num_valid // 2]
		
		return height

	def exp_ortho(self):
	
		doc = PhotoScan.app.document
		chunk = doc.chunk
		path = doc.path.rsplit(&quot;\\&quot;, 1)[0]
		
		if not chunk.model:
			PhotoScan.app.messageBox(&quot;No mesh generated!\n&quot;)
			return False
		
		try:
			resolution = float(self.resEdt.text())
		except(ValueError):
			PhotoScan.app.messageBox(&quot;Incorrect export resolution! Please use point delimiter.\n&quot;)
			print(&quot;Script aborted.&quot;)
			return False

		print(&quot;Export started...&quot;)  #information message
		
		self.btnP1.setDisabled(True)
		self.btnQuit.setDisabled(True)
		self.pBar.setMinimum(0)
		self.pBar.setMaximum(100)
		
		export_list = list()
		if self.radioBtn_sel.isChecked():
			for photo in chunk.cameras:
				if photo.selected:
					export_list.append(photo)
		elif self.radioBtn_all.isChecked():
			export_list = list(chunk.cameras)
		elif self.radioBtn_rnd.isChecked():
			random_cams = random.sample(range(len(chunk.cameras)), 10) #number of random cameras
			for i in range (0, p_num):
				export_list.append(chunk.cameras[random_cams[i]])
		for photo in chunk.cameras:
			photo.enabled = False

		blending_mode = self.blend_types[self.blendCmb.currentText()]
			
		processed = 0
		t0 = time.time()

		for i in range (0, len(chunk.cameras)):
			photo = chunk.cameras[i]
			photo.enabled = False

		PhotoScan.app.update()

		for photo in export_list: 
			
			if not photo.transform:
				continue
			
			x0 = x1 = x2 = x3 = PhotoScan.Vector((0.0,0.0,0.0))
				
			width = photo.sensor.width
			height = photo.sensor.height
			calibration = photo.sensor.calibration

			# vectors corresponding to photo corners

			v0 = PhotoScan.Vector(( -calibration.cx / calibration.fx, -calibration.cy / calibration.fy, 1))
			v1 = PhotoScan.Vector(( (width - calibration.cx) / calibration.fx, -calibration.cy / calibration.fy, 1))
			v2 = PhotoScan.Vector(( -calibration.cx / calibration.fx, (height - calibration.cy) / calibration.fy, 1))
			v3 = PhotoScan.Vector(( (width - calibration.cx) / calibration.fx, (height - calibration.cy) / calibration.fy, 1))
			vc = photo.center	

			v0.size = v1.size = v2.size = v3.size = vc.size = 4 
			v0[3] = v1[3] = v2[3] = v3[3] = 0
			vc[3] = 1
			
			M = chunk.transform.matrix * photo.transform

			v0_gc = M * v0
			v1_gc = M * v1
			v2_gc = M * v2
			v3_gc = M * v3
			vc_gc = chunk.transform.matrix * vc
				
			v0_gc.size = v1_gc.size = v2_gc.size = v3_gc.size = vc_gc.size = 3

			# surface normal
			
			cen_p = photo.center
			cen_t = chunk.transform.matrix.mulp(cen_p)
			if chunk.crs:
				cen_t = chunk.crs.project(cen_t)
			
			h = self.surf_height(chunk, photo)
			
			vloc = PhotoScan.Vector((cen_t[0], cen_t[1], h))
			vloc_h = PhotoScan.Vector((cen_t[0], cen_t[1], h))
			vloc_h[2] += 1

			if chunk.crs:
				vloc_gc = chunk.crs.unproject(vloc)
				vloc_h_gc = chunk.crs.unproject(vloc_h)
				surf_n =  vloc_h_gc - vloc_gc
			else:
				vloc_gc = vloc
				vloc_h_gc = vloc_h
				surf_n = vloc_h - vloc
				
			surf_n.normalize()
			v0_gc.normalize()
			v1_gc.normalize()
			v2_gc.normalize()
			v3_gc.normalize()
			
			#intersection with the surface
			
			x0 = intersect(vloc_gc, surf_n, vc_gc, v0_gc)
			x1 = intersect(vloc_gc, surf_n, vc_gc, v1_gc)
			x2 = intersect(vloc_gc, surf_n, vc_gc, v2_gc)
			x3 = intersect(vloc_gc, surf_n, vc_gc, v3_gc)
			
			if chunk.crs:
				x0 = chunk.crs.project(x0)
				x1 = chunk.crs.project(x1)
				x2 = chunk.crs.project(x2)
				x3 = chunk.crs.project(x3)

			x_0 = min(x0[0],  x1[0], x2[0], x3[0])
			x_1 = max(x0[0],  x1[0], x2[0], x3[0])
			y_0 = min(x0[1],  x1[1], x2[1], x3[1])
			y_1 = max(x0[1],  x1[1], x2[1], x3[1])

			x_0 -= (x_1 - x_0) / 20.
			x_1 += (x_1 - x_0) / 20.
			y_0 -= (y_1 - y_0) / 20.
			y_1 += (y_1 - y_0) / 20.
			
			reg = (x_0, y_0, x_1, y_1)
			
			photo.enabled = True
			PhotoScan.app.update()
			p_name = photo.photo.path.rsplit(&quot;/&quot;, 1)[1].rsplit(&quot;.&quot;,1)[0]
			p_name = &quot;ortho_&quot; + p_name
			
			if chunk.crs:
				proj = chunk.crs   ##export in chunk coordinate system
			else:
				proj = PhotoScan.Matrix().diag([1,1,1,1]) #TopXY
			d_x = d_y = resolution
			
			#recalculating WGS84 resolution from degrees into meters if required
			if chunk.crs:
				if ('UNIT[&quot;degree&quot;' in proj.wkt):
					crd = photo.reference.location

					#longitude
					v1 = PhotoScan.Vector((crd[0], crd[1], 0) )
					v2 = PhotoScan.Vector((crd[0] + 0.001, crd[1], 0))
					vm1 = chunk.crs.unproject(v1)
					vm2 = chunk.crs.unproject(v2)
					res_x = (vm2 - vm1).norm() * 1000

					#latitude
					v2 = PhotoScan.Vector( (crd[0], crd[1] + 0.001, 0))
					vm2 = chunk.crs.unproject(v2)
					res_y = (vm2 - vm1).norm() * 1000
						
					pixel_x = pixel_y = resolution  #export resolution (meters/pix)
					d_x = pixel_x / res_x  
					d_y = pixel_y / res_y
							
			
			if chunk.exportOrthophoto(path + &quot;\\&quot; + p_name + &quot;.tif&quot;, format = &quot;tif&quot;, blending = blending_mode, color_correction = False, projection = proj, region = reg, dx = d_x, dy = d_y, write_world = True):
				processed +=1
			photo.enabled = False
			self.pBar.setValue(int(processed / len(export_list) * 100))
			
		for i in range (0, len(chunk.cameras)):
			photo = chunk.cameras[i]
			photo.enabled = True

		PhotoScan.app.update()


		self.btnP1.setDisabled(False)
		self.btnQuit.setDisabled(False)
		
		t1 = time.time()

		t1 -= t0
		t1 = int(t1)

		PhotoScan.app.messageBox(&quot;Processing finished.\nProcessed &quot;+ str(processed) +&quot; images to orthophotos.\nProcessing time: &quot;+ str(t1)  +&quot; seconds.\nPress OK.&quot;)  #information message
		
		return 1

def main():

	global doc
	doc = PhotoScan.app.document

	app = QtGui.QApplication.instance()
	parent = app.activeWindow()
	
	dlg = ExportOrthoDlg(parent)
		
		
PhotoScan.app.addMenuItem(&quot;Custom/Export individual orthophotos&quot;, main)
</pre>

<!-- 
NewPP limit report
CPU time usage: 0.012 seconds
Real time usage: 0.024 seconds
Preprocessor visited node count: 4/1000000
Preprocessor generated node count: 24/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key db1042778_wiki:pcache:idhash:70-0!*!*!*!*!*!* and timestamp 20150323093040 and revision id 97
 -->
</div>									<div class="printfooter">
						Retrieved from "<a dir="ltr" href="http://wiki.agisoft.com/w/index.php?title=Export_Individual_Orthophotos.py&amp;oldid=97">http://wiki.agisoft.com/w/index.php?title=Export_Individual_Orthophotos.py&amp;oldid=97</a>"					</div>
													<div id='catlinks' class='catlinks catlinks-allhidden'></div>												<div class="visualClear"></div>
							</div>
		</div>
		<div id="mw-navigation">
			<h2>Navigation menu</h2>

			<div id="mw-head">
									<div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label">
						<h3 id="p-personal-label">Personal tools</h3>
						<ul>
							<li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Export+Individual+Orthophotos.py" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o">Log in</a></li><li id="pt-createaccount"><a href="/wiki/Special:RequestAccount">Request account</a></li>						</ul>
					</div>
									<div id="left-navigation">
										<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
						<h3 id="p-namespaces-label">Namespaces</h3>
						<ul>
															<li  id="ca-nstab-main" class="selected"><span><a href="/wiki/Export_Individual_Orthophotos.py"  title="View the content page [c]" accesskey="c">Page</a></span></li>
															<li  id="ca-talk" class="new"><span><a href="/w/index.php?title=Talk:Export_Individual_Orthophotos.py&amp;action=edit&amp;redlink=1"  title="Discussion about the content page [t]" accesskey="t">Discussion</a></span></li>
													</ul>
					</div>
										<div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label">
												<h3 id="p-variants-label"><span>Variants</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
									</div>
				<div id="right-navigation">
										<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
						<h3 id="p-views-label">Views</h3>
						<ul>
															<li id="ca-view" class="selected"><span><a href="/wiki/Export_Individual_Orthophotos.py" >Read</a></span></li>
															<li id="ca-viewsource"><span><a href="/w/index.php?title=Export_Individual_Orthophotos.py&amp;action=edit"  title="This page is protected.&#10;You can view its source [e]" accesskey="e">View source</a></span></li>
															<li id="ca-history" class="collapsible"><span><a href="/w/index.php?title=Export_Individual_Orthophotos.py&amp;action=history"  title="Past revisions of this page [h]" accesskey="h">View history</a></span></li>
													</ul>
					</div>
										<div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label">
						<h3 id="p-cactions-label"><span>More</span><a href="#"></a></h3>

						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
										<div id="p-search" role="search">
						<h3>
							<label for="searchInput">Search</label>
						</h3>

						<form action="/w/index.php" id="searchform">
														<div id="simpleSearch">
															<input type="search" name="search" placeholder="Search" title="Search Agisoft [f]" accesskey="f" id="searchInput" /><input type="hidden" value="Special:Search" name="title" /><input type="submit" name="fulltext" value="Search" title="Search the pages for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton" /><input type="submit" name="go" value="Go" title="Go to a page with this exact name if exists" id="searchButton" class="searchButton" />								</div>
						</form>
					</div>
									</div>
			</div>
			<div id="mw-panel">
				<div id="p-logo" role="banner"><a style="background-image: url(/w/resources/assets/photoscan.png);" href="/wiki/Main_Page"  title="Visit the main page"></a></div>
						<div class="portal" role="navigation" id='p-navigation' aria-labelledby='p-navigation-label'>
			<h3 id='p-navigation-label'>Navigation</h3>

			<div class="body">
									<ul>
													<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
													<li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r">Recent changes</a></li>
													<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random page [x]" accesskey="x">Random page</a></li>
													<li id="n-help"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents" title="The place to find out">Help</a></li>
											</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id='p-tb' aria-labelledby='p-tb-label'>
			<h3 id='p-tb-label'>Tools</h3>

			<div class="body">
									<ul>
													<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Export_Individual_Orthophotos.py" title="A list of all wiki pages that link here [j]" accesskey="j">What links here</a></li>
													<li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Export_Individual_Orthophotos.py" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li>
													<li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li>
													<li id="t-print"><a href="/w/index.php?title=Export_Individual_Orthophotos.py&amp;printable=yes" rel="alternate" title="Printable version of this page [p]" accesskey="p">Printable version</a></li>
													<li id="t-permalink"><a href="/w/index.php?title=Export_Individual_Orthophotos.py&amp;oldid=97" title="Permanent link to this revision of the page">Permanent link</a></li>
													<li id="t-info"><a href="/w/index.php?title=Export_Individual_Orthophotos.py&amp;action=info">Page information</a></li>
											</ul>
							</div>
		</div>
				</div>
		</div>
		<div id="footer" role="contentinfo">
							<ul id="footer-info">
											<li id="footer-info-lastmod"> This page was last modified on 6 February 2015, at 14:08.</li>
											<li id="footer-info-viewcount">This page has been accessed 125 times.</li>
									</ul>
							<ul id="footer-places">
											<li id="footer-places-privacy"><a href="/wiki/Agisoft:Privacy_policy" title="Agisoft:Privacy policy">Privacy policy</a></li>
											<li id="footer-places-about"><a href="/wiki/Agisoft:About" title="Agisoft:About">About Agisoft</a></li>
											<li id="footer-places-disclaimer"><a href="/wiki/Agisoft:General_disclaimer" title="Agisoft:General disclaimer">Disclaimers</a></li>
									</ul>
										<ul id="footer-icons" class="noprint">
											<li id="footer-poweredbyico">
															<a href="//www.mediawiki.org/"><img src="/w/resources/assets/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" width="88" height="31" /></a>
													</li>
									</ul>
						<div style="clear:both"></div>
		</div>
		<script>/*<![CDATA[*/window.jQuery && jQuery.ready();/*]]>*/</script><script>if(window.mw){
mw.loader.state({"site":"ready","user":"ready","user.groups":"ready"});
}</script>
<script>if(window.mw){
mw.loader.load(["mediawiki.action.view.postEdit","mediawiki.user","mediawiki.hidpi","mediawiki.page.ready","mediawiki.searchSuggest"],null,true);
}</script>
<script>if(window.mw){
mw.config.set({"wgBackendResponseTime":411});
}</script>
	</body>
</html>
	